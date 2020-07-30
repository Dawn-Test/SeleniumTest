import unittest
from parameterized import parameterized

"""
目标：parameterized插件应用
步骤：
     1.导包 from parameterized import parameterized
     2.修饰测试函数 @parameterized.expand（列表类型数据）
     3.在床上函数中使用变量接收，传递来的值
语法：
     1.单个参数：值位列表
     2.多个参数：值为列表嵌套元组 如【（1,2,3）,（2,3,4）】
"""

class Test01(unittest.TestCase):
    # 单个参数使用方法
    # @parameterized.expand(["1","2","3"])
    # def test_add(self,num):
    #     print("num:",num)

    # 多个参数使用方法  写法一
    # @parameterized.expand([(1,2,3),(3,0,3),(2,1,3)])
    # def test_add(self,a,b,result):
    #     print("{}+{}+{}:".format(a,b,result))



    # 推荐！！！
    def get_data(self):
        return [(1,2,3),(3,0,3),(2,1,3)]

    @parameterized.expand(get_data())
    def test_add_more(self,a,b,result):
        print("{}+{}+{}:".format(a,b,result))
