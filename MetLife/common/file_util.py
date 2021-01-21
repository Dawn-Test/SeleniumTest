#!/usr/bin/env python3
# coding=utf-8
import datetime
import os


def get_work_path():
    work_root_directory = os.path.dirname(os.path.dirname(__file__))
    return work_root_directory


def gen_images_directory():
    images_directory = os.path.join(get_work_path(), 'images')
    if not os.path.exists(images_directory):
        os.makedirs(images_directory)
    return images_directory


def get_curr_time_str():
    return datetime.datetime.now().strftime('%Y%m%d%H%M%S')


if __name__ == '__main__':
    print(get_work_path())
    print(get_curr_time_str())
