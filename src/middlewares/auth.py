from src.repository.user_repository import UserRepository
import hashlib, binascii, os

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
            return {"Result": True}
        else:
            return {"Result": False, "Error": "Contraseña incorrecta"}