# .sen_keys()  输入方法
# .click()     点击方法
# .clear()     清空
# 注：输入方法前要进行清空操作


# 导包
from selenium import webdriver
from time import sleep

# 获取浏览器对象
driver = webdriver.Chrome(r'd:\webdrivers\chromedriver.exe')

# 打开url
crl = ""
driver.get(crl)
# 输入admin
driver.find_element_by_css_selector("#userA").send_keys("admin")
# 输入密码123456
driver.find_element_by_css_selector("#password").send_keys("123456")
# 输入电话7758521
driver.find_element_by_css_selector(".tel").send_keys("7758521")
# 输入邮箱123@qq.com
driver.find_element_by_css_selector("#emali").send_keys("123@qq.com")
# 暂停3秒
sleep(3)
# 修改电话号码 123456789
driver.find_element_by_css_selector(".tel").clear()
driver.find_element_by_css_selector(".tel").send_keys("123456789")
# 暂停3秒
sleep(3)
# 点击注册按钮
driver.find_element_by_css_selector("button").click()
# 暂停3秒
sleep(3)
# 关闭浏览器
driver.quit()