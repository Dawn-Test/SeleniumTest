from selenium.webdriver.common.by import By


class AuthorizationLocator:
    insur_allno = (By.XPATH, '//input[@id="formOper:insurSelcAll:1"]','被保险人')
    insur_height = (By.XPATH, '//input[@id="formOper:insur0101050005"]','被保险人身高cm')
    insur_weight = (By.XPATH, '//input[@id="formOper:insur0101060006"]','被保险人体重kg')
    appnt_allno = (By.XPATH, '//input[@id="formOper:appntSelcAll:1"]','投保人')
    appnt_height = (By.XPATH, '//input[@id="formOper:appnt0101050005"]','投保人身高cm')
    appnt_weight = (By.XPATH, '//input[@id="formOper:appnt0101060006"]','投保人体重kg')
    first_pay_method = (By.XPATH, '//select[@id="formOper:FirPayType"]','首期保险费交付方法')
    renew_pay_method = (By.XPATH, '//select[@id="formOper:EscPayType"]','续期保险费交付方法')
    auth_bank = (By.XPATH, '//select[@id="formOper:AuthBank"]','授权银行名称')
    auth_account = (By.XPATH, '//input[@id="formOper:AuthACount"]','授权账户号码')
    sign_date = (By.XPATH, '//input[@id="formOper:SignDate"]','投保书签署日')
    target_date = (By.XPATH, '//input[@id="formOper:TargetDate"]','卡钟日')
    agent_branch_code = (By.XPATH, '//input[@id="formOper:AgentBranchattr"]','代理网点代码HQ000100AA0007')
    agent_code = (By.XPATH, '//input[@id="formOper:AgentCode"]','# 销售人员代码1000051902')
    send_type = (By.XPATH, '//select[@id="formOper:AgentTrantype"]','递送方式')
