"""
目标：
     unittest框架————TestCase使用
步骤：
     1. 导包 import unittest
     2. 新建类 并继承 unittest.TestCase
     3. 测试方法必须以test字母开头
案例：
     编写  求和测试函数
"""
# 导包
import unittest

# 编写求和测试函数
def add(x,y):
    return x+y

# 定义测试类 并继承
class Test01(unittest.TestCase):   # 如果鼠标在这里点运行，则运行所有用例
    # 定义测试 注意：以test开头！！！否则不运行
    def test_add(self):            # 如果鼠标在这里点运行，则运行当前用例
        result = add(1,1)
        print("结果为：",result)

    def test_add02(self):           # 如果鼠标在这里点运行，则运行当前用例
        result = add(1,2)
        print("结果为：",result)
        print("name内置变量获取当前运行的模块名称：",__name__)

if __name__ == "_main_":
    unittest.main()