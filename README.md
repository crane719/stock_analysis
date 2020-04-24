# stock_analysis

## prerequired
pythonを用いて、quandl apiから、株価のデータを取得します。そのため、quandlに登録する必要があります。

1. https://www.quandl.com/ に登録
2. Login
3. account settings
4. api keyをメモ

## usage

一回目だけ、
```
pip install -r requirements.txt
```

```
python run.py
```

## function

- 株価時系列の表示、削除
- 株価の移動平均の取得
