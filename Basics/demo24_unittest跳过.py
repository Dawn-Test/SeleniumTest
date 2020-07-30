"""
目标：unittest skip 与 skip功能
语法：
    @unittest.skip("原因")
    @unittest.skipIf("条件，原因")
"""
# 导包
import unittest
# 新建测试类
# @unittest.skip("test01方法暂未实现")
class Tset01(unittest.TestCase):
    # 新建测试方法
    # @unittest.skip("test01方法暂未实现")
    def test01(self):
        print("test01")
    # 新建测试方法02
    # @unittest.skipIf(version > 25, "版本大约25，跳过此用例")
    def test02(self):
        print("test02")