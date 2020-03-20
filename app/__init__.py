from flask import Flask
from flask_login import LoginManager, UserMixin

from .main import main as main_blueprint
from .auth import auth as auth_blueprint

def create_app():
    app = Flask(__name__)

    # login処理
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user():
        returnUser.get()

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)

    return app

class User(UserMixin):
    pass

app = create_app()
