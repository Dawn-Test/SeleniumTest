import time
from selenium.webdriver.support.wait import WebDriverWait

from scripts.shizhan import page
from scripts.shizhan.base.get_logger import GteLogger
# 获取log日志器

log = GteLogger().get_logger()

class Base:
    def __init__(self, driver):
        log.info("正在获取初始化driver对象：{}".format(driver))
        self.driver = driver

    # 查找元素 封装
    def base_find(self, loc, timeout=30, poll=0.5):
        log.info("正在定位:{} 元素，默认超时时间为:{}".format(loc,time))
         # 使用显示等待
        return WebDriverWait(self.driver,
                             timeout=timeout,
                              poll_frequency=poll).until(lambda x:x.find_element(*loc))
    # 点击元素方法 封装
    def base_click(self, loc):
        log.info("正在对：{}元素实行点击事件".format(loc))
        self.base_find(loc).click()
    # 输入元素方法 封装
    def base_input(self, loc, value):
        # 获取元素
        log.info("正在对：{}进行清空操作".format(loc))
        el = self.base_find(loc)
        # 清空
        el.clear()
        # 输入
        el.send_keys(value)
    # 获取文本信息方法  封装
    def base_get_text(self, loc):
        log.info("正在获取：{}元素文本值".format(loc))
        return self.base_find(loc).text
    # 截图方法  封装
    def base_get_image(self):
        log.info("断言出错，调用截图")
        self.driver.get_screenshot_as_flie("../shizhan/image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))
    # 判断元素是否存在 方法封装
    def base_element_is_exist(self, loc):
        try:
            self.base_find(loc, timeout=2)
            log.info("{}元素查找成功，存在页面".format(loc))
            return True # 代表元素存在
        except:
            log.info("{}元素查找失败，不存在页面".format(loc))
            return False # 代表元素不存在

    # 回到首页（购物车、下订单、支付）都需用到
    def base_index(self):
        self.driver.get(page.URL)
    # 切换frame表单方法
    def base_switch_frame(self,name):
        self.driver.switch_to.frame(name)

    # 回到默认目录方法
    def base_default_content(self):
         self.driver.switch_to.default_content()


    # 切换窗口方法
    def base_swich_to_window(self, title):
        self.base_get_title_handle(title)
    # 获取指定title页面的handle方法
    def base_get_title_handle(self,title):
        # 获取当前页面的所有handles
        for handle in self.driver.window_handles:
            # 切换 handle
            self.driver.switch_to.window(handle)
            # 获取当前页面title 并判断 是否等于 指定参数title
            if self.driver.title == title:
                # 返回 handle
                return handle