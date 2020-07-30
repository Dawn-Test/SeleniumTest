# 元素信息操作api
# 1）.ext                获取元素文本
# 2）.size               获取元素大小
# 3）.get_attribute()    获取元素属性值
# 4）.is_disoplayed()    判断元素是否可见
# 5）.is_endbled()       判断元素是否被选中
# 6）.is_slected()       判断元素是否可用


# 导包
from selenium import webdriver
from time import sleep

# 获取浏览器对象
driver = webdriver.Chrome(r'd:\webdrivers\chromedriver.exe')

# 打开url
crl = ""
driver.get(crl)
# 获取用户名文本框大小
size = driver.find_element_by_css_selector("#user").size
print("用户名大小为：",size)
# 获取页面上第一个超文本链接内容
text = driver.find_element_by_css_selector("a").text
print("页面上第一个a标签为：",text)
# 获取页面上第一个超文本链接地址
att = driver.find_element_by_css_selector("a").get_attribute("属性名")
print("页面第一个标签属性值为：",att)
# 判断页面span元素是否可见
display = driver.find_element_by_css_selector("span").is_displayed()
print("span按钮是否可见：",display)
# 判断取消按钮是否可用
endbled = driver.find_element_by_css_selector("#cancel").is_enabled()
print("取消按钮是否可用：",endbled)
# 判断旅游是否被选中
selected = driver.find_element_by_css_selector("#ly").is_selected()
print("取消按钮是否可用：",selected)
# 暂停3秒
sleep(3)
# 关闭浏览器
driver.quit()