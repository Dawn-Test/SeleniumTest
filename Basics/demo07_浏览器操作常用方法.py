# 浏览器常用api
# 最大化：driver.maximize_window()
# 设置浏览器大小：driver.set_window_size(300,200)
# 设置浏览器位置：driver.set_window_position(320,150)
# 浏览器后退：driver.back()
# 浏览器前进：driver.forward()
# 浏览器刷新：driver.refresh()
# 关闭当前主窗口：driver.close()
# 关闭所有窗口：driver.quit()
# 获取当前页面title信息：driver.title
# 获取当前页面url信息：driver.current_url

# 注意：
# 1. driver.title 和 driver.current_url 没有括号，一般用于判断上部操作是否成功
# 2. driver.maximize_window()  一般为前置代码，获取driver后，直接编写最大化浏览器




# 导包
from selenium import webdriver
from time import sleep

# 获取浏览器对象
driver = webdriver.Chrome(r'd:\webdrivers\chromedriver.exe')

# 打开url
driver.get('https://www.baidu.com')

# 将浏览器最大化
driver.maximize_window()
# 暂停两秒
sleep(2)
# 设置固定大小300.200
driver.set_window_size(300,200)
# 暂停2秒
sleep(2)
# 移动浏览器x:320,y:150
driver.set_window_position(320,150)
# 暂停2秒
sleep(2)
# 最大化
driver.maximize_window()
# 点击访问新浪网站
driver.find_element_by_partial_link_text("访问").click()
# 暂停两秒
sleep(2)
# 执行后退
driver.back()
# 暂停2秒
sleep(2)
# 执行前进
driver.forward()
# 暂停3秒
sleep(3)
# 关闭浏览器
driver.quit()




# 导包
from selenium import webdriver
from time import sleep

# 获取浏览器对象
driver = webdriver.Chrome(r'd:\webdrivers\chromedriver.exe')

# 打开url
driver.get('https://www.baidu.com')

# 用户名输入：admin  目的：刷新————清空
driver.find_element_by_css_selector("#cserA").send_keys("admin")
# 暂停2秒
sleep(2)
# 刷新
driver.refresh()
# 获取title
title  = driver.title
print("当前页面title：",title)
# 获取当前url
current = driver.current_url
print("当前页面的url地址：",current)
# 点击注册a网页，打开新窗口
driver.find_element_by_link_text("注册A网页").click()
# 关闭主窗口
driver.close()
# 暂停3秒
sleep(3)
# 关闭浏览器
driver.quit()