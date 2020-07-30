# 导包
# import logging

# 设置日志级别,默认级别为warning以上的级别
# logging.basicConfig(level=logging.DEBUG)

# 设置修改默认的输出日志格式
# fm = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] -%(message)s)]"
# 设置日志输出到指定的文件中

# logging.basicConfig(level=logging.DEBUG, format=fm, filename="../scripts/1.log")
#  调用指定级别，输入日志信息
# logging.debug("this id a 王金龙..")
# logging.info("this id a ingo..")
# logging.warning("this id a warning..")
# logging.error("this id a error..")
# logging.critical("this id a critical..")


"""
目标：学习 logging底层模块实现
    1.logger
"""
# 注意以后不再使用此方法
# import logging

import logging.handlers
# 导包时 导入import logging.handlers
# 推荐：注意logging是包名，导入包名时会自动执行下面的__init_文件
# 所有这样导入，相当于导入了logging，handlers为模块名称

# 获取logger
# logger = logging.getLogger()
# 修改名称
from time import sleep

logger = logging.getLogger("admin")
# 设置级别
logger.setLevel(logging.INFO)
# 获取控制台处理器
sh = logging.StreamHandler()
# 到文件，根据时间切割
th = logging.handlers.TimedRotatingFileHandler(filename="../scripts/1.log",
                                        when="S",
                                        interval=1,
                                        backupCount=3)
# 添加格式器
fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] -%(message)s)]"
fm = logging.Formatter(fmt)
# 将格式器添加到处理器中
sh.setFormatter(fm)
th.setFormatter(fm)
# 将处理器添加到 logger
logger.addHandler(sh)
logger.addHandler(th)
while True:
    sleep(1)

    # 输入信息
    logger.info("info")
    logger.debug("debug")