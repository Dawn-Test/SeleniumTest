# 导包
import unittest
from selenium import webdriver
# 新街测试类  并继承
class TestLogin(unittest.TestCase):
    driver = None
    # 初始化 setup
    @classmethod
    def sefUpClass(cls):
        # 获取driver对象
        cls.driver = webdriver.Chrome(r"d:\webdrivers\chromedriver.exe")
        # 最大化浏览器
        cls.driver.maximize_window()
        # 隐式等待
        cls.driver.implicitly_wait(30)
        # 打开URL
        cls.driver.get("http//localhost")
        # 点击登录连接
        cls.driver.find_element_by_link_text("登录").click()

    # 结束 teardown
    @classmethod
    def tearDownClass(cls):
        # 关闭浏览器
        cls.driver.quit()
    # 新建测试方法  用户名不存在
    def test_login_username_not_exist(self):
        driver = self.driver
        # 输入用户名
        username = driver.find_element_by_css_selector("#suername")
        username.clear()
        username.send_keys("001112222")
        # 输入密码
        pwd  = driver.find_element_by_css_selector("#password")
        pwd.clear()
        pwd.send_keys("123456")
        # 输入验证码
        yanzhengma = driver.find_element_by_css_selector("#verify_code")
        yanzhengma.clear()
        yanzhengma.send_keys("88888")
        # 点击登录按钮
        driver.find_element_by_css_selector(".J-login-submit").click()
        # 获取错误提示信息
        msg = self.driver.find_element_by_css_selector(".layui").text
        print("msg", msg)
        try:
            # 断言
            self.assertEqual(msg,"账号不存在！")
            # 点击提示框确定按钮
            self.driver.find_element_by_css_selector(".lagui-btn0").click()
        except AssertionError:
            # 截图
            self.driver.get_screenshot_as_file("../1.png")
    # 新建测试方法 密码错误
    def tearDownClass(cls):
        driver = self.driver
        # 输入用户名
        username = driver.find_element_by_css_selector("#suername")
        username.clear()
        username.send_keys("001112222")
        # 输入密码
        pwd  = driver.find_element_by_css_selector("#password")
        pwd.clear()
        pwd.send_keys("12346")
        # 输入验证码
        yanzhengma = driver.find_element_by_css_selector("#verify_code")
        yanzhengma.clear()
        yanzhengma.send_keys("88888")
        # 点击登录按钮
        driver.find_element_by_css_selector(".J-login-submit").click()
        # 获取错误提示信息
        msg = driver.find_element_by_css_selector(".layui").text
        print("msg", msg)
        try:
            # 断言
            driver.assertEqual(msg,"密码错误！")
            # 点击提示框确定按钮
            driver.find_element_by_css_selector(".lagui-btn0").click()
        except AssertionError:
            # 截图
            driver.get_screenshot_as_file("../1.png")


