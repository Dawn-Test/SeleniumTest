# 商城的登录页面，账户出错
# v1 模型：无法批量运行
# 导包
from selenium import  webdriver
# 获取driver对象
driver = webdriver.Chrome(r"d:\webdrivers\chromedriver.exe")
# 最大化浏览器
driver.maximize_window()
# 隐式等待
driver.implicitly_wait(30)
# 打开URL
driver.get("http//localhost")
# 点击登录连接
driver.find_element_by_link_text("登录").click()
# 输入用户名
driver.find_element_by_css_selector("#suername").send_keys("001112222")
# 输入密码
driver.find_element_by_css_selector("#password").send_keys("123456")
# 输入验证码
driver.find_element_by_css_selector("#verify_code").send_keys("88888")
# 点击登录按钮
driver.find_element_by_css_selector(".J-login-submit").click()
# 获取错误提示信息
msg = driver.find_element_by_css_selector(".layui").text
print("msg",msg)
# 断言
assert msg == "用户名不存在"
# 点击提示框确定按钮
driver.find_element_by_css_selector(".lagui-btn0").click()
# 关闭
driver.quit()