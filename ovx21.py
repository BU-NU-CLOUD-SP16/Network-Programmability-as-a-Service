#!/usr/bin/python

import os

def main():
	print os.getcwd()
	os.chdir("/home/deepanshu/OpenVirteX/utils")
	for c in commands: 
		tmp = os.popen(c).read()
		print tmp




commands=[]
#######Virtual network 1
commands.append("sudo python ovxctl.py -n createNetwork tcp:192.168.241.141:6633 10.0.0.0 24")
commands.append("sudo python ovxctl.py -n createSwitch 1 00:00:00:00:00:00:01:00")
commands.append("sudo python ovxctl.py -n createSwitch 1 00:00:00:00:00:00:02:00")

commands.append("sudo python ovxctl.py -n createPort 1 00:00:00:00:00:00:01:00 1")
commands.append("sudo python ovxctl.py -n createPort 1 00:00:00:00:00:00:01:00 2")

commands.append("sudo python ovxctl.py -n createPort 1 00:00:00:00:00:00:02:00 1")
commands.append("sudo python ovxctl.py -n createPort 1 00:00:00:00:00:00:02:00 2")


commands.append("python ovxctl.py -n connectLink 1 00:a4:23:05:00:00:00:01 2 00:a4:23:05:00:00:00:02 2 spf 1")



commands.append("python ovxctl.py -n connectHost 1 00:a4:23:05:00:00:00:01 1 00:00:00:00:00:01")
commands.append("python ovxctl.py -n connectHost 1 00:a4:23:05:00:00:00:02 1 00:00:00:00:00:02")


commands.append("python ovxctl.py -n startNetwork 1")

#######Virtual network 2
commands.append("sudo python ovxctl.py -n createNetwork tcp:192.168.241.141:6653 10.0.0.0 24")
commands.append("sudo python ovxctl.py -n createSwitch 2 00:00:00:00:00:00:03:00")
commands.append("sudo python ovxctl.py -n createSwitch 2 00:00:00:00:00:00:04:00")

commands.append("sudo python ovxctl.py -n createPort 2 00:00:00:00:00:00:03:00 1")
commands.append("sudo python ovxctl.py -n createPort 2 00:00:00:00:00:00:03:00 2")


commands.append("sudo python ovxctl.py -n createPort 2 00:00:00:00:00:00:04:00 1")
commands.append("sudo python ovxctl.py -n createPort 2 00:00:00:00:00:00:04:00 2")


commands.append("python ovxctl.py -n connectLink 2 00:a4:23:05:00:00:00:03 2 00:a4:23:05:00:00:00:04 2 spf 1")

commands.append("python ovxctl.py -n connectHost 2 00:a4:23:05:00:00:00:03 1 00:00:00:00:00:03")
commands.append("python ovxctl.py -n connectHost 2 00:a4:23:05:00:00:00:04 1 00:00:00:00:00:04")
commands.append("python ovxctl.py -n startNetwork 2")

main()
