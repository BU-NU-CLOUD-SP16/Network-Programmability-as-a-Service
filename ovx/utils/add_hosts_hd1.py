#!/usr/bin/python
import os
import sys
def main():
	os.chdir("/home/ovx/OpenVirteX/utils")
	for c in commands: 
		tmp = os.popen(c).read()
		print tmp
commands=[]
commands.append("sudo python ovxctl.py -n stopNetwork 1")
commands.append("sudo python ovxctl.py -n connectHost 1 00:a4:23:05:00:00:00:03 1 00:00:00:00:00:01")
commands.append("sudo python ovxctl.py -n connectHost 1 00:a4:23:05:00:00:00:04 1 00:00:00:00:00:03")
commands.append("sudo python ovxctl.py -n startNetwork 1")
commands.append("sudo python ovxctl.py -n stopNetwork 2")
commands.append("sudo python ovxctl.py -n connectHost 2 00:a4:23:05:00:00:00:03 2 00:00:00:00:00:02")
commands.append("sudo python ovxctl.py -n connectHost 2 00:a4:23:05:00:00:00:04 2 00:00:00:00:00:04")
commands.append("sudo python ovxctl.py -n startNetwork 2")
main()