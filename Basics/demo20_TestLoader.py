"""
目标：
     unittest框架————演示testloader（）类的方法
作用：
     搜索指定目录下指定开头的py文件，在py文件中搜索test开头的测试方法
     并且将这些方法添加到测试套件中
步骤：
     1. 导包 import unittest
     2. 调用testloader类下的discaver方法

"""
# 导包
import unittest
# 调用方法
suite = unittest.TestLoader().discover("../python")
# 拓展以**开头的文件
suite = unittest.TestLoader().discover("../python",pattern="1**.py")
# 拓展 使用
suite = unittest.defaultTestLoader.discover("../python")
# 执行 套件方法 texttestrunner
unittest.TextTestRunner().run(suite)