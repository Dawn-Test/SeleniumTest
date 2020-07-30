# import unittest
"""
目标：unittest常用 断言
      1.assertTrue:如果结果为True通过，否则失败
      

"""

# class Test01(unittest.TestCase):
#     def test001(self):
#         flag = True
        # flag = False
        # 断言是否为True
        # self.assertTrue(flag)

        # 判断两个字符是否相等
        # self.assertEqual("你好！","您好！")
        # self.assertEqual("你好！", "你好！")

        # 判断后面的字符串是否包含前面的字符串
        # self.assertIn("您好","您好，王先生")
        # self.assertIn("您好 ！","您好 王先生！")

        # 判断是否为none
        # self.assertIsNone(flag)


# 断言联系
"""
案例：
    输入正确的用户名和密码  验证码为空
    断言：提示信息是否为，验证码不能为空
    要求：如果断言出错，截屏保存

"""
# 导包
import unittest
from selenium import webdriver
from time import sleep
# 定义测试类 并继承 测试用例
class TestTphopLogin(unittest.TestCase):
    # 定义初始化方法
    def setUp(self):
        # 获取浏览器驱动对象
        self.driver = webdriver.Chrome(r'd:\webdrivers\chromedriver.exe')
        # 打开url
        self.driver.get("http//localhost")
        # 最大化浏览器
        self.driver.maximize_window()
        # 隐式等待
        self.driver.implicitly_wait(30)
    # 定义teardown
    def tearDown(self):
         # 关不浏览器驱动
         sleep(2)
         self.driver.quit()
    # 定义登录测试方法  验证码为空
    def yanzhengma(self):
        driver = self.driver
        # 点击登录链接
        driver.find_element_by_link_text("登录").click()
        # 输入用户名
        driver.find_element_by_css_selector("#username").send_keys('1234565')
        # 输入密码
        driver.find_element_by_css_selector("#password").send_keys("123456")
        # 输入验证码
        driver.find_element_by_css_selector("#verify_code").send_keys("")
        # 点击登录
        driver.find_element_by_css_selector(".J-login-submit").click()
        # 获取登录后的提示信息
        result = driver.find_element_by_css_selector(".layui-layer-content").text
        print("result:",result)
        # 定义预计结果
        expect_result = "验证码不能为空"
        try:
            # 断言
            self.assertEqual(result,expect_result)
        except AssertionError:
            # 截图
            driver.get_screenshot_as_file("../scripts/1.png")
            # 抛异常
            raise
