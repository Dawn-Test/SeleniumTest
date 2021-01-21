from selenium.webdriver.common.by import By

class SearchLocator:
    # 点击保单录入
    # Policy_entry_title = (By.XPATH, '//div[@id="headMenu1"]/a')

    # 投保书审核/查询
    # search_cont_no = (By.XPATH, '//div[@id="secondaryNav1"]/ul/li[2]/a', '投保书审核/查询')
    search_cont_no = 'mdes/banklns/banklnsFrame.jsf?type=2'

    # 输入投保书编号
    cont_no_input = (By.XPATH, '//input[@id="formQuery:contno"]','输入投保书编号')
    # 查询
    cont_no_searchBTN = (By.XPATH, '//input[@id="formQuery:searchButton"]', '查询')
    # 查询得到的投保单号
    cont_no = (By.XPATH, '//a[@id="formQuery:dataList:0:viewBtn"]', '查询得到的投保单号')
    # 保单号
    policy_number = (By.XPATH, '//input[@id="formInsu:mainPolNo"]', '保单号')
    # 投保书号
    proposal_cont_no = (By.XPATH, '//input[@id="formInsu:proposalContNo"]', '投保书号')
    # 保单状态
    policy_status = (By.XPATH, '//input[@id="formInsu:lnpstate"]', '保单状态')

    #读取险种信息中的每个单元格的内容
    # td_locator = (By.XPATH, '//tbody[@id="formInsu:dataList:tb"]//tr//td', '读取险种信息中的每个单元格的内容')

    #读取险种信息表中的每行数据
    tr_locator = (By.XPATH, '//tbody[@id="formInsu:dataList:tb"]//tr', '读取险种信息表中的每行数据')
    print(tr_locator)

    # 合计首期保费
    first_premium = (By.XPATH, '//span[@id="formInsu:sum"]', '合计首期保费')

