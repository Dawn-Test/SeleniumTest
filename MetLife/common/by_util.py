#!/usr/bin/env python3
# coding=utf-8
from selenium.webdriver.common.by import By as SeleniumBy


class By(SeleniumBy):
    JQUERY_SELECTOR = "jquery selector"
    GROUP_NAME_SELECTOR = 'group name selector'
