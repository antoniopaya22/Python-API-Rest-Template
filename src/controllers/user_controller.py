from src.models.user import User
from src import db

class UserController:

    def add_user(self, request):
        user = User(
            firstName = request.json['firstName'],
            lastName = request.json['lastName'],
            hash = request.json['hash'],
            salt = request.json['salt']
        )
        db.session.add(user)
        db.session.commit()
        return True

    def delete_user(self, id):
        User.query.filter_by(id=id).delete()
        db.session.commit()
        return True

    def get_user_by_id(self, id):
        return User.query.get(id).to_json()

    def get_all_users(self):
        return [x.to_json() for x in User.query.all()]