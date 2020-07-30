from time import sleep
# 导包 webdriver
from selenium import webdriver

# 获取谷歌浏览器对象
driver = webdriver.Chrome(r'd:\webdrivers\chromedriver.exe')

# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
driver.get('http://demo6.tp-shop.cn/')
# 暂停三秒
sleep(3)
# 退出浏览器
driver.quit()



