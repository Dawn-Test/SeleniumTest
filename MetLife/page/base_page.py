import base64
import os
import tempfile
import time
from collections import namedtuple
from typing import Union, Tuple

import allure
import numpy as np
from PIL import Image
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from loguru import logger
from common.by_util import By
from common.file_util import get_curr_time_str, gen_images_directory
# from common.logger import logger
from common.ui_exception import LocatorTypeNotSupport

FALSE_STRINGS = {'FALSE', 'NO', 'OFF', '0', 'NONE', ''}
ACCEPT = "ACCEPT"
DISMISS = "DISMISS"
LEAVE = "LEAVE"
_next_alert_action = ACCEPT


class BasePage(object):
    """
    page基类，所有的子页面都继承此基类
    """

    def __init__(self,  driver):
        self.driver = driver
        self.timeout = 15
        self.sleep = 0.5
        self._speed = driver.speed if 'speed' in vars(driver) else 0

    @property
    def speed(self):
        return self.driver.speed

    @speed.setter
    def speed(self, speed):
        """
        设置脚本的运行速度，speed 的单位是秒(s)
        """
        step_info = f'设置浏览器运行脚本的速度{speed}'
        with allure.step(step_info):
            self.driver.speed = speed
            logger.info(step_info)

    """
    ==================================================================
    元素操作
    ==================================================================
    """

    def is_string(self, item):
        """
        检查item是否为字符串
        """
        return isinstance(item, (str,))

    def is_truthy(self, item):
        if self.is_string(item):
            return item.upper() not in FALSE_STRINGS
        return bool(item)

    def _handle_locator(self, locator):
        by = value = comment = None
        if len(locator) == 2:
            by, value = locator
            comment = ''
        elif 3 == len(locator):
            by, value, comment = locator
        return by, value, comment

    def _find_element_with_jquery(self, jq_locator):
        js = f"return jQuery('{jq_locator}').get()"
        elements = self.driver.execute_script(js)
        if elements:
            return elements[0]
        raise NoSuchElementException(f"not fund {jq_locator} by jquery ,please check")

    def find_element(self, locator: tuple, parent: WebElement = None) -> WebElement:
        """
        查找元素
        """
        if self._speed > 0:
            time.sleep(self._speed)
        by, value, comment = self._handle_locator(locator)
        if by in [By.JQUERY_SELECTOR]:
            element = self._find_element_with_jquery(value)
            return element
        if parent:
            return WebDriverWait(self.driver, timeout=self.timeout, poll_frequency=self.sleep).until(
                parent.find_element(by, value))
        return WebDriverWait(self.driver, timeout=self.timeout, poll_frequency=self.sleep).until(
            ec.presence_of_element_located((by, value)))


    def click_element(self, locator: tuple, modifier: str = None, action_chain: bool = False, by_js: bool = False):
        """
        点击元素
        """
        step_info = f"点击元素 {locator[2]} : [ 使用 {locator[0]}={locator[1]} 查找 ]"
        with allure.step(step_info):
            if by_js:
                # 通过js执行点击操作
                self.driver.execute_script('arguments[0].click();', self.find_element(locator))
            else:
                if self.is_truthy(modifier):
                    self._click_with_modifier(locator, modifier)
                elif self.is_truthy(action_chain):
                    self._click_with_action_chain(locator)
                else:
                    self.find_element(locator).click()
            logger.info(step_info)

    def _click_with_action_chain(self, locator):
        """
        使用ActionChains 点击元素
        """
        action = ActionChains(self.driver)
        element = self.find_element(locator)
        action.move_to_element(element)
        action.click()
        action.perform()

    def _parse_aliases(self, key):
        if key == "CTRL":
            return "CONTROL"
        if key == "ESC":
            return "ESCAPE"
        return key

    def parse_modifier(self, modifier):
        modifier = modifier.upper()
        modifiers = modifier.split("+")
        keys = []
        for item in modifiers:
            item = item.strip()
            item = self._parse_aliases(item)
            if hasattr(Keys, item):
                keys.append(getattr(Keys, item))
            else:
                raise ValueError(f"'{item}' modifier does not match to Selenium Keys")
        return keys

    def _click_with_modifier(self, locator, modifier):
        """
        点击元素，并可以带快捷键
        """
        modifier = self.parse_modifier(modifier)
        action = ActionChains(self.driver)
        for item in modifier:
            action.key_down(item)
        element = self.find_element(locator)
        action.click(element)
        for item in modifier:
            action.key_up(item)
        action.perform()

    def input_text(self, locator: tuple, text: str, clear: bool = True, by_js: bool = False):
        """
        文本输入
        """
        step_info = f"向元素 {locator[2]} 中输入 {text}: [ 使用 {locator[0]}={locator[1]} 查找 ]"
        with allure.step(step_info):
            element = self.find_element(locator)
            if self.is_truthy(clear):
                element.clear()
            if by_js:
                self.driver.execute_script(f'arguments[0].value="{text}"', element)
            else:
                element.send_keys(text)
        logger.info(step_info)

    def get_element_size(self, locator: tuple) -> Tuple[int, int]:
        """
        返回元素的大小
        """
        step_info = f"获取元素 {locator[2]} 的大小: [ 使用 {locator[0]}={locator[1]} 查找 ]"
        with allure.step(step_info):
            element = self.find_element(locator)
            logger.info(
                f"获取元素 {locator[2]} 的大小({element.size['width']},{element.size['height']}): [ 使用 {locator[0]}={locator[1]} 查找 ]")
        return element.size["width"], element.size["height"]

    def get_element_attribute(self, locator: tuple, attribute: str) -> str:
        """
        查找元素并返回指定的属性
        """
        return self.find_element(locator).get_attribute(attribute)

    def get_element_value(self, locator: tuple):
        """
        查找元素，并返指定元素的value
        """

        step_info = f"获取元素 {locator[2]} 的value: [ 使用 {locator[0]}={locator[1]} 查找 ]"
        with allure.step(step_info):
            value = self.get_element_attribute(locator, "value")
        logger.info(f"获取元素 {locator[2]} 的value {value}: [ 使用 {locator[0]}={locator[1]} 查找 ]")
        return value

    def get_text(self, locator: tuple) -> str:
        """
        返回元素的文本
        """
        step_info = f"获取元素 {locator[2]} 的文本 : [ 使用 {locator[0]}={locator[1]} 查找 ]"
        with allure.step(step_info):
            text = self.find_element(locator).text
        logger.info(f"获取元素 {locator[2]} 的文本 {text}: [ 使用 {locator[0]}={locator[1]} 查找 ]")
        return text

    def clear_element_text(self, locator: tuple):
        """
        清空元素的值
        """
        step_info = f"清空元素 {locator[2]} 的值 : [ 使用 {locator[0]}={locator[1]} 查找 ]"
        with allure.step(step_info):
            self.find_element(locator).clear()
        logger.info(step_info)

    def get_vertical_position(self, locator: tuple) -> int:
        """
        返回元素的y坐标
        """
        return self.find_element(locator).location["y"]

    def double_click_element(self, locator: tuple):
        """
        查找并双击元素
        """
        step_info = f"双击元素 {locator[2]} : [ 使用 {locator[0]}={locator[1]} 查找 ]"
        with allure.step(step_info):
            element = self.find_element(locator)
            action = ActionChains(self.driver)
            action.double_click(element).perform()
        logger.info(step_info)

    def set_focus_to_element(self, locator: tuple):
        """
        设置元素为获取焦点
        """
        step_info = f"模拟元素 {locator[2]} 获取到焦点 : [ 使用 {locator[0]}={locator[1]} 查找 ]"
        with allure.step(step_info):
            element = self.find_element(locator)
            self.driver.execute_script("arguments[0].focus();", element)
        logger.info(step_info)

    def scroll_element_into_view(self, locator: tuple):
        """
        滚动页面到元素可见
        """
        step_info = f"滚动页面，直到元素 {locator[2]} 可见 : [ 使用 {locator[0]}={locator[1]} 查找 ]"
        with allure.step(step_info):
            element = self.find_element(locator)
            try:
                ActionChains(self.driver).move_to_element(element).perform()
            except AttributeError:
                element = element.wrapped_element
                ActionChains(self.driver).move_to_element(element).perform()
        logger.info(step_info)

    def drag_and_drop(self, locator: tuple, target: tuple):
        """
        将元素拖拽到目标元素
        """
        step_info = f"拖拽元素 {locator[2]} 到 元素 {target[2]} 的位置 : [ 使用 {locator[0]}={locator[1]} 和 {target[0]}={target[1]} 查找 ]"
        with allure.step(step_info):
            element = self.find_element(locator)
            target = self.find_element(target)
            action = ActionChains(self.driver)
            action.drag_and_drop(element, target).perform()
        logger.info(step_info)

    def drag_and_drop_by_offset(self, locator: tuple, x_offset: int, y_offset: int):
        """
        拖拽元素以偏移量移动
        """
        step_info = f"拖拽元素 {locator[2]} 根据偏移量x={x_offset},y={y_offset}移动 : [ 使用 {locator[0]}={locator[1]} 查找 ]"
        with allure.step(step_info):
            element = self.find_element(locator)
            action = ActionChains(self.driver)
            action.drag_and_drop_by_offset(element, x_offset, y_offset)
            action.perform()
        logger.info(step_info)

    def mouse_out(self, locator: tuple):
        """
        模拟将鼠标移出元素
        """
        step_info = f"模拟鼠标移出元素 {locator[2]}  : [ 使用 {locator[0]}={locator[1]} 查找 ]"
        with allure.step(step_info):
            element = self.find_element(locator)
            size = element.size
            offset_x = (size["width"] / 2) + 1
            offset_y = (size["height"] / 2) + 1
            action = ActionChains(self.driver)
            try:
                action.move_to_element(element)
            except AttributeError:
                element = element.wrapped_element
                action.move_to_element(element)
            action.move_by_offset(offset_x, offset_y)
            action.perform()
        logger.info(step_info)

    def mouse_over(self, locator: tuple):
        """
        模拟将鼠标悬停在元素上
        """
        step_info = f"模拟鼠标悬停在元素 {locator[2]}  : [ 使用 {locator[0]}={locator[1]} 查找 ]"
        with allure.step(step_info):
            element = self.find_element(locator)
            action = ActionChains(self.driver)
            try:
                action.move_to_element(element).perform()
            except AttributeError:
                element = element.wrapped_element
                action.move_to_element(element).perform()
        logger.info(step_info)

    def open_context_menu(self, locator: tuple):
        """
        在元素上右键
        """
        step_info = f"模拟鼠标在元素 {locator[2]} 右键 : [ 使用 {locator[0]}={locator[1]} 查找 ]"
        with allure.step(step_info):
            element = self.find_element(locator)
            action = ActionChains(self.driver)
            action.context_click(element).perform()
        logger.info(step_info)

    def _parse_keys(self, *keys):
        if not keys:
            raise AssertionError('"keys" argument can not be empty.')
        list_keys = []
        for key in keys:
            separate_keys = self._separate_key(key)
            separate_keys = self._convert_special_keys(separate_keys)
            list_keys.append(separate_keys)
        return list_keys

    def _separate_key(self, key):
        one_key = ""
        list_keys = []
        for char in key:
            if char == "+" and one_key != "":
                list_keys.append(one_key)
                one_key = ""
            else:
                one_key += char
        if one_key:
            list_keys.append(one_key)
        return list_keys

    def _convert_special_keys(self, keys):
        KeysRecord = namedtuple("KeysRecord", "converted, original special")
        converted_keys = []
        for key in keys:
            key = self._parse_aliases(key)
            if self._selenium_keys_has_attr(key):
                converted_keys.append(KeysRecord(getattr(Keys, key), key, True))
            else:
                converted_keys.append(KeysRecord(key, key, False))
        return converted_keys

    def _selenium_keys_has_attr(self, key):
        return hasattr(Keys, key)

    def _press_keys_special_keys(self, actions, element, parsed_key, key):
        if len(parsed_key) == 1 and element:
            logger.info(f"Pressing special key {key.original} to element.")
            actions.send_keys(key.converted)
        elif len(parsed_key) == 1 and not element:
            logger.info(f"Pressing special key {key.original} to browser.")
            actions.send_keys(key.converted)
        else:
            logger.info(f"Pressing special key {key.original} down.")
            actions.key_down(key.converted)

    def plural_or_not(item):
        count = item if isinstance(item, int) else len(item)
        return '' if count == 1 else 's'

    def _press_keys_normal_keys(self, actions, key):
        # logger.info(f"Sending key{self.plural_or_not(key.converted)} {key.converted}")
        actions.send_keys(key.converted)

    def _special_key_up(self, actions, parsed_key):
        for key in parsed_key:
            if key.special:
                logger.info(f"Releasing special key {key.original}.")
                actions.key_up(key.converted)

    def press_keys(self, locator, *keys):
        """
        在某个元素或者激活的浏览器上按键
        """
        parsed_keys = self._parse_keys(*keys)

        ac = ActionChains(self.driver)
        if locator:
            element = self.find_element(locator)
            ac.click(element).perform()
        else:
            element = None
        # 解析按键
        for parsed_key in parsed_keys:
            actions = ActionChains(self.driver)
            for key in parsed_key:
                if key.special:
                    self._press_keys_special_keys(actions, element, parsed_key, key)
                else:
                    self._press_keys_normal_keys(actions, key)
            self._special_key_up(actions, parsed_key)
            actions.perform()

    """
    ==================================================================
    浏览器操作
    ==================================================================
    """

    def open_url(self, url: str):
        """
        浏览器打开url
        """
        step_info = f"浏览器打开链接{url}"
        with allure.step(step_info):
            self.driver.get(url)
        logger.info(step_info)

    def get_source(self) -> str:
        """返回当前页面或frame的源码"""
        pg = ''
        step_info = f"获取当前页面的源码{pg}"
        with allure.step(step_info):
            pg = self.driver.page_source
        logger.info(step_info)
        return pg

    def get_title(self) -> str:
        """返回当前页面的title"""
        title = self.driver.title
        step_info = f"获取当前页面的标题 {title} "
        logger.info(step_info)
        with allure.step(step_info):
            return title

    def get_location(self) -> str:
        """返回当前浏览器窗口的URL"""
        cur_url = self.driver.current_url
        step_info = f"获取当前页面的url {cur_url} "
        logger.info(step_info)
        with allure.step(step_info):
            return cur_url

    def close_browser(self):
        if self.driver:
            self.driver.close()

    def go_back(self):
        """模拟浏览器返回"""
        logger.info("模拟浏览器返回")
        with allure.step("模拟浏览器返回"):
            self.driver.back()

    def set_implicit_wait(self, value: float):
        """
        设置隐式等待
        """
        step_info = f"设置浏览器执行脚本的隐式等待时间为 {value}"
        with allure.step(step_info):
            self.driver.implicitly_wait(value)
        logger.info(step_info)

    def select_radio_button(self, locator: tuple, value):
        """
        选择单选按钮
        """
        if locator[1] == By.GROUP_NAME_SELECTOR:
            group_name = locator[1]
        else:
            raise LocatorTypeNotSupport(f'选择单选按钮时，该定位方式{locator[0]}不支持')
        step_info = f"根据值{value}选择单选按钮{group_name}"
        with allure.step(step_info):
            xpath = (
                f"//input[@type='radio' and @name='{group_name}' and "
                f"(@value='{value}' or @id='{value}')]"
            )
            locator = (By.XPATH, xpath, '')
            element = self.find_element(locator)
            if not element.is_selected():
                element.click()
        logger.info(step_info)

    """
    ==================================================================
    js操作
    ==================================================================
    """

    def execute_async_javascript(self, js: str):
        """
        异步执行js
        """
        step_info = f"异步执行js脚本"
        with allure.step(step_info):
            rs = self.driver.execute_async_script(js)
            logger.info(f"异步执行js脚本\n{js}")
            return rs

    def execute_javascript(self, js: str):
        """
        执行js
        """
        step_info = f"执行js脚本"
        with allure.step(step_info):
            rs = self.driver.execute_script(js)
            logger.info(f"执行js脚本\n{js}")
            return rs

    """
    ==================================================================
    截图
    ==================================================================
    """

    def capture_page_screen(self, file_name: str = None, description=None):
        """
        截图
        """
        if description is None:
            description = '截图'
        images_directory = gen_images_directory()
        curr_time = get_curr_time_str()
        if file_name:
            file_name = os.path.join(images_directory, file_name)
        else:
            file_name = os.path.join(images_directory, f'{curr_time}.png')
        rs = self.driver.get_screenshot_as_base64()
        with open(file_name, mode='wb') as f:
            f.write(base64.b64decode(rs))
        allure.attach.file(file_name, attachment_type=allure.attachment_type.PNG, name=description)
        logger.info(f'成功截图，图片路径 {file_name}')
        return file_name

    def capture_full_page_screen(self, file_name: str = None, description: str = None):
        """
        整个页面截屏
        """
        images_directory = gen_images_directory()
        curr_time = get_curr_time_str()
        if file_name:
            file_name = os.path.join(images_directory, file_name)
        else:
            file_name = os.path.join(images_directory, f'{curr_time}.png')
        window_height = self.driver.get_window_size()['height']

        page_height = self.driver.execute_script('return document.documentElement.scrollHeight')  # 页面高度
        self.driver.save_screenshot(file_name)
        os_temp_dir = tempfile.gettempdir()

        if page_height > window_height:
            n = page_height // window_height  # 需要滚动的次数
            base_mat = np.atleast_2d(Image.open(file_name))  # 打开截图并转为二维矩阵

            for i in range(n):
                self.driver.execute_script(f'document.documentElement.scrollTop={window_height * (i + 1)};')
                time.sleep(.5)
                png_path = os.path.join(os_temp_dir, f'temp_{i}.png')
                self.driver.save_screenshot(png_path)  # 保存截图
                mat = np.atleast_2d(Image.open(png_path))  # 打开截图并转为二维矩阵
                base_mat = np.append(base_mat, mat, axis=0)  # 拼接图片的二维矩阵
            Image.fromarray(base_mat).save(file_name)

    """
    ==================================================================
    框架操作
    ==================================================================
    """

    def select_frame(self, locator: (str, int, tuple)):
        """
        选择指定的frame或者元素
        """
        step_info = ""
        if isinstance(locator, (str, int)):
            step_info = f"进入框架{locator}"
            with allure.step(step_info):
                self.driver.switch_to.frame(locator)
        else:
            step_info = f"进入框架{locator[2]} : 使用 {locator[0]}={locator[1]} 查找"
            with allure.step(step_info):
                element = self.find_element(locator)
                self.driver.switch_to.frame(element)
        logger.info(step_info)

    def unselect_frame(self):
        """
        取消先前的选择的frame
        """
        step_info = "取消先前的选择的frame"
        with allure.step(step_info):
            self.driver.switch_to.default_content()
        logger.info(step_info)

    """
    ==================================================================
    下拉框操作
    ==================================================================
    """

    def select_from_list_by_index(self, locator: tuple, *indexes: str):
        """
        下拉框根据索引选择
        """
        step_info = f" 选择下拉框 {locator[2]} 中下标索引 {indexes}的选项: 使用 {locator[0]}={locator[1]} 查找"
        with allure.step(step_info):
            select = self._get_select_list(locator)
            for index in indexes:
                select.select_by_index(int(index))
        logger.info(step_info)

    def select_from_list_by_value(self, locator: tuple, *values: str):
        """
        下拉框根据值选择
        """
        step_info = f" 选择下拉框 {locator[2]} 中值 {values}的选项: 使用 {locator[0]}={locator[1]} 查找"
        with allure.step(step_info):
            select = self._get_select_list(locator)
            for value in values:
                select.select_by_value(value)
        logger.info(step_info)

    def select_from_list_by_label(self, locator: tuple, *labels: str):
        """
        下拉框根据文本选择
        """
        step_info = f" 选择下拉框 {locator[2]} 中文本 {labels}的选项: 使用 {locator[0]}={locator[1]} 查找"
        with allure.step(step_info):
            select = self._get_select_list(locator)
            for label in labels:
                select.select_by_value(label)
        logger.info(step_info)

    def _get_select_list(self, locator: tuple):
        """
        获取select
        """
        element = self.find_element(locator)
        select = Select(element)
        return select

    def all_selected_options(self, locator: tuple):
        """
        返回下拉框中所有已选择的选项的文本值
        """
        select = self._get_select_list(locator)
        selected_options_txt = [option.text for option in select.all_selected_options]
        step_info = f" 下拉框 {locator[2]} 中选择中选项文本的值{','.join(selected_options_txt)}的选项: 使用 {locator[0]}={locator[1]} 查找"
        with allure.step(step_info):
            return selected_options_txt

    """
    ==================================================================
    弹框操作
    ==================================================================
    """

    def handle_alert(self, action: str = ACCEPT, timeout: Union[float, str, None] = None):
        """
        处理alert
        """
        step_info = f"对弹出框执行{action}操作"
        with allure.step(step_info):
            alert = self._wait_alert(timeout)
            rs = self._handle_alert(alert, action)
        logger.info(f"弹框文本：{rs}" + step_info)
        return rs

    def _handle_alert(self, alert, action):
        action = action.upper()
        text = " ".join(alert.text.splitlines())
        if action == ACCEPT:
            alert.accept()
        elif action == DISMISS:
            alert.dismiss()
        elif action != LEAVE:
            raise ValueError(f"Invalid alert action '{action}'.")
        return text

    def _wait_alert(self, timeout=None):
        if timeout is None:
            timeout = self.timeout
        wait = WebDriverWait(self.driver, timeout)
        try:
            return wait.until(ec.alert_is_present())
        except TimeoutException:
            raise AssertionError(f"Alert not found in {timeout}.")
        except WebDriverException as err:
            raise AssertionError(f"An exception occurred waiting for alert: {err}")

    """
    ==================================================================
    等待操作
    ==================================================================
    """
    # TODO 添加等待的几种方法

    """
    ==================================================================
    window操作
    ==================================================================
    """

    def switch_window(self, title):
        """
        根据title切换到指定的window
        """
        switch_flag = False
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if self.driver.title == title:
                switch_flag = True
                break
        if not switch_flag:
            raise Exception("未切换到目标window")
