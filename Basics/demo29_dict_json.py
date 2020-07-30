"""
目标：
    将python字典对象 转为 json字符串
操作：
    1.导包 import json
    2.调用dumps()方法  字典对象转为json字符串-->注意：而不是dump方法

    json字符串转为python字典
       方法：lodes（）-->将json字符串转为python字典  注意：lodes带s
"""
"""将python字典对象 转为 json字符串"""
# 导包
import json
# # 定义json字符串

# data = {"name":"张三", "age":18}
# # 转换
# data2 = json.dumps(data)
# print(data2)
# print("转换之后的类型：", type(data2))

"""将json字符串 转为 python字典对象"""
# 定义json
# 里面的键名必须为双引号！！
data = '{"name":"张三", "age":18}'
print("未转换之后的类型：", type(data))
# 转换
data2 = json.loads(data)
print(data2)
print("转换之后的类型：", type(data2))