from selenium.webdriver.common.by import By


class LoginPageLocator:
    # 用户名
    usrname = (By.XPATH, '//input[@id="loginForm:userCode"]', '用户名')
    # 密码
    password = (By.XPATH, '//input[@id="loginForm:userPassword"]','密码')
    # 登陆button
    loginBTN = (By.XPATH, '//input[@id="loginForm:loginBtn"]','登陆')




