from common.functions import built_in_functions,mdes_buile_in_functions
from page_locators.client_detail_locator import ClientDetailLocator
import allure
import time
from testcase.mdes_base_case import MdesBaseCase


class ClientInputInsuredPagearea(MdesBaseCase):
    @allure.step("输入被保人信息")
    def input_insured_info(self, kwargs):
        self.switch_frame_to_main()
        self.select_frame('frame_content')
        self.select_frame(0)
        self.select_frame('WorkFrame')
        if kwargs.get('appnt_relation') != '本人':
            # 被保人信息-联系地址
            time.sleep(1)
            self.input_text(ClientDetailLocator.insur_link_adr, kwargs.get('insur_link_adr'), clear=False)
            if kwargs.get('insur_link_adr') == '其他':
                #邮编地址
                time.sleep(1)
                self.input_text(ClientDetailLocator.insur_home_zipcode , kwargs.get('insur_home_zipcode'))
                # 地址-省/直辖市
                self.select_option_native(ClientDetailLocator.insur_home_province, kwargs.get('insur_home_province'))
                for i in range(3):
                    # 地址-市
                    if self.find_element(ClientDetailLocator.insur_home_city):
                        self.select_option_native(ClientDetailLocator.insur_home_city, kwargs.get('insur_home_city'))
                        break
                    else:
                        time.sleep(0.5)
                # 地址-县/区
                self.select_option_native(ClientDetailLocator.insur_home_county , kwargs.get('insur_home_county'))
                # 地址-路
                self.input_text(ClientDetailLocator.insur_home_road, kwargs.get('insur_home_road'))
                # 地址-镇
                self.input_text(ClientDetailLocator.insur_home_village, kwargs.get('insur_home_village'))
        self.input_text(ClientDetailLocator.insur_name, kwargs.get('insur_name'), clear=False)
        self.select_option_native(ClientDetailLocator.insur_nationality, kwargs.get('insur_nationality'))
        if kwargs.get('insur_ID_type') == '身份证':
            self.select_option_native(ClientDetailLocator.insur_id_type, kwargs.get('insur_ID_type'))
            if kwargs.get('insur_ID') != '':
                self.input_text(ClientDetailLocator.insur_id, kwargs.get('insur_ID'))
            else:
                self.input_text(ClientDetailLocator.insur_id, built_in_functions.gen_id_card())
        else:
            self.select_option_native(ClientDetailLocator.insur_sex, kwargs.get('insur_sex'))
            self.input_text(ClientDetailLocator.insur_birthday, kwargs.get('insur_birthday'))
            # self.input_text(ClientDetailLocator.insur_age, kwargs.get('insur_age'))
            self.click_element(ClientDetailLocator.insur_age)  #被保人年龄是自动生成
            self.select_option_native(ClientDetailLocator.insur_id_type, kwargs.get('insur_ID_type'))
            if kwargs.get('insur_ID') != '':
                self.input_text(ClientDetailLocator.insur_id, kwargs.get('insur_ID'))
            else:
                self.input_text(ClientDetailLocator.insur_id, mdes_buile_in_functions.random_id_extend())
        self.select_option_native(ClientDetailLocator.insur_id_validity_type,
                                        kwargs.get('insur_ID_validity_type'))
        if kwargs.get('insur_ID_validity_type') == '非终身有效':
            self.input_text(ClientDetailLocator.insur_id_validity, kwargs.get('insur_ID_validity'))
        self.select_option_native(ClientDetailLocator.insur_id_view, kwargs.get('insur_ID_view'))
        self.input_text(ClientDetailLocator.insur_company, kwargs.get('insur_company'))
        self.input_text(ClientDetailLocator.insur_occupation_code, kwargs.get('insur_occupation_code'))
        self.select_option_native(ClientDetailLocator.insur_province, kwargs.get('insur_province'))
        for i in range(3):
            if self.find_element(ClientDetailLocator.insur_city):
                self.select_option_native(ClientDetailLocator.insur_city, kwargs.get('insur_city'))
                break
            else:
                time.sleep(0.5)
        self.select_option_native(ClientDetailLocator.insur_county, kwargs.get('insur_county'))
        self.input_text(ClientDetailLocator.insur_road, kwargs.get('insur_road'))
        self.input_text(ClientDetailLocator.insur_address, kwargs.get('insur_address'))
        self.select_option_native(ClientDetailLocator.insur_phone_area, kwargs.get('insur_phone_area'))
        self.input_text(ClientDetailLocator.insur_phone, kwargs.get('insur_phone'))
        self.input_text(ClientDetailLocator.insur_zip, kwargs.get('insur_zip'))
        self.input_text(ClientDetailLocator.insur_mobile, kwargs.get('insur_mobile'))
        self.input_text(ClientDetailLocator.insur_year_salary, kwargs.get('insur_year_salary'))
        self.input_text(ClientDetailLocator.insur_mail, kwargs.get('insur_mail'))

