"""
目标：
     unittest框架————TestSuite使用
步骤：
     1. 导包 import unittest
     2. 实例化获取TestSuite对象
     3. 调用addTest方法获取用例，到指定套件中
案例：
     编写  求和测试函数
"""
# 导包
import unittest
from scripts.text18_TestCase import Test01
# from scripts.文件名 import Test01  可以继续执行别的文本，进行导包就可以了
# 实例化获取TestSuite对象
suite = unittest.TestSuite()
# 调用添加方法
# 方法一  类名
suite.addTest(Test01("test_add"))
suite.addTest(Test01("test_add02"))
# 方法二  执行所有test开头的用例  拓展
# suite.addTest(unittest.makeSuite(Test01))
# 执行测试套件
runner = unittest.TextTestRunner()
runner.run(suite)