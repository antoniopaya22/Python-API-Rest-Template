from flask import Flask
from flask_cors import CORS
from .config import Config
from flask_sqlalchemy import SQLAlchemy

class App():

    def __init__(self, name):
        self.app = Flask(name)
        self.db = SQLAlchemy()

    def init_app(self):
        CORS(self.app)
        self.config()
        self.db.init_app(self.app)
        with self.app.app_context():
            # Imports parts of out app
            self.import_routes()
            self.db.create_all()
            return self.app

    def import_routes(self):
        from .routes import auth_routes
        from .routes import user_routes

    def config(self):
        self.app.config.from_object(Config)

    def get_db(self):
        return self.db

    def get_app(self):
        return self.app

    def get_migrate(self):
        return self.migrate


# START
application = App(__name__)
app = application.get_app()
db = application.get_db()
application.init_app()