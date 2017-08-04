import os
import re
import imp
import time
from lib.core.data import target,path
from lib.core.data import path

def init():
	initPath()
	initTargetInfo()

def initPath():
	path.SYSTEM_PATH = os.getcwd()
	path.SCRIPTS_PATH = path.SYSTEM_PATH + "/scripts/"

def initTargetInfo():
	print("\033[33m[*] The target url: {} \033[0m".format(target.url))
	print("\033[33m[*] The target type: {} \033[0m".format(target.type))
	print("\033[33m[*] Try to load the script: {} \033[0m".format(target.script))

def startTimeInfo():
	print("\033[33m[*] Start at: {} \033[0m".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

def endTimeInfo():
	print("\033[33m[*] End at: {} \033[0m".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

def loadScripts():
	try:
		file, pathname, desc = imp.find_module(os.path.splitext(target.script)[0],[path.SCRIPTS_PATH+target.type])
	except ImportError as e:
		print("\033[31m[!] Import script error.Please make sure the script name and type name are right!\033[0m\n")
		exit()
	script = imp.load_module('poc',file, pathname, desc)
	return script


def run(script):
	startTimeInfo()
	script.poc()
	endTimeInfo()