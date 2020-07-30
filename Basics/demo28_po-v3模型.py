"""
页面对象层：
页面对象编写技巧：
     类名：使用大驼峰将模块名称潮进来，有下划线去掉下划线
     方法：根据业务需求每个操作步骤单独封装一个方法
           方法名page_xxx
"""
from selenium import webdriver
class PageLogin:
    def __init__(self):
        # 获取driver对象
        self.driver = webdriver.Chrome(r"d:\webdrivers\chromedriver.exe")
        # 最大化浏览器
        self.driver.maximize_window()
        # 隐式等待
        self.driver.implicitly_wait(30)
        # 打开URL
        self.driver.get("http//localhost")
    # 点击登录连接
    def page_click_login_link(self):
        self.driver.find_element_by_link_text("登录").click()
    # 输入用户名
    def page_input_username(self,username):
        self.driver.find_element_by_css_selector("#username").send_keys("1")
    # 输入密码
    def page_input_pwd(self,pwd):
        self.driver.find_element_by_css_selector("#password").send_keys("1")
    # 输入验证码
    def page_input_verify_code(self,code):
        self.driver.find_element_by_css_selector("#verify_code").send_keys("88888")
    # 点击登录
    def page_get_text(self):
        self.driver.find_element_by_css_selector("#verify_code").click()

    # 获取异常提示信息
    def page_get_text(self):
        return self.driver.find_element_by_css_selector(".layui").text
    # 点击提示框确定按钮
    def page_click_err_btn_ok(self):
        self.driver.find_element_by_css_selector(".lagui-btn0").click()
    # 组装登录业务方法，给业务层调用
    def page_login(self,username,pwd,code):
        self.page_click_login_link()
        self.page_input_username()
        self.page_input_pwd()
        self.page_input_verify_code()
        self.page_get_text()
