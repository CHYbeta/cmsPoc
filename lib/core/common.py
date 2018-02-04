import os
import time

from lib.core.setting import BANNER


def banner():
    print(BANNER)


def begin_time_info():
    begin_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print("\033[33m[*] Start at: {} \033[0m".format(begin_time))
    return begin_time


def end_time_info():
    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print("\033[33m[*] End at: {} \033[0m".format(end_time))
    return end_time


def get_script_path():
    return init_path()


def init_path():
    return os.getcwd() + "/scripts/"
