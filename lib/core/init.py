import os
from lib.core.data import target, path


def init_path():
    path.SYSTEM_PATH = os.getcwd()
    path.SCRIPTS_PATH = path.SYSTEM_PATH + "/scripts/"


def init_target_info():
    print("\033[33m[*] The target url: {} \033[0m".format(target.url))
    print("\033[33m[*] The target type: {} \033[0m".format(target.type))
    print("\033[33m[*] Try to load the script: {} \033[0m".format(target.script))
