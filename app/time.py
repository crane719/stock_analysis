from flask import Blueprint, render_template, request, jsonify, Response
from flask_login import login_required, current_user
import finance
import json

time = Blueprint('time', __name__)

@time.route('/timeseries')
def timeseries():
    return render_template('time.html')

@time.route('/get_time', methods=["GET"])
def get_timeseries():
    brand = request.args.get("brand")
    api = current_user.id
    times = finance.get(api, brand)
    json = times.to_json()
    return jsonify(json)
