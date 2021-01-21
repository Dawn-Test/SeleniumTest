import os
import time
import pytest
from page.login_page import Login
from selenium import webdriver
from page.policy_input_page import PolicyInputPage
from page.menu_page import MenuPage
from page.authorization_page import AuthorizationPage
from page.search_policy_page import SearchPage
import allure
from testcase.mdes_base_case import MdesBaseCase
from page.client_select_relation_pagearea import ClientSelectRelationPagearea
from page.client_input_appnt_pagearea import ClientInputAppntPagearea
from page.client_input_insured_pagearea import ClientInputInsuredPagearea
from page.client_input_benefit_pagearea import ClientInputBenefitPagearea


@pytest.fixture(scope='session')
def record_result():
    # """ 将投保人五要素 & 险种信息写入excel """
    result_list = []
    yield result_list
    MdesBaseCase.write_dictinlist_into_sheet(result_list)

@allure.story('登陆测试')
class TestMdesRecordPolicy():
    mdes_base_case = MdesBaseCase(webdriver)
    @pytest.mark.parametrize("data", mdes_base_case.load_data("datas\\read_mdes.xlsx"))
    @pytest.mark.parametrize('create_driver', ['ie'], indirect=True)
    @allure.testcase('mdes录单')
    # def testest_logint_login(self, create_driver, record_result):
    def test_mdes_record_policy(self, create_driver, data, record_result):

        data_dict = {}
        login = Login(create_driver)
        login.login()
        time.sleep(2)
        menu = MenuPage(create_driver)

        # 投保事项--险种信息
        policy = PolicyInputPage(create_driver)
        policy.cont_no_input(data)
        policy.policy_input(data)
        data_dict.update(policy.data_dict)  #将policy_input_page.py文件中的字典更新到这个字典中
        print('#' * 40)
        print(data_dict)
        record_result.append(data_dict)  #再将这个字典中的内容追加到列表中
        print(record_result)

        #客户信息页
        menu.click_client_info()
        # 客户信息--投被保险人关系
        client_selectrelation_pagearea = ClientSelectRelationPagearea(create_driver)
        time.sleep(1)
        client_selectrelation_pagearea.select_relation(data)
        # 客户信息--投保人信息
        client_inputappnt_pagearea = ClientInputAppntPagearea(create_driver)
        client_inputappnt_pagearea.input_appnt_info(data)
        # 客户信息--被保人信息
        client_inputinsured_pagearea = ClientInputInsuredPagearea(create_driver)
        if data.get('appnt_relation') != '本人':
            client_inputinsured_pagearea.input_insured_info(data)
        # 客户信息--身故受益人信息
        client_inputbenefit_pagearea = ClientInputBenefitPagearea(create_driver)
        client_inputbenefit_pagearea.input_benefit_info(data)
        data_dict.update(client_inputappnt_pagearea.data_dict)
        record_result = []
        record_result.append(data_dict)


        #告知及授权
        menu.click_authorization()   # 点击告知及授权
        authorization = AuthorizationPage(create_driver)
        time.sleep(2)
        authorization.authorization_input(data)
        authorization.agent_input(data)

        # 三个标签页再点击一次做为保存
        menu.click_policy_tab()
        time.sleep(1)
        policy.get_year()  # 投保事项 填入年金领取年龄
        menu.click_authorization()  # 点击告知及授权
        menu.click_policy_tab()  # 点击投保事项标签

        # 点击“提交审核”
        menu.submit_policy()

        #查询并将信息写入excel
        search_policy = SearchPage(create_driver)
        data_dict.update(search_policy.search_policy_number())
        record_result = []
        record_result.append(data_dict)
        print(record_result)


if __name__ == "__main__":
    pytest.main(['-s', 'test_mds.py', '--alluredir', '../allure-report'])
    os.system('allure generate ../allure-report/ -o ../report/ --clean')

# D:\Auto_mds_dev\MIDDLELAYER-GSSP-AUTOTEST\testcase
# pytest test_mds.py --alluredir ..\allure-report\
# $ allure generate ..\allure-report\ -o ..\report\ --clean
