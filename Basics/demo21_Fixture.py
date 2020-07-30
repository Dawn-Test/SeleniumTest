"""
目标：
     unittest框架————fixture用法
     fixture 其实就是两个函数，这个函数可以一起使用，也可以单独使用
         1.初始化函数：def setUp（）
         2.结束函数：def tearDown()
    fixture级别
    函数级别
    类级别
    模块级别【了解】
"""
import unittest

def setUpModule():
    print("setUpModule")
def tearDownModule():
    print("tearDownModule")
class Test03(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass被执行")

    @classmethod
    def tearDownClass(self):
        print("tearDownClass被执行")
    def setUp(self):
        print("setUp被执行")
    def tearDown(self):
        print("tearDown被执行")
    def test01(self):
        print("test01被执行")
    def test02(self):
        print("test02被执行")