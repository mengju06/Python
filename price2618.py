#查詢個股股價測試
import twstock

stock = twstock.Stock('2618')
print("近6筆收盤價")
print(stock.price[-6:])

while True:
    real = twstock.realtime.get('2618')
    if real['success']:
        print("即時股票資料：")
        print(real)
        print("目前股價：")
        print(real['realtime']['latest_trade_price'])
        break
    else:
        print("錯誤：" + real['rtmessage'])
