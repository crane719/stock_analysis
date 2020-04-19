import quandl
import numpy as np

def get(api, brand):
    quandl.ApiConfig.api_key = api
    data = quandl.get(dataset=brand, returns="pandas")
    return data

def moving_average(data, point):
    data_len = len(data)
    half_len = point//2
    pad = [0 for _ in range(half_len)]
    data = pad + data
    data = data + pad

    renew = []
    for i in range(data_len):
        renew.append(np.average(data[i:i+half_len*2+1]))
    return renew

