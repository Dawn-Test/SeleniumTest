#!/usr/bin/env python3
# coding=utf-8
import allure
from page.test_homer_base_page_example import TestHomerBasePage
from page_locators.index_page_locator_example import IndexPageLocator


class IndexPage(TestHomerBasePage):

    @allure.step("点击大会，并点击作者")
    def view_info(self,data):
        print(data)
        self.click_element(IndexPageLocator.head_title)
        self.click_element(IndexPageLocator.author)
        self.capture_page_screen(description="查看作者所有的文章")
