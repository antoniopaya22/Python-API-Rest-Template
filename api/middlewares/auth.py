import time

from api.repository.user_repository import UserRepository
import hashlib, binascii
from flask import abort
from functools import wraps
from flask import Flask, request, jsonify, make_response
import jwt


class Auth:

    def __init__(self):
        self.user_repository = UserRepository()
        self.secret = "secretAPI-RESTnodejs1234$"

    def login(self, request):
        username = request.json['username']
        password = request.json['password']
        user = self.user_repository.get_user_by_name(username)
        if user is None:
            return {"Result": False, "Error": "El usuario no existe"}
        salt = hashlib.sha256(self.secret.encode('ascii')).hexdigest().encode('ascii')
        hash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                   salt, 100000)
        hash = binascii.hexlify(hash).hex()
        if user.hash == hash:
            token = jwt.encode({"username": user.username, 'exp': int(time.time()) + 3600 * 24},
                               self.secret, algorithm='HS256')
            return token
        else:
            abort(400, "Contraseña incorrecta")


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        if not token:
            return jsonify({"meassage": "Token is missing"}), 401
        try:
            jwt.decode(token, "secretAPI-RESTnodejs1234$", algorithm='HS256')
        except jwt.ExpiredSignatureError or jwt.InvalidTokenError:
            return jsonify({"message": "Token is invalid"}), 401
        return f(*args, **kwargs)

    return decorated
