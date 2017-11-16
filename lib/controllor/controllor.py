import os
import re
import imp
import time
from lib.core.data import target,path
from lib.core.data import path



def beginTimeInfo():
	print("\033[33m[*] Start at: {} \033[0m".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

def endTimeInfo():
	print("\033[33m[*] End at: {} \033[0m".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
