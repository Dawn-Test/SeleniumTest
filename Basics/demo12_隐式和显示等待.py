# 隐式等待

# 导包
from selenium import webdriver
from time import sleep

# 获取浏览器对象
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(r'd:\webdrivers\chromedriver.exe')
# 设置元素等待   隐式等待  重要！！！
# 设置隐式等待10秒。
driver.implicitly_wait(5)
# 打开URL
url = 'https://www.baidu.com'
driver.get(url)
"""

目标：隐式等待使用

"""
# 给出一个错误的id，不能做到，如果直接抛出异常，说明等待失效。反之。。
driver.find_element_by_css_selector("#user").send_keys("admin")
# 暂停3秒
sleep(3)
# 关闭浏览器
driver.quit()

# 显示等待

# 导包
from selenium import webdriver
from time import sleep

# 获取浏览器对象
driver = webdriver.Chrome(r'd:\webdrivers\chromedriver.exe')
# 设置元素等待   隐式等待  重要！！！
# 设置隐式等待10秒。
driver.implicitly_wait(5)
# 打开URL
url = 'https://www.baidu.com'
driver.get(url)
"""

目标：显示等待使用
     操作：
         1.导包webdriverwait()类
         2.实例化webdriverwait()类，并调用until（method）方法
           metgod：匿名函数
           lambda x：x.find_element_by_id()
    
     需求：
         定位用户名，输入admin

"""
# 实例化webdriverwait()类，并调用until（method）方法
# 调用until方法返回的一定是一个元素
username = WebDriverWait(driver,timeout=30,poll_frequency=0.5).until(lambda x:x.find_element_by_id("#userA"))
# 输入值
username.send_keys("admin")
# 暂停3秒
sleep(3)
# 关闭浏览器
driver.quit()