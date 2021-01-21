from page_locators.authorization_locator import AuthorizationLocator
import allure
from testcase.mdes_base_case import MdesBaseCase
from common.functions import mdes_buile_in_functions

# 告知及授权
class AuthorizationPage(MdesBaseCase):

    @allure.step('填写基本告知')
    def authorization_input(self, kwargs):
        self.switch_frame_to_main()
        self.select_frame('frame_content')
        self.select_frame(0)
        self.select_frame('WorkFrame')
        self.click_element(AuthorizationLocator.insur_allno)
        self.input_text(AuthorizationLocator.insur_height, kwargs.get('insur_height'))  # 被保险人身高
        self.input_text(AuthorizationLocator.insur_weight, kwargs.get('insur_weight'))  # 被保险人体重
        self.click_element(AuthorizationLocator.appnt_allno)
        self.input_text(AuthorizationLocator.appnt_height, kwargs.get('appnt_height'))  # 投保人身高
        self.input_text(AuthorizationLocator.appnt_weight, kwargs.get('appnt_weight'))  # 投保人体重

    @allure.step('代理人告知')
    def agent_input(self, kwargs):
        bank_id = mdes_buile_in_functions.random_bank_id()
        self.switch_frame_to_main()
        self.select_frame('frame_content')
        self.select_frame(0)
        self.select_frame('WorkFrame')
        self.select_option_native(AuthorizationLocator.first_pay_method, kwargs.get('first_pay_method'))  # 首期保险费交付方法
        self.select_option_native(AuthorizationLocator.renew_pay_method, kwargs.get('renew_pay_method'))  # 续期保险费交付方法
        self.select_option_native(AuthorizationLocator.auth_bank, kwargs.get('auth_bank'))  # 授权银行名称
        self.input_text(AuthorizationLocator.auth_account, bank_id)  # 授权账户号码
        self.input_text(AuthorizationLocator.sign_date, kwargs.get('sign_date'))  # 投保书签署日
        # self.input_text(AuthorizationLocator.sign_date, self.load_data())
        self.input_text(AuthorizationLocator.target_date, kwargs.get('target_date'))  # 卡钟日
        # self.input_text(AuthorizationLocator.target_date, self.load_data())
        self.input_text(AuthorizationLocator.agent_branch_code, kwargs.get('agent_branch_code'))  # 代理网点代码HQ000100AA0007\HQ000900AA0001
        self.input_text(AuthorizationLocator.agent_code, kwargs.get('agent_code'))  # 销售人员代码1000051902
        self.select_option_native(AuthorizationLocator.send_type,kwargs.get('send_type'))  # 递送方式


