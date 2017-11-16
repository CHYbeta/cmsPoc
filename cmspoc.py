from lib.core.data import target,path
from lib.parse.cmdline import cmdLineParser
from lib.core.common import banner
from lib.controllor.task import loadScripts
from lib.controllor.task import runPoc,autoPoc
# from lib.controllor.init import initPath,
from lib.controllor.task import start
import requests

def cli():
	try:
		banner()
		target.update(cmdLineParser().__dict__)
		start()
	except requests.exceptions.InvalidSchema as e:
		print("\033[31m[!] Please input the right url.\033[0m\n")
	except requests.exceptions.MissingSchema as e:
		print("\033[31m[!] Please apply a right schema.e.g:http://www.example.com\033[0m\n")
	except requests.exceptions.ConnectionError as e:
		print("\033[31m[!] The network is busy.Connetion error!\033[0m\n")
	except KeyboardInterrupt as e:
		print("\033[31m[!] User aborted!\033[0m\n")


if __name__ == "__main__":
    cli()
