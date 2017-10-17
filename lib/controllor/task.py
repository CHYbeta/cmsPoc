import os
import re
import imp
from lib.core.data import target,path
from lib.core.data import path
from lib.core.init import initPath,initTargetInfo
from lib.plugin.other.findweb import whatweb
from controllor import beginTimeInfo,endTimeInfo

def start():
	beginTimeInfo()
	if target.type != None:
		if target.script != None:
			initPath()
			initTargetInfo()
			runPoc(loadScripts())
			endTimeInfo()
		else:
			initPath()
			autoPoc()
			endTimeInfo()
	elif target.script == None:
		tryFindType()
		autoPoc()
		endTimeInfo()
	else:
		print("set the type")
		endTimeInfo()
		exit()


def loadScripts():
	try:
		file, pathname, desc = imp.find_module(os.path.splitext(target.script)[0],[path.SCRIPTS_PATH+target.type])
	except ImportError as e:
		print("\033[31m[!] Import script error.Please make sure the script name and type name are right!\033[0m\n")
		exit()
	script = imp.load_module('poc',file, pathname, desc)
	return script

def runPoc(script):
	script.poc()

def autoPoc():
	print("autopoc")

def tryFindType():
	whatweb()
