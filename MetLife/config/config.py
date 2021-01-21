import configparser
import os


def get_config(section, option):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    cf = configparser.ConfigParser()
    # print(root_dir)
    cf.read(root_dir + '\\sys.conf')
    return cf.get(section, option)
