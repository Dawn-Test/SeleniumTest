# 导包
from selenium import webdriver
from time import sleep
# 获取浏览器对象
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(r'd:\webdrivers\chromedriver.exe')
# 最大化浏览器
driver.maximize_window()
# 隐式等待
driver.implicitly_wait(30)

url = r"lujing"
driver.get("url")
"""
目标：
     1.定位  上海a
     2.暂停2秒
     3.定位   广州a
步骤：
     1.导包select类
     2.获取select对象
        匿名：select(element).select_by_index() # 通过下标
        实名：select = select（element）
             调用：select.select_by_index()
注意：
     1.select类只能通过select.select_by_index()
"""
# 使用css定位操作上海
# sleep(2)
# driver.find_element_by_css_selector("[value = 'sh']").click()
# 使用css定位操作广州
# sleep(2)
# driver.find_element_by_css_selector("[value = 'gz']").click()

# 方式二：使用select完成需求
"""   通过下标形式访问   """
el = driver.find_element_by_css_selector("#selectA")
# 暂停2秒
sleep(2)
Select(el).select_by_index(1)
sleep(2)
Select(el).select_by_index(2)

"""   通过value形式访问   """
# 获取select引用对象
sel = Select(el)
sel.select_by_value("sh")
sleep(2)
sel.select_by_value("gz")
sleep(2)

"""   通过 显示文本切换  """
sleep(2)
# 切换上海
Select(el).select_by_visible_text("a上海")

sleep(2)
# 切换广州
Select(el).select_by_visible_text("广州")
# 关闭浏览器
driver.quit()