"""
目标：基于unitt框架执行生成HTML报告
操作：
    1.复制hrmltestrunner.py文件到指定目录中
    2.导包from HTMLTestRunner import HTMLTestRunner
    3.获取报告存放文件流，并实例化HTMLTestRunner类，执行run方法

"""
# 导包
import time
import unittest 


from tools.HTMLTestRunner import HTMLTestRunner
# 定义 测试套件
suite = unittest.defaultTestLoader.discover("../scripts",pattern="text24*.py")
# 定义报告存放路径及文件名称
a = "../scripts/{}.html".format(time.strftime("%Y_%m_%d %H_%M_%S"))
# 获取报告文件流并执行
with open(a,"wb") as f:
    HTMLTestRunner(stream=f,verbosity=2,title="xx项目自动化测试报告").run(suite)

