from flask import Flask
from flask_login import LoginManager, login_required

app = Flask(__name__)

# login関連の処理
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@app.route('/')
@login_required
def index():
    return "hell world"

@app.route('/login', methods=["GET", "POST"])
def login_form():
    print("aa")
    return "hello world"

if __name__ == "__main__":
    app.debug = True
    app.run()
