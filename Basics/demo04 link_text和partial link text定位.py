"""
需求：
    1.使用link_text定位方式和partial link text定位方式，
      使用a.html页面，点击访问“新浪网站地址”
方法：
    1.driber.find_element_by_link_test("")  # 定位元素方法
    2.click（） # 点击方法
注意：
    link_text
    1.只能定位a标签
    2.link_text定位元素的内容必须全部匹配!!!
    3.partial link text 可以为模糊值，但是必须要有代表唯一性
"""
# 导包
from selenium import webdriver
from time import sleep

# 获取浏览器对象
driver = webdriver.Chrome(r'd:\webdrivers\chromedriver.exe')

# 打开URL
url = r'路径'
driver.ger(url)

# 使用link_text定位访问新浪网站  # click（） # 点击方法
driver.find_element_by_link_text('新浪网站地址').click()

# 暂停3秒
sleep(3)
# 关闭浏览器
driver.quit()


# 导包
from selenium import webdriver
from time import sleep

# 获取浏览器对象
driver = webdriver.Chrome(r'd:\webdrivers\chromedriver.exe')

# 打开URL
url = r'路径'
driver.ger(url)

# 使用partial link text定位访问新浪网站 使用模糊，但是要有唯一代表性
driver.find_element_by_partial_link_text('新浪')

# 暂停3秒
sleep(3)
# 关闭浏览器
driver.quit()