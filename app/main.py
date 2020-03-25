from flask import Blueprint, render_template, request
import finance
import flask_login

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')
