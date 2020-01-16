from src.models.user import User
from src import db

class UserRepository:

    def add_user(self, user):
        try:
            db.session.add(user)
            db.session.commit()
        except:
            return False
        return True

    def delete_user(self, id):
        try:
            User.query.filter_by(id=id).delete()
            db.session.commit()
        except:
            return False
        return True

    def get_user_by_name(self, name):
        return User.query.filter_by(firstName=name).one()

    def get_user_by_id(self, id):
        return User.query.get(id)

    def get_all_users(self):
        try:
            return User.query.all()
        except:
            return []