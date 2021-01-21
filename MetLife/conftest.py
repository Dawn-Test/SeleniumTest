#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

import pytest
import requests
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager import chrome, firefox, microsoft, utils

from common.logger import logger
from page.base_page import BasePage
import numpy as np

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    """
    用例失败后自动截图
    """
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')
        # 判断用例是否失败或者xfail跳过的测试
        if (report.skipped and xfail) or (report.failed and not xfail):
            # 获取测试用例代码中webDriver参数来获取浏览器进行抓屏
            for i in item.funcargs:
                if isinstance(item.funcargs[i], WebDriver):
                    # 截图
                    BasePage(item.funcargs[i]).capture_page_screen(description='失败截图')
                    break
        report.extra = extra


@pytest.fixture
def create_driver(request):
    # Todo 1.传递参数创建driver;2.增加创建driver的自定义参数
    if request.param:
        browser = request.param
    else:
        browser = 'gc'
    if browser in ['google chrome', 'chrome', 'gc']:
        try:
            driver = webdriver.Chrome(chrome.ChromeDriverManager(log_level=logging.WARN).install())
        except requests.exceptions.ConnectionError:
            logger.warning('自动化下载驱动失败，使用系统配置驱动')
            driver = webdriver.Chrome()

    elif browser in ['mobile', 'gcm']:
        mobileEmulation = {'deviceName': 'iPhone X'}
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation', mobileEmulation)
        try:
            driver = webdriver.Chrome(chrome.ChromeDriverManager(log_level=logging.WARN).install(),
                                      chrome_options=options)
        except ConnectionError:

            driver = webdriver.Chrome(chrome_options=options)

    elif browser in ['firefox', 'ff']:
        driver = webdriver.Firefox(executable_path=firefox.GeckoDriverManager().install())

    elif browser in ['ie', 'internet explorer']:
        caps = DesiredCapabilities.INTERNETEXPLORER
        caps['nativeEvents'] = False
        try:
            driver = webdriver.Ie(microsoft.IEDriverManager(os_type='Win32', log_level=logging.WARN).install(),
                                  capabilities=caps)
        except requests.exceptions.ConnectionError:
            logger.warning('自动化下载驱动失败，使用系统配置驱动')
            driver = webdriver.Ie(capabilities=caps)
    else:
        driver = webdriver.Edge()
    driver.maximize_window()
    driver.speed = 1
    yield driver
    # driver.quit()


if __name__ == '__main__':
    print(utils.os_type())
