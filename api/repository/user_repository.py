from api.models.user import User
from api import db


class UserRepository:

    @staticmethod
    def add_user(user):
        try:
            db.session.add(user)
            db.session.commit()
        except:
            return False
        return True

    @staticmethod
    def delete_user(id):
        try:
            User.query.filter_by(id=id).delete()
            db.session.commit()
        except:
            return False
        return True

    @staticmethod
    def get_user_by_name(name):
        try:
            return User.query.filter_by(username=name).one()
        except:
            return None

    @staticmethod
    def get_user_by_id(id):
        try:
            return User.query.get(id)
        except:
            return None

    @staticmethod
    def get_all_users():
        try:
            return User.query.all()
        except:
            return []
