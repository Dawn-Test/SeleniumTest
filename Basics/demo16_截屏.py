import time
from time import sleep
# 导包 webdriver
from selenium import webdriver

# 获取谷歌浏览器对象
driver = webdriver.Chrome(r'd:\webdrivers\chromedriver.exe')

"""
目标：截屏
方法：
     driver.get_screenshot_as_file()
需求：
     1.输入用户名
     2.截图 当前目录 admin.png
"""
# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
driver.get('https://www.baidu.com')
# 输入 admin
driver.find_element_by_css_selector("#user").send_keys("admin")
# 调用截图方法
# driver.get_screenshot_as_file("./admin.png")
# 获取文件名称，使用时间戳
driver.get_screenshot_as_file("../image/%s.png"% (time.strftime("%Y_%m_%d"%H_%M_%S)))
# 暂停三秒

sleep(3)
# 退出浏览器
driver.quit()