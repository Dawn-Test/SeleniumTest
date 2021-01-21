import allure

from common.functions import built_in_functions
from page_locators.policy_input_locator import PolicyPageLocator
from page_locators.menu_locator import MenuLocator
from page_locators.client_detail_locator import ClientDetailLocator
import re
import time
from testcase.mdes_base_case import MdesBaseCase


class PolicyInputPage(MdesBaseCase):
    data_dict = {}

    @allure.step('输入投保书号')
    def cont_no_input(self, kwargs):
        cont_no = built_in_functions.get_time(fmt='%Y%m%d%H%M')
        self.data_dict.update({'proposal_cont_no': cont_no})  #将生成的投保书号，先更新到字典中
        self.switch_frame_to_main()
        self.select_frame('frame_content')
        self.select_frame(0)
        self.select_frame('MainInfoFrame')
        time.sleep(2)
        for i in range(3):
            if self.find_element(PolicyPageLocator.proposal_cont_no):
                self.input_text(PolicyPageLocator.proposal_cont_no, cont_no)
                break
            else:
                time.sleep(0.5)
        self.select_option_native(PolicyPageLocator.sign_city, kwargs.get('sign_city'))
        self.click_element(PolicyPageLocator.proposal_Cont_save)
        time.sleep(0.5)
        self.popup_confirm()


    @allure.step("输入险种信息")
    def policy_input(self, kwargs):
        """ 投保事项：传统
        默认为传统 """
        self.switch_frame_to_main()
        self.select_frame('frame_content')
        self.select_frame(0)
        self.select_frame('WorkFrame')
        self.click_element(PolicyPageLocator.search_button1)

        # 从列表字典中[{},{},...]中，找到risk_code_x的不为空的险种值生成一个列表
        risk_code = []
        for k, v in kwargs.items():
            if k is None:
                continue
            if "risk_code" in k:
                if v != None:
                    risk_code.append(v)

        for i in range(len(risk_code)):
            risk_code_locator = PolicyPageLocator.risk_code
            self.input_text((risk_code_locator[0], risk_code_locator[1].format(str(i)), risk_code_locator[2]),
                                kwargs.get('risk_code_' + str(i)))
            year_locator = PolicyPageLocator.year
            self.input_text((year_locator[0], year_locator[1].format(str(i)), year_locator[2]),
                                kwargs.get('year_' + str(i)))
            pay_year_locator = PolicyPageLocator.pay_year
            self.input_text((pay_year_locator[0], pay_year_locator[1].format(str(i)), pay_year_locator[2]),
                                kwargs.get('pay_year_' + str(i)))
            insured_or_premium = 'select_insured_or_premium_' + str(i)
            if kwargs[insured_or_premium] == '保额':
                # 保额（单选）
                insured_cost_locator = PolicyPageLocator.insured_cost
                self.click_element(
                    (insured_cost_locator[0], insured_cost_locator[1].format(str(i)), insured_cost_locator[2]))
            elif kwargs[insured_or_premium] == '保费':
                # 保费（单选）
                premium_locator = PolicyPageLocator.premium
                self.click_element(
                    (premium_locator[0], premium_locator[1].format(str(i)), premium_locator[2]))
            # 保额/保费（输入）
            premium_input_locator = PolicyPageLocator.premium_input
            self.input_text(
                (premium_input_locator[0], premium_input_locator[1].format(str(i)), premium_input_locator[2]),
                kwargs.get('premium_input_' + str(i)))
        # 保费交付频率
        self.select_option_native(PolicyPageLocator.pay_frequency, kwargs.get('pay_frequency'))
        # 溢交保险费转下期选择
        self.select_option_native(PolicyPageLocator.agent_get_flag, kwargs.get('agent_get_flag'))
        # 保险费逾期未付的选择
        self.select_option_native(PolicyPageLocator.live_get_mode, kwargs.get('live_get_mode'))
        # 红利给付方式
        if kwargs.get('bonus_get_mode') in ['现金', '累计生息', '增额红利', '购买交清增额保险']:
            self.select_option_native(PolicyPageLocator.bonus_get_mode, kwargs.get('bonus_get_mode'))
        # 年金/生存金领取方式
        if kwargs.get('dead_get_mode') in ['现金','累计生息','交清增额'] :
            self.select_option_native(PolicyPageLocator.dead_get_mode, kwargs.get('dead_get_mode'))
        # 年金领取频率
        if kwargs.get('stand_by_flag3') in ['年领','月领']:
            self.select_option_native(PolicyPageLocator.stand_by_flag3, kwargs.get('stand_by_flag3'))


    @allure.step('填入年金领取年龄')
    def get_year(self):
        """ DD11BA
         从被保人信息取得年龄后得到对应的年金领取年龄填入投保事项 """
        # 返回客户信息页面
        self.switch_frame_to_main()
        self.select_frame('frame_content')
        self.select_frame(0)
        self.select_frame('NavigationFrame')
        self.click_element(MenuLocator.tab_2)
        # 获得被保人年龄
        self.switch_frame_to_main()
        self.select_frame('frame_content')
        self.select_frame(0)
        self.select_frame('WorkFrame')
        self.wait_element(ClientDetailLocator.insur_age)
        age = self.get_element_attribute(ClientDetailLocator.insur_age, 'value')
        print(age)
        comp = re.compile('[^0-9]')
        year = comp.sub('', age)
        get_year = str(int(year) + 5)
        print(get_year)
        self.switch_frame_to_main()
        self.select_frame('frame_content')
        self.select_frame(0)
        self.select_frame('NavigationFrame')

        # 返回投保事项页面
        time.sleep(1)
        self.click_element(MenuLocator.tab_1)
        self.switch_frame_to_main()
        self.select_frame('frame_content')
        self.select_frame(0)
        self.select_frame('WorkFrame')
        for i in range(3):
            if self.find_element(PolicyPageLocator.get_year):
                self.input_text(PolicyPageLocator.get_year, get_year)
                break
            else:
                time.sleep(0.5)
