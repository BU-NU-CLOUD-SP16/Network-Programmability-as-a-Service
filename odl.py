#!/usr/bin/python

import os
import sys


def main():
	print os.getcwd()
	os.chdir("/home/deepanshu/odl")
	if len(sys.argv)==1:
	
		os.system("./bin/karaf")

	elif len(sys.argv)==2 and sys.argv[2]=="clean":
		os.system("./bin/karaf clean")

	else:
		print "Invalid command entered"


main()



