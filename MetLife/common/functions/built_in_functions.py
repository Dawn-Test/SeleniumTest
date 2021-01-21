#!/usr/bin/env python3
# coding=utf-8
import json
import os
import random
import uuid
from datetime import datetime
from dateutil.relativedelta import relativedelta
from random import randint

from xeger import Xeger

ID_CODE_LIST = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
CHECK_CODE_LIST = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]

extend_lib_dir = os.path.dirname(__file__)

with open(os.path.join(extend_lib_dir, "district_code.json"), encoding="utf-8") as f:
    AREA_DICT = json.loads(f.read())

with open(os.path.join(extend_lib_dir, "name_codes.json"), encoding="utf-8") as f:
    js = json.loads(f.read())
    LAST_NAMES = js.get("last_names")
    FIRST_NAMES = js.get("first_names")


def get_time(fmt='%Y%m%d%H%M%S'):
    return datetime.now().strftime(fmt)

def get_time_mdes(fmt='%Y%m%d%H%M'):
    return datetime.now().strftime(fmt)

def gen_birthday(age=0, day=0, fmt='%Y%m%d'):
    """
    生成出生日期
    :param age: 年龄
    :param day: 天数
    :param fmt: 时间字符串格式
    :return: 出生日期
    """
    today_date = datetime.today()
    if age > 0:
        today_date = today_date + relativedelta(years=-abs(age))
    if day > 0:
        today_date = today_date + relativedelta(days=-abs(day))
    else:
        today_date = today_date + relativedelta(days=+abs(day))
    return today_date.strftime(fmt)


def gen_rand_str(str_len=10):
    return ''.join([chr(randint(65, 90)) for i in range(str_len)])


def get_uuid():
    """
    返回一个uuid，并不带“-”
    :return:
    """
    return ''.join(str(uuid.uuid4()).split("-"))


def get_str_reg(reg_str):
    """
    根据正则公式生成字符串
    :param reg_str: 正则格式
    :return:
    """
    x = Xeger(limit=500)
    return x.xeger(reg_str)


def gen_phone():
    """
    随机生成手机号
    :return 手机号
    """
    phone_pres = ['135', '139', '138', '157', '151', '152', '130', '131', '132']
    phone_pre = phone_pres[int(random.random() * len(phone_pres))]
    phone_suf = ''
    for i in range(8):
        phone_suf += str(int(random.random() * 10))
    return phone_pre + phone_suf


def gen_email():
    """
    随机生成邮箱
    :return: 邮箱
    """
    email_servers = ['@qq.com', '@sina.com', '@google.com', '@outlook.cn', '@apple.com']
    chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f',
             'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    email_pre_count = int(random.random() * 8) + 4
    email_pre = ''
    for i in range(email_pre_count):
        email_pre += chars[int(random.random() * len(chars))]

    return email_pre + email_servers[int(random.random() * len(email_servers))]


def _random_names(names):
    length = len(names)
    return names[int(random.random() * length) + 1]


def gen_name(encode_flag=True):
    """
    随机生成姓名
    :return 姓名
    """
    l_name = _random_names(LAST_NAMES)
    first_name_count = int(random.random() * 2) + 1
    for i in range(first_name_count):
        f_name = _random_names(FIRST_NAMES)
        l_name += f_name
    return l_name


def gen_id_card(birthday, gender, area_code=None):
    """
    :param birthday:生日，格式为YYYY-mm-dd或者YYYYmmdd
    :param gender 性别
    :param area_code: 地区号 可以传入，如果不传入则会随机生成
    """

    if not area_code:
        area_list = list(AREA_DICT.keys())
        area_code = area_list[random.randint(0, len(area_list))]
    if not str(birthday):
        return None
    birthday = str(birthday).replace('-', "")
    rd = random.randint(0, 999)
    if gender == 0 or gender == '女':
        gender_num = rd if rd % 2 == 0 else rd + 1
    else:
        gender_num = rd if rd % 2 == 1 else rd - 1
    result = str(area_code) + birthday + str(gender_num).zfill(3)
    return result + str(CHECK_CODE_LIST[
                            sum([a * b for a, b in zip(ID_CODE_LIST, [int(a) for a in result])]) % 11])

if __name__ == '__main__':
    # print(get_time_mdes('%Y%m%d %H:%M:%S'))
    print(get_time_mdes(fmt='%Y%m%d%H%M'))
    print(gen_birthday(54,4))

