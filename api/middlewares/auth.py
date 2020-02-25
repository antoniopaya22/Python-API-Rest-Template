import binascii
import hashlib
import time
import jwt
import os

from functools import wraps
from flask import abort
from flask import request, jsonify
from api.repository.user_repository import UserRepository

secret = os.environ.get('SECRET') or "secretAPI-RESTnodejs1234$"


class Auth:

    @staticmethod
    def login(request):
        username = request.json['username']
        password = request.json['password']
        user = UserRepository.get_user_by_name(username)
        if user is None:
            return {"Result": False, "Error": "El usuario no existe"}, 401
        salt = hashlib.sha256(secret.encode('ascii')).hexdigest().encode('ascii')
        hash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                   salt, 100000)
        hash = binascii.hexlify(hash).hex()
        if user.hash == hash:
            token = jwt.encode({"username": user.username, 'exp': int(time.time()) + 3600 * 24},
                               secret, algorithm='HS256')
            return token
        else:
            return {"Result": False, "Error": "Contraseña incorrecta"}, 401


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
