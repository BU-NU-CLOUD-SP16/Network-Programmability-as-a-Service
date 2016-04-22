#!/usr/bin/python

import os
import sys

def main():
	os.chdir("/home/ubuntu/OpenVirteX/utils")
	for c in commands: 
		tmp = os.popen(c).read()
		print tmp
try:
    ip1 = sys.argv[1]+":"+sys.argv[2]
    ip2 = sys.argv[3]+":"+sys.argv[4]
    
except:
    print "Please enter IP address and port number of 2 controllers as CLI"
    sys.exit()

commands=[]

#######Virtual network 1
commands.append("sudo python ovxctl.py -n createNetwork tcp:"+ip1+" 10.0.0.0 16 1")
commands.append("sudo python ovxctl.py -n createSwitch 1 00:00:00:00:00:00:01:00")
commands.append("sudo python ovxctl.py -n createSwitch 1 00:00:00:00:00:00:02:00")
commands.append("sudo python ovxctl.py -n createSwitch 1 00:00:00:00:00:00:03:00")
commands.append("sudo python ovxctl.py -n createSwitch 1 00:00:00:00:00:00:04:00")
commands.append("sudo python ovxctl.py -n createSwitch 1 00:00:00:00:00:00:05:00")
commands.append("sudo python ovxctl.py -n createSwitch 1 00:00:00:00:00:00:06:00")
commands.append("sudo python ovxctl.py -n createSwitch 1 00:00:00:00:00:00:07:00")

commands.append("sudo python ovxctl.py -n createPort 1 00:00:00:00:00:00:01:00 1")
commands.append("sudo python ovxctl.py -n createPort 1 00:00:00:00:00:00:01:00 2")

commands.append("sudo python ovxctl.py -n createPort 1 00:00:00:00:00:00:02:00 1")
commands.append("sudo python ovxctl.py -n createPort 1 00:00:00:00:00:00:02:00 2")
commands.append("sudo python ovxctl.py -n createPort 1 00:00:00:00:00:00:02:00 3")


commands.append("sudo python ovxctl.py -n createPort 1 00:00:00:00:00:00:03:00 1")
commands.append("sudo python ovxctl.py -n createPort 1 00:00:00:00:00:00:03:00 2")
commands.append("sudo python ovxctl.py -n createPort 1 00:00:00:00:00:00:03:00 3")

commands.append("sudo python ovxctl.py -n createPort 1 00:00:00:00:00:00:04:00 1")
commands.append("sudo python ovxctl.py -n createPort 1 00:00:00:00:00:00:04:00 2")
commands.append("sudo python ovxctl.py -n createPort 1 00:00:00:00:00:00:04:00 3")


commands.append("sudo python ovxctl.py -n createPort 1 00:00:00:00:00:00:05:00 1")
commands.append("sudo python ovxctl.py -n createPort 1 00:00:00:00:00:00:05:00 2")
commands.append("sudo python ovxctl.py -n createPort 1 00:00:00:00:00:00:05:00 3")

commands.append("sudo python ovxctl.py -n createPort 1 00:00:00:00:00:00:06:00 1")
commands.append("sudo python ovxctl.py -n createPort 1 00:00:00:00:00:00:06:00 2")
commands.append("sudo python ovxctl.py -n createPort 1 00:00:00:00:00:00:06:00 3")

commands.append("sudo python ovxctl.py -n createPort 1 00:00:00:00:00:00:07:00 1")
commands.append("sudo python ovxctl.py -n createPort 1 00:00:00:00:00:00:07:00 2")
commands.append("sudo python ovxctl.py -n createPort 1 00:00:00:00:00:00:07:00 3")

commands.append("sudo python ovxctl.py -n connectLink 1 00:a4:23:05:00:00:00:01 1 00:a4:23:05:00:00:00:02 3 spf 1")
commands.append("sudo python ovxctl.py -n connectLink 1 00:a4:23:05:00:00:00:01 2 00:a4:23:05:00:00:00:05 3 spf 1")
commands.append("sudo python ovxctl.py -n connectLink 1 00:a4:23:05:00:00:00:02 1 00:a4:23:05:00:00:00:03 3 spf 1")
commands.append("sudo python ovxctl.py -n connectLink 1 00:a4:23:05:00:00:00:02 2 00:a4:23:05:00:00:00:04 3 spf 1")
commands.append("sudo python ovxctl.py -n connectLink 1 00:a4:23:05:00:00:00:05 1 00:a4:23:05:00:00:00:06 3 spf 1")
commands.append("sudo python ovxctl.py -n connectLink 1 00:a4:23:05:00:00:00:05 2 00:a4:23:05:00:00:00:07 3 spf 1")

commands.append("sudo python ovxctl.py -n startNetwork 1")

#######Virtual network 2
commands.append("sudo python ovxctl.py -n createNetwork tcp:"+ip2+" 10.0.0.0 16 2")
commands.append("sudo python ovxctl.py -n createSwitch 2 00:00:00:00:00:00:01:00")
commands.append("sudo python ovxctl.py -n createSwitch 2 00:00:00:00:00:00:02:00")
commands.append("sudo python ovxctl.py -n createSwitch 2 00:00:00:00:00:00:03:00")
commands.append("sudo python ovxctl.py -n createSwitch 2 00:00:00:00:00:00:04:00")
commands.append("sudo python ovxctl.py -n createSwitch 2 00:00:00:00:00:00:05:00")
commands.append("sudo python ovxctl.py -n createSwitch 2 00:00:00:00:00:00:06:00")
commands.append("sudo python ovxctl.py -n createSwitch 2 00:00:00:00:00:00:07:00")

commands.append("sudo python ovxctl.py -n createPort 2 00:00:00:00:00:00:01:00 1")
commands.append("sudo python ovxctl.py -n createPort 2 00:00:00:00:00:00:01:00 2")

commands.append("sudo python ovxctl.py -n createPort 2 00:00:00:00:00:00:02:00 1")
commands.append("sudo python ovxctl.py -n createPort 2 00:00:00:00:00:00:02:00 2")
commands.append("sudo python ovxctl.py -n createPort 2 00:00:00:00:00:00:02:00 3")

commands.append("sudo python ovxctl.py -n createPort 2 00:00:00:00:00:00:03:00 1")
commands.append("sudo python ovxctl.py -n createPort 2 00:00:00:00:00:00:03:00 2")
commands.append("sudo python ovxctl.py -n createPort 2 00:00:00:00:00:00:03:00 3")

commands.append("sudo python ovxctl.py -n createPort 2 00:00:00:00:00:00:04:00 1")
commands.append("sudo python ovxctl.py -n createPort 2 00:00:00:00:00:00:04:00 2")
commands.append("sudo python ovxctl.py -n createPort 2 00:00:00:00:00:00:04:00 3")


commands.append("sudo python ovxctl.py -n createPort 2 00:00:00:00:00:00:05:00 1")
commands.append("sudo python ovxctl.py -n createPort 2 00:00:00:00:00:00:05:00 2")
commands.append("sudo python ovxctl.py -n createPort 2 00:00:00:00:00:00:05:00 3")


commands.append("sudo python ovxctl.py -n createPort 2 00:00:00:00:00:00:06:00 1")
commands.append("sudo python ovxctl.py -n createPort 2 00:00:00:00:00:00:06:00 2")
commands.append("sudo python ovxctl.py -n createPort 2 00:00:00:00:00:00:06:00 3")


commands.append("sudo python ovxctl.py -n createPort 2 00:00:00:00:00:00:07:00 1")
commands.append("sudo python ovxctl.py -n createPort 2 00:00:00:00:00:00:07:00 2")
commands.append("sudo python ovxctl.py -n createPort 2 00:00:00:00:00:00:07:00 3")

commands.append("sudo python ovxctl.py -n connectLink 2 00:a4:23:05:00:00:00:01 1 00:a4:23:05:00:00:00:02 3 spf 1")
commands.append("sudo python ovxctl.py -n connectLink 2 00:a4:23:05:00:00:00:01 2 00:a4:23:05:00:00:00:05 3 spf 1")
commands.append("sudo python ovxctl.py -n connectLink 2 00:a4:23:05:00:00:00:02 1 00:a4:23:05:00:00:00:03 3 spf 1")
commands.append("sudo python ovxctl.py -n connectLink 2 00:a4:23:05:00:00:00:02 2 00:a4:23:05:00:00:00:04 3 spf 1")
commands.append("sudo python ovxctl.py -n connectLink 2 00:a4:23:05:00:00:00:05 1 00:a4:23:05:00:00:00:06 3 spf 1")
commands.append("sudo python ovxctl.py -n connectLink 2 00:a4:23:05:00:00:00:05 2 00:a4:23:05:00:00:00:07 3 spf 1")

commands.append("sudo python ovxctl.py -n startNetwork 2")

main()
