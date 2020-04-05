from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
import finance

time = Blueprint('time', __name__)

@time.route('/timeseries')
def timeseries():
    return render_template('time.html')

@time.route('/get_time', methods=["GET"])
@login_required
def get_timeseries():
    brand = request.args.get("brand")
    api = current_user.id
    times = finance.get(api, brand)
    return times
