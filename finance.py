import quandl

def get(api, brand):
    quandl.ApiConfig.api_key = api
    print(api, brand)
    print("aaa")
    data = quandl.get(dataset=brand, returns="pandas")
    return data
