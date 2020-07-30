"""
目标：写入josn
方法：
    json.dump（写什么数据（字典数据），往哪写（文件流））
"""''
# import json
# """json写入"""
# # data = {"name":"wangjinlong", "age":22}
# data = {"name":"王金龙,", "age": 22}
# # 调用写入方法
# with open("../scripts/1.json", "w", encoding="utf-8")as f:
#     json.dump(data, f, ensure_ascii=False)

"""
目标：读取
方法：load
"""
# 导包
import json
# 获取文件名并调用load方法
with open("../scripts/1.json", "r",encoding="utf-8")as f:
    data = json.load(f)
    print(data)