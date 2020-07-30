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


     需求：
         1.点击alert按钮
         2.输入用户名admin

"""
# 定位aleat按钮 并点击
driver.find_element_by_css_selector("#aleata").click()

# 切换到alert
# 默认返回alert默认值
at = driver.switch_to_alert()
# 处理对话框
# 同意
at.accept()

# 获取文本
print("警告信息：",at.text)


# 取消
at.dismiss()
# 定位 用户名 输入admin
driver.find_element_by_css_selector("#userA").send_keys("admin")
# 暂停3秒
sleep(3)
# 关闭浏览器
driver.quit()

# 滚动条操作

# 导包
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


     需求：滚动条操作
         1.暂停2秒
         2.滚动条拉倒最底下
"""
# 第一步  设置js控制滚动条语句
js = "window.scrollTo(0,10000)"
# 第二部  调通js语句方法
driver.execute_script(js)
# 暂停3秒
sleep(3)
# 关闭浏览器
driver.quit()