#樂透開獎號碼爬蟲
import requests
from bs4 import BeautifulSoup
url = 'https://www.taiwanlottery.com.tw/'
r = requests.get(url)
sp = BeautifulSoup(r.text, 'lxml')

datas = sp.find('div', class_='contents_box02')

title = datas.find('span', 'font_black15').text
print('威力彩期數：', title)

nums = datas.find_all('div', class_='ball_tx ball_green')

print('開出順序：', end=' ')
for i in range(0,6):
    print(nums[i].text, end=' ')
print('\n大小順序：', end=' ')
for i in range(6,12):
    print(nums[i].text, end=' ')
num = datas.find('div', class_='ball_red').text
print('\n第二區：', num)
