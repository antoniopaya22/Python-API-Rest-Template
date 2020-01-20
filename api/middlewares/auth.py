import time

from api.repository.user_repository import UserRepository
import hashlib, binascii
from flask import abort
import jwt

class Auth:

    def __init__(self):
        self.user_repository = UserRepository()
        self.secret = "secretAPI-RESTnodejs1234$"

    def login(self, request):
        firstName = request.json['firstName']
        password = request.json['password']
        user = self.user_repository.get_user_by_name(firstName)
        if user is None:
            return {"Result": False, "Error": "El usuario no existe"}
        salt = hashlib.sha256(self.secret.encode('ascii')).hexdigest().encode('ascii')
        hash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                   salt, 100000)
        hash = binascii.hexlify(hash).hex()
        if user.hash == hash:
            token = jwt.encode({"firstName": user.firstName, 'exp': int(time.time()) + 3600 * 24},
                               self.secret, algorithm='HS256')
            return token
        else:
            abort(400,"Contraseña incorrecta")

    def verify_token(self, token):
        try:
            jwt.decode(token, self.secret, algorithm='HS256')
            return True
        except jwt.ExpiredSignatureError:
            return False
        except jwt.InvalidTokenError:
            return False

    def login_required(self, request, fn):
        token = request.headers['Authorization'] if 'Authorization' in request.headers else ''
        if self.verify_token(token):
            return fn
        else:
            abort(401, "Unauthorized Access")