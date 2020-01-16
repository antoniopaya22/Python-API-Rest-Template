from .app import App

application = App(__name__)
application.config()
db = application.get_db()
app = application.get_app()

from .routes import user_routes, auth_routes
