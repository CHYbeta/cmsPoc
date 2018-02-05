# -*- encoding:"utf-8"-*-
import requests

from lib.controllor.task import Task
from lib.core.common import banner
from lib.core.data import target
from lib.parse.cmdline import cmd_line_parser


def cli():
    try:
        banner()
        target.update(cmd_line_parser().__dict__)
        task = Task(target)
        task.info()
        task.run()
        task.end()
    except requests.exceptions.InvalidSchema:
        print("\033[31m[!] Please input the right url.\033[0m\n")
    except requests.exceptions.MissingSchema:
        print(
            "\033[31m[!] Please apply a right schema.e.g:http://www.example.com\033[0m\n"
        )
    except requests.exceptions.ConnectionError:
        print("\033[31m[!] The network is busy.Connection error!\033[0m\n")
    except KeyboardInterrupt:
        print("\033[31m\n[!] User aborted!\033[0m\n")
    except Exception:
        print("\033[31m[!] Something error!\033[0m\n")
        exit()


if __name__ == "__main__":
    cli()
