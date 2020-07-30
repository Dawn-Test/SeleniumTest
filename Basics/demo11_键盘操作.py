# 键盘对应的方法在keys中
# 包：from selenium.webdriver.common.keys import Keys
#

# 导包
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
# 获取浏览器对象
driver = webdriver.Chrome(r'd:\webdrivers\chromedriver.exe')

# 打开URL
url = r'路径'
driver.ger(url)

# 定位用户名
username = driver.find_element_by_css_selector("#userA")
# 输入admin
username.send_keys("admim1")
# 删除1
username.send_keys(Keys.BACK_SPACE)
# 全选admin  ctrl+a
username.send_keys(Keys.CONTROL,"a")
# 复制 Ctrl+c
username.send_keys(Keys.CONTROL,"C")
# 复制密码 并执行 Ctrl+v
driver.find_element_by_css_selector("#password").send_keys(Keys.CONTROL,"c")
sleep(3)
# 关闭浏览器
driver.quit()