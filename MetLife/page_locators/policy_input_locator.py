from selenium.webdriver.common.by import By


class PolicyPageLocator:
    # 投保书号
    proposal_cont_no = (By.XPATH, '//input[@id="formInsu:proposalContNo"]','投保书号')
    # 签署地/出单地
    sign_city = (By.XPATH, '//select[@id="formInsu:insuSignCityFirst"]', '签署地/出单地')
    # 投保书保存
    proposal_Cont_save = (By.XPATH, '//input[@id="formInsu:button1"]', '投保书保存')
    """ 投保事项 """
    # 传统
    traditional = (By.XPATH, '//input[@id="formInsu:it:0"]','传统')
    # VUL/VA
    vul_la = (By.XPATH, '//input[@id="formInsu:it:1"]','VUL/VA')
    # 组合
    combine = (By.XPATH, '//input[@id="formInsu:it:2"]','组合')
    # 年金转换
    annuity_change = (By.XPATH, '//input[@id="formInsu:it:3"]','年金转换')

    # 险种信息：
    #险种的,  增加按钮的定位元素1
    search_button1 = (By.XPATH, '//input[@id="formInsu:searchButton1"]', '险种的,增加按钮的定位元素1')
    # 险种的,  增加按钮的定位元素2
    search_button2 = (By.XPATH, '//input[@id="formInsu:searchButton2"]', '险种的,增加按钮的定位元素2')
    # 险种代码和附加险代码
    risk_code = (By.XPATH, '//input[@id="formInsu:riskcode{}"]',"险种代码和附加险代码")
    # 保障期
    year = (By.XPATH, '//input[@id="formInsu:years{}"]',"保障期")
    # 缴费期
    pay_year =(By.XPATH, '//input[@id="formInsu:Payyears{}"]',"缴费期")
    # 保额（单选）
    insured_cost = (By.XPATH, '//input[@id="formInsu:type{0}:0"]',"保额（单选）" )
    # 保费（单选）
    premium = (By.XPATH, '//input[@id="formInsu:type{0}:1"]',"保费（单选）")
    # 保额/保费（输入）
    premium_input = (By.XPATH, '//input[@id="formInsu:money{0}"]',"保额/保费（输入）")
    # 年金领取年龄
    get_year = (By.XPATH, '//input[@id="formInsu:getyear"]','年金领取年龄')

    # 其他事项：
    # 保费交付频率
    pay_frequency = (By.XPATH, '//select[@id="formInsu:payintv"]','保费交付频率')
    # 溢交保险费转下期选择
    agent_get_flag = (By.XPATH, '//select[@id="formInsu:agentgetflag"]','溢交保险费转下期选择')
    # 保险费逾期未付的选择
    live_get_mode = (By.XPATH, '//select[@id="formInsu:livegetmode"]','保险费逾期未付的选择')
    # 红利给付方式
    bonus_get_mode = (By.XPATH, '//select[@id="formInsu:bonusgetmode"]','红利给付方式')
    # 年金/生存金领取方式
    dead_get_mode = (By.XPATH, '//select[@id="formInsu:deadgetmode"]','年金/生存金领取方式')
    # 年金领取频率
    stand_by_flag3 = (By.XPATH, '//select[@id="formInsu:StandbyFlag3"]','年金领取频率')

