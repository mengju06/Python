import twstock
import time
import requests

def LINE_Notify(token, msg):
    headers = {
    "Authorization": "Bearer " + token, 
    "Content-Type" : "application/x-www-form-urlencoded"
    }
    
    payload = {'message':msg}
    notify = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return notify.status_code

def sendline(mode, realprice, counterLine, token):
    print('長榮航目前股價：' + str(realprice))
    if mode == 1:
        message = '現在長榮航股價為 ' + str(realprice) + '元，達賣出目標價'
    else:
        message = '現在長榮航股價為 ' + str(realprice) + '元，請注意'
    code = LINE_Notify(token, message)
    if code == 200:
        counterLine = counterLine + 1
        print(' 第 ' + str(counterLine) + ' 次發送 LINE 訊息。')
    else:
        print('發送 LINE訊息失敗')
    return counterLine

token = 'yE9pAeywZi9ByM5tEy8NN8c5zM93GPCTDZLcENxgE5e'
counterLine = 0
counterError = 0

print('程式開始')
while True:
    real = twstock.realtime.get('2618')
    if real['success']:
        realprice = real['realtime']['latest_trade_price']
        if float(realprice) >= 30:
            counterLine = sendline(1, realprice, counterLine, token)
        elif float(realprice) <= 25:
            counterLine = sendline(2, realprice, counterLine, token)
        if counterLine >= 33:
            print('程式結束')
            break
    else:
        print('錯誤:' + real['rtmessage'])
        counterError = counterError + 1
        if counterError >= 3:
            print('程式結束')
            break
        
    for i in range(600):
        time.sleep(1)
        
        
        
        
        
        
        
        
        
        