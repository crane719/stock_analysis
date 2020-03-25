from flask import Flask
from flask_login import LoginManager, UserMixin

from .main import main as main_blueprint
from .auth import auth as auth_blueprint
from .time import time as time_blueprint
from .auth import User

def create_app():
    app = Flask(__name__)
    app.secret_key = "secret_keyyyy"

    # login処理
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        user = User()
        user.id = user_id
        return user

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(time_blueprint)

    return app


app = create_app()
