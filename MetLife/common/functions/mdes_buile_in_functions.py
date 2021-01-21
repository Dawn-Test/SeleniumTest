#!/usr/bin/env python3
# coding=utf-8

import random
import time


def random_bank_id():
    """ 随机生成银行卡号 """
    a = '622202' + str(random.randint(1000000000, 9999999999))
    return a

def random_id_extend():
    """ 随机生成军人证/护照等证件号 """
    a = 'S' + str(random.randint(1000000000, 9999999999))
    return a

def local_date():
    """ 生成当天日期 """
    date = time.strftime("%Y%m%d", time.localtime())
    return date

if __name__ == '__main__':
    print(random_id_extend())