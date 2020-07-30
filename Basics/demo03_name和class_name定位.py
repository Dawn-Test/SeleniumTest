# 登录页面tag_name方法相同

from time import sleep

# name定位
# 导包
from selenium import webdriver

# 获取浏览器对象
driver = webdriver.Chrome(r'd:\webdrivers\chromedriver.exe')

# 打开URL
url = r'路径'
driver.ger(url)

# 查找用户名输入admin
driver.find_element_by_name('urlA').send_keys('admin')
# 查找密码输入123456
driver.find_element_by_name('passwordA').send_keys('123456')
# 暂停3秒
sleep(3)
# 关闭浏览器
driver.quit()

# class_name定位
# 导包
from selenium import webdriver
from time import sleep

# 获取浏览器对象
driver = webdriver.Chrome(r'd:\webdrivers\chromedriver.exe')

# 打开URL
url = r'路径'
driver.ger(url)

# 查找电话输入1564561651
driver.find_element_by_class_name('telA').send_keys('1564561651')
# 查找邮箱输入2123@11.com
driver.find_element_by_class_name('emailA').send_keys('2123@11.com')
# 暂停3秒
sleep(3)
# 关闭浏览器
driver.quit()

