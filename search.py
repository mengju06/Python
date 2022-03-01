#用selenium查詢關鍵字
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'https://www.google.com/'
key = "鮭魚"

driver = webdriver.Chrome()
driver.get(url)

driver.find_element_by_xpath("//input[@class='gLFyf gsfi']").send_keys(key)
driver.find_element_by_xpath("//input[@class='gLFyf gsfi']").send_keys(Keys.ENTER)
