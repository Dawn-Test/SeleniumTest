#              1）context_click()              #右击
#             2）double_click()              #双击
#             3）drag_and_drop()         #拖拽
#             4）move_to_element()     #悬停
#             5）perform()                    #执行以上事件方法

# 导包
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import keys
# 获取浏览器对象
driver = webdriver.Chrome(r'd:\webdrivers\chromedriver.exe')

# 打开URL
url = r'路径'
driver.ger(url)

# 实例化并获取 actionchalins类
action = ActionChains(driver)
# 定位用户名，自用户名上右击鼠标、预期：粘贴
username = driver.find_element_by_css_selector("#user")
action.context_click(username).perform()
# 发送admin  并进行双击 ，预期：选择admin
username.send_keys("admin")
action.double_click(username).perform()
# 移动到注册按钮上，预期：按钮变色
action.move_to_element(driver.find_element_by_css_selector("属性名")).perform()
sleep(3)
# 关闭浏览器
driver.quit()