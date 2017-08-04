import argparse

def cmdLineParser():
	parser =argparse.ArgumentParser()

	parser.add_argument("-t","--type",required=True,help="e.g.,phpcms")
	parser.add_argument("-s","--script",required=True,help="Select script")
	parser.add_argument("-u","--url", required=True,help="Input a target url")
	args = parser.parse_args()
	
	return args