from api.models.user import User
from api import application


class UserRepository:

    def __init__(self):
        self.db = application.get_db()

    def add_user(self, user):
        try:
            self.db.session.add(user)
            self.db.session.commit()
        except:
            return False
        return True

    def delete_user(self, id):
        try:
            User.query.filter_by(id=id).delete()
            self.db.session.commit()
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
