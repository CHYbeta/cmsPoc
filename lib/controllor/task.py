from lib.controllor.controllor import load_poc, run_poc
from lib.core.common import begin_time_info, end_time_info, get_script_path
from lib.core.data import target


class Task:
    def __init__(self, target):
        self.url = target.url
        self.type = target.type
        self.poc_name = target.script
        self.poc_path = get_script_path() + self.type
        self.poc = load_poc(self.poc_name, [self.poc_path])
        self.begin_time = begin_time_info()

    def info(self):
        print("\033[33m[*] The target url: {} \033[0m".format(self.url))
        print("\033[33m[*] The target type: {} \033[0m".format(self.type))
        print("\033[33m[*] Try to load the script: {} \033[0m".format(
            self.poc_name))

    def run(self):
        if target.type is not None:
            if target.script is not None:
                if run_poc(self.poc, self.url):
                    self.status = "Success"
                else:
                    self.status = "Fail"

    def log(self):
        try:
            with open('log/log.csv', 'a') as f:
                self.record = "%s,%s,%s,%s,%s,%s\n" % (self.url, self.type,
                                                       self.poc_name,
                                                       self.status,
                                                       self.begin_time,
                                                       self.end_time)
                f.write(self.record)
                print("\033[33m[*] Log save at log/log.csv\033[0m")
        except Exception:
            print("\033[31m[!] Log save errors!\033[0m\n")

    def end(self):
        print("\033[33m[*] Complete this task: {} \033[0m".format(self.url))
        self.end_time = end_time_info()
        self.log()
