"""
需求：
    1.使用绝对路径定位 用户名输入admin
    2.暂停2秒
    3.使用相对路径定位密码框输入123
方法：
    driver.find_element_by_xpach()
"""
# 导包
from selenium import webdriver
from time import sleep

# 获取浏览器驱动对象4
driver = webdriver.Chrome(r'd:\webdrivers\chromedriver.exe')

# 打开注册a.html
url = r'路径'
driver.ger(url)

# 使用绝对路径定位用户名admin
driver.find_element_by_xpath("/html/boby/div/p[1]/input").send_keys("admin")

# 暂停2秒
sleep(2)

# 使用相对路径定位密码123
driver.find_element_by_xpath("//input[@id='password']").send_keys('123')

# 暂停3秒
sleep(3)

# 关闭浏览器
driver.quit()


"""
需求：
    1.使用css id选择器定位 用户名输入admin
    2.使用css属性选择，定位密码框输入123456
    3.使用css class 选择器定位电话号码
    4.使用css 元素选择器 定位span标签获取文本值
    5.使用层级选择器 定位email 输入123@qq.com
方法：
    driver.find_element_by_css_selector\()
"""
# 导包
from selenium import webdriver
from time import sleep



# 获取浏览器驱动对象4
driver = webdriver.Chrome(r'd:\webdrivers\chromedriver.exe')

# 打开注册a.html
url = r'路径'
driver.ger(url)

# 使用cssid选择器定位用户名输入admin
driver.find_element_by_css_selector('#user').send_keys('admin')
# 2.使用css属性选择，定位密码框输入123456
driver.find_element_by_css_selector("[name='passwordA']").send_keys("123456")
# 3.使用css class 选择器定位电话号码
driver.find_element_by_css_selector(".telA").send_keys("12345456787")
# 4.使用css 元素选择器 定位span标签获取文本值
span = driver.find_element_by_css_selector("span").text
print("获取的span标签文本值：",span)
# 5.使用层级选择器 定位email 输入123@qq.com
driver.find_element_by_css_selector("p>input[属性='电子邮箱']").send_keys('123@qq.com')

# 暂停3秒
sleep(3)

# 关闭浏览器
driver.quit()
