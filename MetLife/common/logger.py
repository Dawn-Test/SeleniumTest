import logging
from datetime import datetime
import os

from loguru import logger

log_dir = os.path.dirname(os.path.dirname(__file__))
logger.add(os.path.join(log_dir, 'logs', '{time}.log'), encoding="utf-8")

# class Log(object):
#     def __init__(self):
#         """ log目录 """
#         log_root = os.path.dirname(os.path.dirname(__file__))
#         log_dir = os.path.join(log_root, "logs")
#         log_file_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + '.log'
#         self.logname = log_dir + '\\' + log_file_name
#
#     def printconsole(self, level, message):
#         """ log输出控制 """
#         """ 创建logger """
#         logger = logging.getLogger('log')
#         logger.setLevel(logging.DEBUG)
#         """ 创建一个handler控制写入到文件 """
#         fh = logging.FileHandler(self.logname, 'a')
#         fh.setLevel(logging.DEBUG)
#         """ 创建一个handler控制输出到控制台 """
#         ch = logging.StreamHandler()
#         ch.setLevel(logging.DEBUG)
#         """ 定义handler输出格式 """
#         formatter = logging.Formatter('%(asctime)s - %(funcName)s : [%(levelname)s] ---> %(message)s')
#         fh.setFormatter(formatter)
#         ch.setFormatter(formatter)
#         """ 添加handler到logger """
#         logger.addHandler(fh)
#         logger.addHandler(ch)
#         """ 记录日志 """
#         if level == 'info':
#             logger.info(message)
#         elif level == 'debug':
#             logger.info(message)
#         elif level == 'warning':
#             logger.info(message)
#         elif level == 'error':
#             logger.info(message)
#         logger.removeHandler(ch)
#         logger.removeHandler(fh)
#
#     def debug(self, message):
#         self.printconsole('debug', message)
#
#     def info(self, message):
#         self.printconsole('info', message)
#
#     def warning(self, message):
#         self.printconsole('warning', message)
#
#     def error(self, message):
#         self.printconsole('error', message)
#
#
#
# if __name__ == "__main__":
#     log = Log()
#     log.info('info')
#     log.debug('debug')
#     log.warning('warning')
#     log.error('error')
