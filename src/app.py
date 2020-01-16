from flask import Flask
from flask_cors import CORS
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

class App():

    def __init__(self, name):
        self.app = Flask(name)
        self.config()

    def config(self):
        CORS(self.app)
        self.app.config.from_object(Config)
        self.db = SQLAlchemy(self.app)
        self.migrate = Migrate(self.app, self.db)

    def get_db(self):
        return self.db

    def get_app(self):
        return self.app

    def get_migrate(self):
        return self.migrate