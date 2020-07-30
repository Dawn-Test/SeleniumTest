from selenium import webdriver
from scripts.shizhan import page
class GetDriver:
    driver = None

    # 获取driver
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            # 获取driver
            cls.driver = webdriver.Chrome(r'd:\webdrivers\chromedriver.exe')
            # 最大化浏览器
            cls.driver.maximize_window()
            # 打开url
            cls.driver.get(page.URL)
        # 返回driver
        return cls.driver

    # 关闭driver
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            # 必须 置空操作
            cls.driver = None

if __name__ == '__main__':
    GetDriver().quit_driver()