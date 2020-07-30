# 导包
from selenium import webdriver
from time import sleep

# 获取浏览器对象
webdriver = webdriver.Chrome(r'd:\webdrivers\chromedriver.exe')
# 打开url
# url = r" "d:缺少url文件路径"
# driver.get(url)
# 查找用户名元素
# username = driver.find_element_by_id('userA')
# 查找密码元素
# password = driver.find_element_by_id('passwordA')
# 用户输入admin sed_keys（内容）
# username.send_keys("admin")
# # 用户输入123456
# password.send_keys("123456")
# # 暂停三秒
sleep(3)
# 退出浏览器驱动
