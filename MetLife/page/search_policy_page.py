import allure
from page_locators.search_policy_locator import SearchLocator
import time
from page_locators.menu_locator import MenuLocator
from page_locators.client_detail_locator import ClientDetailLocator
from testcase.mdes_base_case import MdesBaseCase
from config import config
from selenium import webdriver

# 投保书审核/查询
class SearchPage(MdesBaseCase):
    temp_dict1 = {}

    @allure.step('查询已提交的投保书号并获取保单五要素')
    def search_policy_number(self):

        self.switch_frame_to_main()
        self.select_frame('frame_content')
        self.select_frame(0)
        self.select_frame('MainInfoFrame')
        # cont_no = '202010291707'
        cont_no = self.get_element_attribute(SearchLocator.proposal_cont_no, 'value')  # 获取已提交的投保书号
        print(cont_no)
        self.switch_frame_to_main()
        print('开始点击投保书号查询，进入查询页面')
        # self.click_element(SearchLocator.search_cont_no)   # 点击进入投保书号查询页面，方法一：通过定位元素,不稳定
        # self.click_element_by_js(SearchLocator.search_cont_no)  # 点击进入投保书号查询页面，方法二：通过js定位，不稳定
        self.driver.get(config.get_config("MDES", "ip") + SearchLocator.search_cont_no)  # 点击进入投保书号查询页面，方法三：通过直接跳转链接
        self.switch_frame_to_main()
        self.select_frame('frame_content')
        # self.wait_element(SearchLocator.proposal_cont_no)   --------------------------------
        self.input_text(SearchLocator.cont_no_input, cont_no)  # 填入投保书号
        print('开始点击查询')
        self.click_element(SearchLocator.cont_no_searchBTN)
        time.sleep(3)
        try:
            self.click_element(SearchLocator.cont_no)  # 点击投保书号进入保单详情页面
        except Exception as e:
            print('没有找到投保书号...')
            raise
        time.sleep(3)

        """ 采集留存信息 """
        # temp_list = []  # 新建列表保存留存信息
        temp_risk_list = []

        self.switch_frame_to_main()
        self.select_frame('frame_content')
        self.select_frame(0)
        self.select_frame('MainInfoFrame')
        # proposal_cont_no = self.get_element_attribute(SearchLocator.proposal_cont_no, 'value')  # 投保书号
        self.switch_frame_to_main()
        self.select_frame('frame_content')
        self.select_frame(0)
        self.select_frame('WorkFrame')

        """ 读取险种信息 """
        tr_elements = self.get_elements(SearchLocator.tr_locator)
        for tr_element in tr_elements:
            temp_risk_list.append(tr_element.text)

        """ 将险种信息组合成字典"""

        temp_dict = {}

        # list2 = []
        # for i in range(len(temp_risk_list)):
        #     list2 = temp_risk_list[i].split()
        #     for j in range(len(list2)):
        #         temp_dict[risk_keys_list[j] + "_" + str(i)] = list2[j]
        #         print(risk_keys_list[j] + "_" + str(i))
        # print(temp_dict)

        risk_keys_list = ['risk_code', 'risk_name', 'year', 'pay_year', 'get_year', 'select_insured_or_premium',
                          'pay_frequency', 'each_premium']
        temp_dict = {(risk_keys_list[j] + "_" + str(i)): temp_risk_list[i].split()[j] for i in range(len(temp_risk_list)) for j in
                     range(len(temp_risk_list[i].split()))}

        first_premium = self.get_element_text(SearchLocator.first_premium)  # 合计首期保费
        temp_dict['first_premium'] = first_premium
        self.switch_frame_to_main()
        self.select_frame('frame_content')
        self.select_frame(0)
        self.select_frame('NavigationFrame')
        self.click_element(MenuLocator.tab_2)  # 客户信息页
        self.switch_frame_to_main()
        self.select_frame('frame_content')
        self.select_frame(0)
        self.select_frame('MainInfoFrame')
        time.sleep(1)
        policy_number = self.get_element_attribute(SearchLocator.policy_number, 'value')  # 保单号
        self.switch_frame_to_main()
        self.select_frame('frame_content')
        self.select_frame(0)
        self.select_frame('WorkFrame')
        # appnt_name = self.get_element_attribute(ClientDetailLocator.appnt_name, 'value')  # 投保人姓名
        # appnt_sex = self.get_element_attribute(ClientDetailLocator.appnt_sex, 'value')  # 投保人性别
        # appnt_nationality = self.get_element_attribute(ClientDetailLocator.appnt_nationality, 'value')  # 投保人国籍
        # appnt_birthday = self.get_element_attribute(ClientDetailLocator.appnt_birthday, 'value')  # 投保人生日
        # appnt_ID_type = self.get_element_attribute(ClientDetailLocator.appnt_id_type, 'value')  # 投保人证件类型
        # appnt_ID = self.get_element_attribute(ClientDetailLocator.appnt_id, 'value')  # 投保人证件号

        """将保单信息&五要素组合成字典"""
        # temp_dict['proposal_cont_no'] = proposal_cont_no
        temp_dict['policy_number'] = policy_number
        # temp_dict['appnt_name'] = appnt_name
        # temp_dict['appnt_sex'] = appnt_sex
        # temp_dict['appnt_nationality'] = appnt_nationality
        # temp_dict['appnt_birthday'] = appnt_birthday
        # temp_dict['appnt_ID_type'] = appnt_ID_type
        # temp_dict['appnt_ID'] = appnt_ID

        return temp_dict

if __name__ == "__main__":
    sp = SearchPage(webdriver.Ie())
    print(config.get_config('MDES', 'ip') + SearchLocator.search_cont_no)

