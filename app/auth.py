from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, UserMixin

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET"])
def login():
    return render_template("login.html")

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.index"))

@auth.route("/login_post", methods=["POST"])
def login_post():
    key = request.form["key"]
    user = User()
    user.id = key
    login_user(user)
    return redirect(url_for("main.index"))

class User(UserMixin):
    pass
