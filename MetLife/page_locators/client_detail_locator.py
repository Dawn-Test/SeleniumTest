from selenium.webdriver.common.by import By


class ClientDetailLocator:
    # 投被保人关系
    appnt_relation = (By.XPATH, '//select[@id="formOper:appntRealation"]', '投被保人关系')
    # 大客户
    appnt_vip = (By.XPATH, '//select[@id="formOper:appntVIP"]', '大客户')
    """ 投保人信息 """
    # 投保人姓名
    appnt_name = (By.XPATH, '//input[@id="formOper:AppntName"]', '投保人姓名')
    # 投保人性别
    appnt_sex = (By.XPATH, '//select[@id="formOper:appntSex"]', '投保人性别')
    # 国籍
    appnt_nationality = (By.XPATH, '//select[@id="formOper:appntNative"]', '国籍')
    # 出生日期
    appnt_birthday = (By.XPATH, '//input[@id="formOper:appntBirthDay"]', '出生日期')
    # 投保人年龄
    appnt_age = (By.XPATH, '//input[@id="formOper:appntAge"]', '投保人年龄')
    # 证件类型
    appnt_id_type = (By.XPATH, '//select[@id="formOper:appntIDType"]', '证件类型')
    # 证件号码
    appnt_id = (By.XPATH, '//input[@id="formOper:appntID"]', '证件号码')
    # 证件有效期类型
    appnt_id_validity_type = (By.XPATH, '//select[@id="formOper:appntIDVailityType"]', '证件有效期类型')
    # 证件有效期
    appnt_id_validity = (By.XPATH, '//input[@id="formOper:appntIDVaility"]', '证件有效期')
    # 证件已交附件
    appnt_id_view = (By.XPATH, '//select[@id="formOper:appntIDView"]', '证件已交附件')
    # 工作单位
    appnt_company = (By.XPATH, '//input[@id="formOper:appntGrpName"]', '工作单位')
    # 职业代码
    appnt_occupation_code = (By.XPATH, '//input[@id="formOper:appntoccCode"]', '职业代码')
    # 职业名称
    appnt_occupation_name = (By.XPATH, '//input[@id="formOper:appntoccName"]', '职业名称')
    """ 地址 """
    # 省/直辖市
    appnt_province = (By.XPATH, '//select[@id="formOper:appntCompanyProvince"]', '省')
    # 市
    appnt_city = (By.XPATH, '//select[@id="formOper:appntCompanyCity"]', '市')
    # 县/区
    appnt_county = (By.XPATH, '//select[@id="formOper:appntCompanyCounty"]', '县')
    # 镇/路
    appnt_road = (By.XPATH, '//input[@id="formOper:appntCompanyRoad"]', '镇')
    # 详细地址
    appnt_address = (By.XPATH, '//input[@id="formOper:appntCompanyVillage"]', '详细地址')
    """"""
    # 电话区号
    appnt_phone_area = (By.XPATH, '//select[@id="formOper:appntAreaCode"]', '电话区号')
    # 电话
    appnt_phone = (By.XPATH, '//input[@id="formOper:appntCompanyPhone"]', '电话')
    # 邮编
    appnt_zip = (By.XPATH, '//input[@id="formOper:appntCompanyZipCode"]', '邮编')
    # 手机
    appnt_mobile = (By.XPATH, '//input[@id="formOper:appntIPhone"]', '手机')
    # 年收入
    appnt_year_salary = (By.XPATH, '//input[@id="formOper:appntSalary"]', '年收入')
    # 电邮
    appnt_mail = (By.XPATH, '//textarea[@id="formOper:appntCompanyMail"]', '电邮')
    # 联系地址
    appnt_contact_address = (By.XPATH, '//select[@id="formOper:appntLinkAdr"]', '联系地址')
    # 地址-邮编地址
    appnt_home_zipcode = (By.XPATH, '//input[@id="formOper:appntHomeZipCode"]', '地址')
    # 地址-省/直辖市
    appnt_home_province = (By.XPATH, '//select[@id="formOper:appntHomeProvince"]', '地址')
    # 地址-市
    appnt_home_city = (By.XPATH, '//select[@id="formOper:appntHomeCity"]', '地址')
    # 地址-县/区
    appnt_home_county = (By.XPATH, '//select[@id="formOper:appntHomeCounty"]', '地址')
    # 地址-路
    appnt_home_road = (By.XPATH, '//input[@id="formOper:appntHomeRoad"]', '地址')
    # 地址-镇
    appnt_home_village = (By.XPATH, '//input[@id="formOper:appntHomeVillage"]', '地址')

    """ 税收居民身份声明 """
    # 姓名
    tax_name = (By.XPATH, '//input[@id="formOper:AppntName1"]', '姓名')
    # 声明类别
    tax_type_0 = (By.XPATH, '//input[@id="formOper:taxResidentType:0"]', '仅为中国税收居民')    # 1.仅为中国税收居民
    tax_type_1 = (By.XPATH, '//input[@id="formOper:taxResidentType:1"]', '仅为非居民')    # 2.仅为非居民
    tax_type_2 = (By.XPATH, '//input[@id="formOper:taxResidentType:2"]', '既是中国税收居民又是其他国家（地区）税收居民')    # 3.既是中国税收居民又是其他国家（地区）税收居民

    # 仅为非居民和既是中国税收居民又是其他国家（地区）税收居民
    # 姓(英文或拼音):
    appnt_first_name =(By.XPATH, '//input[@id="formOper:AppntFisrtName"]', '姓')
    # 名(英文或拼音)：
    appnt_last_name = (By.XPATH, '//input[@id="formOper:AppntLastName"]', '名')
    # 现居住地(英文或拼音)地址：
    appnt_addre = (By.XPATH, '//input[@id="formOper:addrE"]', '现居住地')
    # 出生地(中文)国家
    appnt_birth_country = (By.XPATH, '//select[@id="formOper:Birthcountry"]', '出生地')
    # 出生地(中文)省/直辖市
    appnt_birth_province = (By.XPATH, '//select[@id="formOper:Birthprovince"]', '出生地')
    # 出生地(中文)市
    appnt_birth_city = (By.XPATH, '//select[@id="formOper:Birthcity"]', '出生地')
    # 出生地(英文或拼单)地址
    appnt_birth_adde= (By.XPATH, '//input[@id="formOper:BirthaddrE"]', '出生地')
    # 税收居民国（地区）
    appnt_ssjmg1 = (By.XPATH, '//select[@id="formOper:SSJMG1"]', '税收居民国')
    # 纳税人识别号
    appnt_nsrsbh1 = (By.XPATH, '//input[@id="formOper:NSRSBH1"]', '纳税人识别号')
    # 居民国（地区）不发放纳税人识别号
    appnt_no_taxpayercode_reason = (By.XPATH, '//input[@id="formOper:noTaxpayercodeReason:0"]', '居民国')
    # 具体原因：
    appnt_reason_description = (By.XPATH, '//input[@id="formOper:reasonDescription"]', '具体原因')


    """ 被保人信息 """
    # 被保人姓名
    insur_name = (By.XPATH, '//input[@id="formOper:insurName"]', '被保人姓名')
    # 被保人性别
    insur_sex = (By.XPATH, '//select[@id="formOper:insurSex"]', '被保人性别')
    # 国籍
    insur_nationality = (By.XPATH, '//select[@id="formOper:insurNative"]', '国籍')
    # 出生日期
    insur_birthday = (By.XPATH, '//input[@id="formOper:insurBirthDay"]', '出生日期')
    # 被保人年龄
    insur_age = (By.XPATH, '//input[@id="formOper:insurAge"]', '被保人年龄')
    # 证件类型
    insur_id_type = (By.XPATH, '//select[@id="formOper:insurIDType"]', '证件类型')
    # 证件号码
    insur_id = (By.XPATH, '//input[@id="formOper:insurID"]', '证件号码')
    # 证件有效期类id型
    insur_id_validity_type = (By.XPATH, '//select[@id="formOper:insurIDVailityType"]', '证件有效期类id型')
    # 证件有效期
    insur_id_validity = (By.XPATH, '//input[@id="formOper:insurIDVaility"]', '证件有效期')
    # 证件已交附件
    insur_id_view = (By.XPATH, '//select[@id="formOper:insurIDView"]', '证件已交附件')
    # 工作单位
    insur_company = (By.XPATH, '//input[@id="formOper:insurGrpName"]', '工作单位')
    # 职业代码
    insur_occupation_code = (By.XPATH, '//input[@id="formOper:insuroccCode"]', '职业代码')
    # 职业名称
    insur_occupation_name = (By.XPATH, '//input[@id="formOper:insuroccName"]', '职业名称')

    """ 地址 """
    # 省/直辖市
    insur_province = (By.XPATH, '//select[@id="formOper:insurCompanyProvince"]', '省')
    # 市
    insur_city = (By.XPATH, '//select[@id="formOper:insurCompanyCity"]', '市')
    # 县/区
    insur_county = (By.XPATH, '//select[@id="formOper:insurCompanyCounty"]', '县')
    # 镇/路
    insur_road = (By.XPATH, '//input[@id="formOper:insurCompanyRoad"]', '镇')
    # 详细地址
    insur_address = (By.XPATH, '//input[@id="formOper:insurCompanyVillage"]', '详细地址')
    """"""
    # 电话区号
    insur_phone_area = (By.XPATH, '//select[@id="formOper:insuAreaCode"]', '电话区号')
    # 电话
    insur_phone = (By.XPATH, '//input[@id="formOper:insurCompanyPhone"]', '电话')
    # 邮编
    insur_zip = (By.XPATH, '//input[@id="formOper:insurCompanyZipCode"]', '邮编')
    # 手机
    insur_mobile = (By.XPATH, '//input[@id="formOper:insurIPhone"]', '手机')
    # 年收入
    insur_year_salary = (By.XPATH, '//input[@id="formOper:insurSalary"]', '年收入')
    # 电邮
    insur_mail = (By.XPATH, '//textarea[@id="formOper:insurCompanyMail"]', '电邮')

    # 联系地址
    insur_link_adr  = (By.XPATH, '//select[@id="formOper:insurLinkAdr"]', '联系地址')
    # 邮编地址
    insur_home_zipcode = (By.XPATH, '//input[@id="formOper:insurHomeZipCode"]', '邮编地址')
    # 地址-省/直辖市
    insur_home_province = (By.XPATH, '//select[@id="formOper:insurHomeProvince"]', '地址')
    # 地址-市
    insur_home_city = (By.XPATH, '//select[@id="formOper:insurHomeCity"]', '地址')
    # 地址-县/区
    insur_home_county = (By.XPATH, '//select[@id="formOper:insurHomeCounty"]', '地址')
    # 地址-路
    insur_home_road = (By.XPATH, '//input[@id="formOper:insurHomeRoad"]', '地址')
    # 地址-镇
    insur_home_village = (By.XPATH, '//input[@id="formOper:insurHomeVillage"]', '地址')

    """ 身故受益人信息 """
    # 是否指定身故受益人
    bnf_is_exist = (By.XPATH, '//select[@id="formOper:bnfIsExist"]', '是否指定身故受益人')
    # 分期领取
    bnf_is_stage = (By.XPATH, '//select[@id="formOper:insuSex3_1"]', '分期领取')   #这个没有用到, '分期领取？
    # 身故受益人姓名
    bnf_name = (By.XPATH, '//input[@id="formOper:dataList:{}:bnfname"]', '身故受益人姓名')
    # 与被保人关系
    bnf_relation= (By.XPATH, '//select[@id="formOper:dataList:{}:bnfrela"]', '与被保人关系')
    # 受益顺序
    bnf_order = (By.XPATH, '//input[@id="formOper:dataList:{}:bnforder"]', '受益顺序')
    # 受益比例
    bnf_rate = (By.XPATH, '//input[@id="formOper:dataList:{}:bnfrate"]', '受益比例')
    # 受益人增加信息  向下的箭头
    bnf_add_btn = (By.XPATH, '//li[@id="formOper:dataList:{}"]/ul/li[./img[@id="add_li"]]/img', '受益人增加信息向下的箭头')
    # 受益人国, '受益人增加信息 籍
    bnf_nationality = (By.XPATH, '//select[@id="formOper:dataList:{}:bnfNative"]', '受益人国籍')
    # 受益人出生日期
    bnf_birthday = (By.XPATH, '//input[@id="formOper:dataList:{}:bnfBirthDay"]', '受益人出生日期')
    # 受益人性别
    bnf_sex = (By.XPATH, '//select[@id="formOper:dataList:{}:bnfSex"]', '受益人性别')
    # 受益人证件类型
    bnf_id_type = (By.XPATH, '//select[@id="formOper:dataList:{}:bnfidtype"]', '受益人证件类型')
    # 受益人证件号码
    bnf_id = (By.XPATH, '//input[@id="formOper:dataList:{}:bnfid"]', '受益人证件号码')
    # 受益人证件有效期类型
    bnf_id_validity_type = (By.XPATH, '//select[@id="formOper:dataList:{}:bnfidvalitype"]', '受益人证件有效期类型')
    # 受益人证件有效期
    bnf_id_validity = (By.XPATH, '//input[@id="formOper:dataList:{}:bnfidvali"]', '受益人证件有效期')
    # 增加受益人
    bnf_add_new = (By.XPATH, '//input[@id="formOper:addnew_btn"]', '增加受益人')
