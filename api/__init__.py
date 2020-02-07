from flask import Flask
from .config import get_mode
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(mode):
    """Construct the core application."""
    app = Flask(__name__)
    app.config.from_object(get_mode(mode))
    db.init_app(app)

    with app.app_context():
        # Imports Routes
        from .routes import auth_routes
        from .routes import user_routes

        # Create tables for models
        db.create_all()

        return app
