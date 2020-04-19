from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
import finance
import datetime as dt
import numpy as np

time = Blueprint('time', __name__)

@time.route('/timeseries')
def timeseries():
    return render_template('time.html')

@time.route('/get_time', methods=["GET"])
def get_timeseries():
    brand = request.args.get("brand")
    stock_type = request.args.get("type")
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    api = current_user.id
    times = finance.get(api, brand)
    start_date = [int(num) for num in start_date.split("-")]
    end_date = [int(num) for num in end_date.split("-")]
    times = times[
            (times.index >= dt.datetime(start_date[0],start_date[1],start_date[2])) &\
            (times.index < dt.datetime(end_date[0],end_date[1],end_date[2]))]
    times.index = times.index.astype(str)
    jsons = times[stock_type].to_json(orient="split")
    return jsonify(jsons)

@time.route("/moving_average", methods=["POST"])
def moving_average():
    datas = request.json
    point = int(datas["point"].split("pt")[0])
    del datas["point"]

    tmp_datas = {}
    if type(datas["labels"])==str:
        datas["labels"] = [datas["labels"]]
        datas["datas"] = [datas["datas"]]
    for key, data in zip(datas["labels"], datas["datas"]):
        data = finance.moving_average(data, point)
        key += "ma%d"%(point)
        tmp_datas[key] = data
    return jsonify(tmp_datas)
