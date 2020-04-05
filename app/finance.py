import quandl

def get(api, brand):
    quandl.ApiConfig.api_key = api
    print(api, brand)
    data = quandl.get(dataset=brand, returns="pandas")
    return data
