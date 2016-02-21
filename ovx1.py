#!/usr/bin/python

import os

def main():
	print os.getcwd()
	os.chdir("/home/deepanshu/OpenVirteX/scripts")
	#print os.popen("sh ovx.sh").read()
	os.system("sh ovx.sh")

main()
