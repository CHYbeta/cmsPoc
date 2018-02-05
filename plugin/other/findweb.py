from lib.core.data import target, path
import requests


def whatweb():
    print("\033[33m[*] Try to find the type of %s" % target.url)

    # query the footprint
    query = {"url": target.url}
    what_web_url = "http://whatweb.bugscaner.com/what/"
    response = requests.post(whatWebUrl, data=query)
    print(response.text)
