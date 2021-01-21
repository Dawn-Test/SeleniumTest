from selenium.webdriver.common.by import By


class MenuLocator:
    """ 菜单在 NavigationFrame 下 """
    # 投保事项
    tab_1 = (By.XPATH, '//div[@id="tabs1"]/ul/li[@name="1"]', '投保事项')
    # 客户信息
    tab_2 = (By.XPATH, '//div[@id="tabs1"]/ul/li[@name="2"]', '客户信息')
    # 告知及授权
    tab_3 = (By.XPATH, '//div[@id="tabs1"]/ul/li[@name="3"]', '告知及授权')
    # 核心系统反馈
    tab_4 = (By.XPATH, '//div[@id="tabs1"]/ul/li[@name="4"]', '核心系统反馈')

    """ MainOperFrame 提交审核 """
    # 提交审核btn
    review_btn = (By.XPATH, '//input[@id="formOper:review"]', '提交审核btn')
    # 保费计算btn
    calculateBTN = (By.XPATH, '//input[@id="formOper:caclulate"]', '保费计算btn')
    # 发送保单btn
    send_btn = (By.XPATH, '//input[@id="formOper:submit"]', '发送保单btn')

    # 保费计算后返回的数据
    return_data = (By.XPATH, '//tbody[@id="formInsu:dataList:tb"]/tr/td','保费计算后返回的数据')

    # 加载等待图标
    load_panel = (By.ID, 'panelForm:loadPanelCDiv', "加载中图标")
