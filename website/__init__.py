from flask import Flask
from authlib.integrations.flask_client import OAuth
from flask_sqlalchemy import SQLAlchemy
from os import path, getenv
from flask_login import LoginManager
from dotenv import load_dotenv

db = SQLAlchemy()

load_dotenv()

app_config = {
    "OAUTH2_CLIENT_ID": getenv("OAUTH2_CLIENT_ID"),
    "OAUTH2_CLIENT_SECRET": getenv("OAUTH2_CLIENT_SECRET"),
    "OAUTH2_META_URL": getenv("OAUTH2_META_URL"),
    "FLASK_SECRET": getenv("FLASK_SECRET"),
    "DB_NAME": getenv("DB_NAME")
}

print(app_config)

oauth = OAuth()

oauth.register("notes_app",
               client_id=app_config.get("OAUTH2_CLIENT_ID"),
               client_secret=app_config.get("OAUTH2_CLIENT_SECRET"),
               server_metadata_url=app_config.get("OAUTH2_META_URL"),
               client_kwargs={
                   "scope": "openid profile email https://www.googleapis.com/auth/user.birthday.read https://www.googleapis.com/auth/user.gender.read"
               })


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = app_config.get("FLASK_SECRET")
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{app_config.get('DB_NAME')}"

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get((int(id)))

    return app


def create_database(app):
    if not path.exists("website/" + app_config.get('DB_NAME')):
        with app.app_context():
            db.create_all()
            print("Created Database!")
