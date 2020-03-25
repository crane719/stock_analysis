from flask import Blueprint, render_template, request
import finance

time = Blueprint('time', __name__)

@time.route('/timeseries')
def timeseries():
    return render_template('time.html')

@time.route('/get_time', methods=["GET"])
def get_timeseries():
    print("aaaaaaa")
    brand = request["brand"]
    api = current_user.id
    times = finance.get(api, brand)
    print(times)
    return times
