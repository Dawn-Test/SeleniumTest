from page_locators.client_detail_locator import ClientDetailLocator
import allure
from testcase.mdes_base_case import MdesBaseCase
import time

class ClientSelectRelationPagearea(MdesBaseCase):

    @allure.step("选择投被保人关系")
    def select_relation(self, kwargs):
        self.switch_frame_to_main()
        self.select_frame('frame_content')
        self.select_frame(0)
        self.select_frame('WorkFrame')
        time.sleep(3)
        print(ClientDetailLocator.appnt_relation)
        print(kwargs)
        print(kwargs.get('appnt_relation'))
        self.select_option_native(ClientDetailLocator.appnt_relation, kwargs.get('appnt_relation'))
        self.select_option_native(ClientDetailLocator.appnt_vip, kwargs.get('appnt_VIP'))
