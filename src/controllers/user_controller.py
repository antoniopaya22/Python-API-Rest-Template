from src.models.user import User
from src.repository.user_repository import UserRepository
import hashlib, binascii, os

class UserController:

    def __init__(self):
        self.user_repository = UserRepository()
        self.secret = "secretAPI-RESTnodejs1234$"

    def add_user(self, request):
        salt = hashlib.sha256(self.secret.encode('ascii')).hexdigest().encode('ascii')
        hash = hashlib.pbkdf2_hmac('sha512', request.json['password'].encode('utf-8'),
                                      salt, 100000)
        hash = binascii.hexlify(hash).hex()
        user = User(
            firstName=request.json['firstName'],
            lastName=request.json['lastName'],
            hash=hash,
            salt=salt.hex()
        )
        if self.user_repository.add_user(user):
            return {"Result": True}
        else:
            return {"Result": False, "Error": "Error al añadir el usuario"}

    def delete_user(self, id):
        if self.user_repository.delete_user(id):
            return {"Result": True}
        else:
            return {"Result": False, "Error": "Error al eliminar el usuario con id"+str(id)}

    def get_user_by_id(self, id):
        user = self.user_repository.get_user_by_id(id)
        return user.to_json() if user is not None else {
            "Result": False,
            "Error": "No existe un usuario con id: "+ str(id)
        }

    def get_all_users(self):
        users = self.user_repository.get_all_users()
        return [x.to_json() for x in users]