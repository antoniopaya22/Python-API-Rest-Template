import binascii
import hashlib

from flask import abort
from api.models.user import User
from api.repository.user_repository import UserRepository

secret = "secretAPI-RESTnodejs1234$"


class UserController:

    @staticmethod
    def add_user(request):
        salt = hashlib.sha256(secret.encode('ascii')).hexdigest().encode('ascii')
        hash = hashlib.pbkdf2_hmac('sha512', request.json['password'].encode('utf-8'),
                                   salt, 100000)
        hash = binascii.hexlify(hash).hex()
        user = User(
            username=request.json['username'],
            lastname=request.json['lastname'],
            hash=hash,
            salt=salt.hex()
        )
        if UserRepository.add_user(user):
            return {"Result": True}
        else:
            return abort(400, "Error al añadir el usuario")

    @staticmethod
    def delete_user(id):
        if UserRepository.delete_user(id):
            return {"Result": True}
        else:
            return abort(400, "Error al eliminar el usuario con id" + str(id))

    @staticmethod
    def get_user_by_id(id):
        user = UserRepository.get_user_by_id(id)
        return user.to_json() if user is not None else abort(400, "No existe un usuario con id: " + str(id))

    @staticmethod
    def get_all_users():
        users = UserRepository.get_all_users()
        return [x.to_json() for x in users]
