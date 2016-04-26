#!/usr/bin/python

import os, sys 

cmd = "sudo kill -9 $(ps aux | grep ovx_receiver.py | grep -v \"grep\" | awk '{print $2}')"

os.system(cmd)
