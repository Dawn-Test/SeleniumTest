from time import sleep
# 导包 webdriver
from selenium import webdriver
# 获取谷歌浏览器对象
driver = webdriver.Chrome(r'd:\webdrivers\chromedriver.exe')
# 最大化浏览器
driver.maximize_window()
# 隐式等待
driver.implicitly_wait(30)
# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
# 设置cookie

url = 'https://www.baidu.com'
driver.get(url)
driver.add_cookie({"name":"BDUSS","value":"GxhVU10TjBrLS1iWDhZb0RyTmhFUmRPdnZicH5pRWJPUzRBNGNrSGZmaHdlRjllRVFBQUFBJCQAAAAAAAAAAAEAAAAZgTW4aHN2c2hza3MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHDrN15w6zdeT"})

# 获取所有的cookies信息
cookies = driver.get_cookies()
print("cookies的内容为：",cookies)
for co in cookies:
    print(co['name'])

# 暂停2秒
sleep(2)

# 刷新  必须进行刷新才能看到效果
driver.refresh()
"""
目标：cookie操作
方法：
     使用cookie绕过百度登录
需求：
     1.手动登录百度网站
     2.手动获取登录后的cookie “BDUSS”
     3.使用selenium内的add_cookie(name = 'BDUSS',value='xxxx')
"""
# 暂停三秒

sleep(3)
# 退出浏览器
driver.quit()