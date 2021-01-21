import allure
from page_locators.menu_locator import MenuLocator
from page_locators.search_policy_locator import SearchLocator
import time
from testcase.mdes_base_case import MdesBaseCase

class MenuPage(MdesBaseCase):

    @allure.step('点击投保事项')
    def click_policy_tab(self):
        time.sleep(1)
        self.switch_frame_to_main()
        self.select_frame('frame_content')
        self.select_frame(0)
        self.select_frame('NavigationFrame')
        self.wait_element(MenuLocator.tab_1)
        self.click_element(MenuLocator.tab_1)

    @allure.step('点击客户信息')
    def click_client_info(self):
        time.sleep(1)
        self.switch_frame_to_main()
        self.select_frame('frame_content')
        self.select_frame(0)
        self.select_frame('NavigationFrame')
        self.click_element(MenuLocator.tab_2)

    @allure.step('点击告知及授权')
    def click_authorization(self):
        time.sleep(1)
        self.switch_frame_to_main()
        self.select_frame('frame_content')
        self.select_frame(0)
        self.select_frame('NavigationFrame')
        self.click_element(MenuLocator.tab_3)

    @allure.step('点击核心系统反馈')
    def click_system_core(self):
        self.switch_frame_to_main()
        self.select_frame('frame_content')
        self.select_frame(0)
        self.select_frame('NavigationFrame')
        self.click_element(MenuLocator.tab_4)

    @allure.step('提交审核')
    def submit_policy(self):
        self.wait_element(MenuLocator.review_btn)
        self.switch_frame_to_main()
        self.select_frame('frame_content')
        self.select_frame(0)
        self.select_frame('MainOperFrame')
        # self.wait_element(MenuLocator.review_btn)
        time.sleep(1)
        self.click_element(MenuLocator.review_btn,  by_js=True)
        # self.wait_element(MenuLocator.calculateBTN)
        time.sleep(1)
        self.click_element(MenuLocator.calculateBTN, by_js=True)
        self.switch_frame_to_main()
        self.wait_until_element_not_visible(MenuLocator.load_panel)
        self.switch_frame_to_main()
        self.select_frame('frame_content')
        self.select_frame(0)
        self.select_frame('MainOperFrame')
        self.click_element(MenuLocator.send_btn)
        self.switch_frame_to_main()
        self.wait_until_element_not_visible(MenuLocator.load_panel)
        self.select_frame('frame_content')
        self.select_frame(0)
        self.select_frame('MainInfoFrame')
        policy_status = self.get_element_attribute(SearchLocator.policy_status, 'value')
        print("获取到的状态："+policy_status)
        if policy_status == '已审核-发送成功':
            pass
        else:
            print('保单发送失败...')
            raise
