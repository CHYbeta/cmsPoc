import os
import imp
from lib.core.data import target
from lib.core.data import path
from lib.core.init import init_path, init_target_info
from lib.plugin.other.findweb import whatweb
from controllor import begin_time_info, end_time_info


def start():
    begin_time_info()
    if target.type is not None:
        if target.script is not None:
            init_path()
            init_target_info()
            run_poc(load_script())
        else:
            init_path()
            autopoc()
    elif target.script is None:
        try_find_type()
        autopoc()
    else:
        print("set the type")
    end_time_info()


def load_script():
    try:
        file_name, path_name, description = imp.find_module(
            os.path.splitext(target.script)[0],
            [path.SCRIPTS_PATH + target.type])
    except ImportError as e:
        print(
            "\033[31m[!] Import script error.Please make sure the script name and type name are right!\033[0m\n"
        )
        exit()
    script = imp.load_module('poc', file_name, path_name, description)
    return script


def run_poc(script):
    script.poc()


def auto_poc():
    print("autopoc")


def try_find_type():
    whatweb()
