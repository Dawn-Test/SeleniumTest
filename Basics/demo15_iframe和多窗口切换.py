from selenium import webdriver
from time import sleep

# 获取浏览器对象
driver = webdriver.Chrome(r'd:\webdrivers\chromedriver.exe')
# 设置元素等待   隐式等待  重要！！！
# 设置隐式等待10秒。
driver.implicitly_wait(5)
# 打开URL
url = 'https://www.taobao.com'
driver.get(url)
"""
目标 ：frame表单

     需求：
         1.打开注册实例
         2.填写主页面 页面信息
         3.填写注册a 页面信息
         4.填写注册b 页面信息
"""
"""填写主页面"""
# 用户名
driver.find_element_by_css_selector("#user").send_keys("admin")
# 密码
driver.find_element_by_css_selector("#password").send_keys("123")
# 电话
driver.find_element_by_css_selector(".tel").send_keys("1231232")
# 邮件
driver.find_element_by_css_selector("#email").send_keys("123@qq.com")

# 切换到注册a
driver.switch_to_frame("myframe1")
"""填写注册a"""
# 用户名
driver.find_element_by_css_selector("#user").send_keys("admin")
# 密码
driver.find_element_by_css_selector("#password").send_keys("123")
# 电话
driver.find_element_by_css_selector(".tel").send_keys("1231232")
# 邮件
driver.find_element_by_css_selector("#email").send_keys("123@qq.com")

# 切换到默认目录
driver.switch_to.default_content()
# 切换到注册b
driver.switch_to_frame("myframe2")
"""填写注册b"""
# 用户名
driver.find_element_by_css_selector("#user").send_keys("admin")
# 密码
driver.find_element_by_css_selector("#password").send_keys("123")
# 电话
driver.find_element_by_css_selector(".tel").send_keys("1231232")
# 邮件
driver.find_element_by_css_selector("#email").send_keys("123@qq.com")
# 暂停3秒
sleep(3)
# 关闭浏览器
driver.quit()



"""多窗口切换"""

from selenium import webdriver
from time import sleep

# 获取浏览器对象
driver = webdriver.Chrome(r'd:\webdrivers\chromedriver.exe')
# 设置元素等待   隐式等待  重要！！！
# 设置隐式等待10秒。
driver.implicitly_wait(5)
# 打开URL
url = 'https://www.taobao.com'
driver.get(url)
"""
目标 ：切换窗口

     需求：
         1.打开注册实例
         2.点击注册a网页
         3.填写注册a网页内容
"""

# 获取当前窗口句柄   目的：判断只要不是当前主窗口句柄，1就新开一个
current = driver.current_window_handle
print("当前窗口句柄为：",current)
# 点击注册a网页
driver.find_element_by_link_text("a网页").click()

# 获取所有窗口句柄
handles = driver.window_handles

# 判断不是当前窗口句柄
for handles in handles:
    if handles != current:
        driver.switch_to.window(handles)
             # 切换

# 切换到注册a
driver.switch_to_frame("myframe1")
"""填写注册a"""
# 用户名
driver.find_element_by_css_selector("#user").send_keys("admin")
# 密码
driver.find_element_by_css_selector("#password").send_keys("123")
# 电话
driver.find_element_by_css_selector(".tel").send_keys("1231232")
# 邮件
driver.find_element_by_css_selector("#email").send_keys("123@qq.com")

# 暂停3秒
sleep(3)
# 关闭浏览器
driver.quit()



