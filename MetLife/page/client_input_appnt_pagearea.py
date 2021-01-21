from common.functions import built_in_functions,mdes_buile_in_functions
from page_locators.client_detail_locator import ClientDetailLocator
import allure
from testcase.mdes_base_case import MdesBaseCase
import time


class ClientInputAppntPagearea(MdesBaseCase):
    data_dict = {}  #--------------
    @allure.step("输入投保人信息")
    def input_appnt_info(self, kwargs):
        self.switch_frame_to_main()
        self.select_frame('frame_content')
        self.select_frame(0)
        self.select_frame('WorkFrame')

        self.input_text(ClientDetailLocator.appnt_name, kwargs.get('appnt_name'))
        appnt_name = self.get_element_attribute(ClientDetailLocator.appnt_name, 'value')  # 投保人姓名
        self.data_dict['appnt_name'] = appnt_name

        self.select_option_native(ClientDetailLocator.appnt_nationality, kwargs.get('appnt_nationality'))
        appnt_nationality = self.get_element_attribute(ClientDetailLocator.appnt_nationality, 'value')  # 投保人国籍
        self.data_dict['appnt_nationality'] = appnt_nationality

        if kwargs.get('appnt_ID_type') == '身份证':
            self.select_option_native(ClientDetailLocator.appnt_id_type, kwargs.get('appnt_ID_type'))
            appnt_ID_type = self.get_element_attribute(ClientDetailLocator.appnt_id_type, 'value')  # 投保人证件类型
            self.data_dict['appnt_ID_type'] = appnt_ID_type

            if kwargs.get('appnt_ID') != '':
                self.input_text(ClientDetailLocator.appnt_id, kwargs.get('appnt_ID'))
                appnt_ID = self.get_element_attribute(ClientDetailLocator.appnt_id, 'value')  # 投保人证件号
                self.data_dict['appnt_ID'] = appnt_ID
            else:
                self.input_text(ClientDetailLocator.appnt_id, built_in_functions.gen_id_card())
        else:
            self.select_option_native(ClientDetailLocator.appnt_sex, kwargs.get('appnt_sex'))
            appnt_sex = self.get_element_attribute(ClientDetailLocator.appnt_sex, 'value')  # 投保人性别
            self.data_dict['appnt_sex'] = appnt_sex

            self.input_text(ClientDetailLocator.appnt_birthday, kwargs.get('appnt_birthday'))
            appnt_birthday = self.get_element_attribute(ClientDetailLocator.appnt_birthday, 'value')  # 投保人生日
            self.data_dict['appnt_birthday'] = appnt_birthday

            # self.input_text(ClientDetailLocator.appnt_age, kwargs.get('appnt_age'), clear=False)
            # self.input_text(ClientDetailLocator.appnt_age, kwargs.get('appnt_age'))
            self.click_element(ClientDetailLocator.appnt_age)  #投保人年龄是自动生成
            time.sleep(1)
            self.select_option_native(ClientDetailLocator.appnt_id_type, kwargs.get('appnt_ID_type'))
            appnt_ID_type = self.get_element_attribute(ClientDetailLocator.appnt_id_type, 'value')  # 投保人证件类型
            self.data_dict['appnt_ID_type'] = appnt_ID_type

            if kwargs.get('appnt_ID') == '':
                self.input_text(ClientDetailLocator.appnt_id, mdes_buile_in_functions.random_id_extend())
            else:
                self.input_text(ClientDetailLocator.appnt_id, kwargs.get('appnt_ID'))
                appnt_ID = self.get_element_attribute(ClientDetailLocator.appnt_id, 'value')  # 投保人证件号
                self.data_dict['appnt_ID'] = appnt_ID

        self.select_option_native(ClientDetailLocator.appnt_id_validity_type, kwargs.get('appnt_ID_validity_type'))
        if kwargs.get('appnt_ID_validity_type') == '非终身有效':
            self.input_text(ClientDetailLocator.appnt_id_validity, kwargs.get('appnt_ID_validity'))
        self.select_option_native(ClientDetailLocator.appnt_id_view, kwargs.get('appnt_ID_view'))
        self.input_text(ClientDetailLocator.appnt_company, kwargs.get('appnt_company'))
        self.input_text(ClientDetailLocator.appnt_occupation_code, kwargs.get('appnt_occupation_code'))
        self.select_option_native(ClientDetailLocator.appnt_province, kwargs.get('appnt_province'))
        for i in range(3):
            if self.find_element(ClientDetailLocator.appnt_city):
                time.sleep(2)
                self.select_option_native(ClientDetailLocator.appnt_city, kwargs.get('appnt_city'))
                break
            else:
                time.sleep(0.5)
        time.sleep(1)
        self.select_option_native(ClientDetailLocator.appnt_county, kwargs.get('appnt_county'))
        time.sleep(1)
        self.input_text(ClientDetailLocator.appnt_road, kwargs.get('appnt_road'))
        self.input_text(ClientDetailLocator.appnt_address, kwargs.get('appnt_address'))
        self.select_option_native(ClientDetailLocator.appnt_phone_area, kwargs.get('appnt_phone_area'))
        self.input_text(ClientDetailLocator.appnt_phone, kwargs.get('appnt_phone'))
        self.input_text(ClientDetailLocator.appnt_zip, kwargs.get('appnt_zip'))
        self.input_text(ClientDetailLocator.appnt_mobile, kwargs.get('appnt_mobile'))
        self.input_text(ClientDetailLocator.appnt_year_salary, kwargs.get('appnt_year_salary'))
        self.input_text(ClientDetailLocator.appnt_mail, kwargs.get('appnt_mail'))
        if kwargs.get('appnt_ID_type') == "身份证" or kwargs.get('appnt_ID_type') == "护照":
            if kwargs.get('tax_type') == '1':
                self.click_element(ClientDetailLocator.tax_type_0)
            else:
                if kwargs.get('tax_type') == '2':
                    self.click_element(ClientDetailLocator.tax_type_1)
                else:
                    self.click_element(ClientDetailLocator.tax_type_2)
                self.input_text(ClientDetailLocator.appnt_first_name, kwargs.get('appnt_FisrtName'))
                self.input_text(ClientDetailLocator.appnt_last_name, kwargs.get('appnt_LastName'))
                self.input_text(ClientDetailLocator.appnt_addre, kwargs.get('appnt_addrE'))
                self.select_option_native(ClientDetailLocator.appnt_birth_country, kwargs.get('appnt_birthcountry'))
                self.select_option_native(ClientDetailLocator.appnt_birth_province, kwargs.get('appnt_birthprovince'))
                self.select_option_native(ClientDetailLocator.appnt_birth_city, kwargs.get('appnt_birthcity'))
                self.input_text(ClientDetailLocator.appnt_birth_adde, kwargs.get('appnt_birth_addE'))
                self.select_option_native(ClientDetailLocator.appnt_ssjmg1, kwargs.get('appnt_SSJMG1'))
                self.input_text(ClientDetailLocator.appnt_nsrsbh1, kwargs.get('appnt_NSRSBH1'))
                # self.click_element(ClientDetailLocator.appnt_no_taxpayercode_reason)
                # self.input_text(ClientDetailLocator.appnt_reason_description, kwargs.get('appnt_reason_description'))
        if kwargs.get('appnt_relation') == '本人':
            # 投保人的联系地址--其他
            self.select_option_native(ClientDetailLocator.appnt_contact_address, kwargs.get('appnt_contact_address'))
            if kwargs.get('appnt_contact_address') == '其他':
                # 邮编地址
                self.input_text(ClientDetailLocator.appnt_home_zipcode, kwargs.get('appnt_home_zipcode'))
                # 地址-省/直辖市
                self.select_option_native(ClientDetailLocator.appnt_home_province, kwargs.get('appnt_home_province'))
                for i in range(2):
                    # 地址-市
                    self.select_option_native(ClientDetailLocator.appnt_home_city, kwargs.get('appnt_home_city'))
                    if self.find_element(ClientDetailLocator.appnt_home_city):
                        break
                    else:
                        time.sleep(0.5)
                # 地址-县/区
                time.sleep(1)
                self.select_option_native(ClientDetailLocator.appnt_home_county, kwargs.get('appnt_home_county'))
                # 地址-路
                self.input_text(ClientDetailLocator.appnt_home_road, kwargs.get('appnt_home_road'))
                # 地址-镇
                self.input_text(ClientDetailLocator.appnt_home_village, kwargs.get('appnt_home_village'))

