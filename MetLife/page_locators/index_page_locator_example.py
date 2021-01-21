#!/usr/bin/env python3
# coding=utf-8
from common.by_util import By
from page_locators.base_page_locator import BasePageLocator


class IndexPageLocator(BasePageLocator):
    head_title = (By.JQUERY_SELECTOR, '.title.media-heading:visible:first()', '最后一个head title')

    author=(By.XPATH,'//*[@id="main"]/div/div[1]/div[1]/div[1]/div/div/a','作者')

