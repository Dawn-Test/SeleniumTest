from common.functions import built_in_functions,mdes_buile_in_functions
from page_locators.client_detail_locator import ClientDetailLocator
import allure
from testcase.mdes_base_case import MdesBaseCase


class ClientInputBenefitPagearea(MdesBaseCase):
    @allure.step("输入身故受益人信息")
    def input_benefit_info(self, kwargs):
        self.switch_frame_to_main()
        self.select_frame('frame_content')
        self.select_frame(0)
        self.select_frame('WorkFrame')
        self.select_option_native(ClientDetailLocator.bnf_is_exist, kwargs.get('bnf_isExist'))

        # 1.判断kwargs中的 bnf_name对应的值不为空,且一共有多少的个数
        bnf_num = []
        for k, v in kwargs.items():
            if k is None:
                continue
            if "bnf_name" in k:
                if v != None:
                    bnf_num.append(v)
        add_bnf_button = int(len(bnf_num))

        # 2.然后用这个数-下标3, 减下来的数,就是点击几次  增加受益人按钮
        if add_bnf_button > 4:
            for i in range(add_bnf_button-4):
                print("点击'新增按钮'")
            self.click_element(ClientDetailLocator.bnf_add_new)

        if kwargs.get('bnf_isExist') == '指定':
            # 1.先判断出Excel表中有多少个身故受益人
            bnf_num = []
            for k, v in kwargs.items():
                if k is None:
                    continue
                if "bnf_name" in k:
                    if v != None:
                        bnf_num.append(v)
            # 2. 循环身故益人进行添加
            bnf_num_len = len(bnf_num)
            for i in range(bnf_num_len):
                bnf_name_locator = ClientDetailLocator.bnf_name  # 身故受益人姓名
                self.input_text((bnf_name_locator[0], bnf_name_locator[1].format(str(i)), bnf_name_locator[2]),
                                    kwargs.get('bnf_name_' + str(i)))
                bnf_relation_location = ClientDetailLocator.bnf_relation  # 与被保人关系
                self.select_option_native(
                    (bnf_relation_location[0], bnf_relation_location[1].format(str(i)), bnf_relation_location[2]),
                    kwargs.get('bnf_relation_' + str(i)))
                bnf_order_location = ClientDetailLocator.bnf_order  # 受益顺序
                self.input_text(
                    (bnf_order_location[0], bnf_order_location[1].format(str(i)), bnf_order_location[2]),
                    kwargs.get('bnf_order_' + str(i)))
                bnf_rate_location = ClientDetailLocator.bnf_rate  # 受益比例
                self.input_text_value(
                    (bnf_rate_location[0], bnf_rate_location[1].format(str(i)), bnf_rate_location[2]),
                    kwargs.get('bnf_rate_' + str(i)))
                bnf_add_btn_location = ClientDetailLocator.bnf_add_btn  # 受益人增加信息  向下的箭头
                self.click_element(
                    (bnf_add_btn_location[0], bnf_add_btn_location[1].format(str(i)), bnf_add_btn_location[2]))
                bnf_nationality_location = ClientDetailLocator.bnf_nationality  # 受益人国籍
                self.select_option_native((bnf_nationality_location[0], bnf_nationality_location[1].format(str(i)),
                                              bnf_nationality_location[2]), kwargs.get('bnf_nationality_' + str(i)))
                bnf_birthday_location = ClientDetailLocator.bnf_birthday  # 受益人出生日期
                self.input_text(
                    (bnf_birthday_location[0], bnf_birthday_location[1].format(str(i)), bnf_birthday_location[2]),
                    kwargs.get('bnf_birthday_' + str(i)))
                bnf_sex_loaction = ClientDetailLocator.bnf_sex  # 受益人性别
                self.select_option_native(
                    (bnf_sex_loaction[0], bnf_sex_loaction[1].format(str(i)), bnf_sex_loaction[2]),
                    kwargs.get('bnf_sex_' + str(i)))
                bnf_ID_type_location = ClientDetailLocator.bnf_id_type  # 受益人证件类型
                bnf_ID_location = ClientDetailLocator.bnf_id  # 受益人证件号码
                if kwargs.get('bnf_ID_type_' + str(i)) == '身份证':
                    self.select_option_native(
                        (bnf_ID_type_location[0], bnf_ID_type_location[1].format(str(i)), bnf_ID_type_location[2]),
                        kwargs.get('bnf_ID_type_' + str(i)))
                    if kwargs.get('bnf_ID_' + str(i)) != '':
                        self.input_text((bnf_ID_location[0], bnf_ID_location[1].format(str(i)), bnf_ID_location[2]),
                                            kwargs.get('bnf_ID_' + str(i)))
                    else:
                        self.input_text_value(
                            (bnf_ID_location[0], bnf_ID_location[1].format(str(i)), bnf_ID_location[2]),
                            built_in_functions.gen_id_card())
                else:
                    self.select_option_native(
                        (bnf_ID_type_location[0], bnf_ID_type_location[1].format(str(i)), bnf_ID_type_location[2]),
                        kwargs.get('bnf_ID_type_' + str(i)))

                    if kwargs.get('bnf_ID_' + str(i)) != '':
                        self.input_text((bnf_ID_location[0], bnf_ID_location[1].format(str(i)), bnf_ID_location[2]),
                                            kwargs.get('bnf_ID_' + str(i)))
                    else:
                        self.input_text((bnf_ID_location[0], bnf_ID_location[1].format(str(i)), bnf_ID_location[2]),
                                            mdes_buile_in_functions.random_id_extend())
                bnf_id_validity_type_location = ClientDetailLocator.bnf_id_validity_type        #受益人证件有效期类型
                self.select_option_native((bnf_id_validity_type_location[0],
                                              bnf_id_validity_type_location[1].format(str(i)),
                                              bnf_id_validity_type_location[2]),
                                             kwargs.get('bnf_ID_validity_type_' + str(i)))
                bnf_id_validity_location = ClientDetailLocator.bnf_id_validity
                print(bnf_id_validity_location)
                # if kwargs.get('bnf_ID_validity_type_0') == '非终身有效':
                #     self.input_text(ClientDetailLocator.insur_id_validity, kwargs.get('bnf_ID_validity_' + str(i)))
                if kwargs.get('bnf_ID_validity_type_' + str(i)) == '非终身有效':
                    self.input_text((bnf_id_validity_location[0], bnf_id_validity_location[1].format(str(i)), bnf_id_validity_location[2]),
                                    kwargs.get('bnf_ID_validity_' + str(i)))

