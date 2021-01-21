import allure
from page_locators.login_page_locator import LoginPageLocator
from config import config
from testcase.mdes_base_case import MdesBaseCase

class Login(MdesBaseCase):

    @allure.step("登陆mdes")
    def login(self):

        self.driver.get(config.get_config("MDES", "url"))   #???????
        self.input_text(LoginPageLocator.usrname, config.get_config("MDES", "username"))
        self.input_text(LoginPageLocator.password, config.get_config("MDES", "password"))
        self.click_element(LoginPageLocator.loginBTN)
        # with allure.step('登陆状态截图'):
        #     self.get_screenshot('获取登陆状态̬')   #？？？这个get_screenshot方法那里继承的？
