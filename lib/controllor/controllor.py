import time


def begin_time_info():
    print("\033[33m[*] Start at: {} \033[0m".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))


def end_time_info():
    print("\033[33m[*] End at: {} \033[0m".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
