#!/usr/bin/env python3
# coding=utf-8
import allure
from selenium.webdriver.remote.webdriver import WebDriver

from page.base_page import BasePage


class TestHomerBasePage(BasePage):


    @allure.step("打开testhomer")
    def open(self):
        self.open_url(url='https://testerhome.com/')
