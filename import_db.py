#!/usr/bin/python
import json
import argparse
import os

commands = list()
len_of_mac = 12
command_beginning = "sudo python ovxctl.py -n "


def main():
    os.chdir("~/OpenVirteX/utils")
    for c in commands:
        tmp = os.popen(c).read()
        print tmp

# Insert colon into the string to make it a proper format
def insert_colons_in_string(inp_str):
    return (':'.join(inp_str[i] +
                     inp_str[i+1]
                     for i in xrange(0, len(inp_str), 2)))


# Convert the integer value of MAC to its hexadecimal value in appropriate format
def convert_mac_format(mac):
    hex_value = str(hex(int(mac)))
    hex_value = hex_value.replace("0x", "")
    prefix_string = "0" * (len_of_mac - len(hex_value))
    hex_value = prefix_string + hex_value

    return insert_colons_in_string(hex_value)


# Convert the integer value of DPID to its hexadecimal value in appropriate format
def convert_dpid_format(dpid):
    hex_value = str(hex(int(dpid)))
    hex_value = hex_value.replace("0x", "00")
    return insert_colons_in_string(hex_value)



parser = argparse.ArgumentParser(description="Update OVX database")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("inp", help="input file")

args = parser.parse_args()

with open(args.inp, 'r') as fp:
    for line in fp.readlines():
        json_data = json.loads(line)

        tenantId = json_data['tenantId']

        stop_network = command_beginning + "stopNetwork " + str(tenantId)
        commands.append(stop_network)

        hosts = json_data['hosts']
        for host in hosts:
            dpid = convert_dpid_format(host['vdpid']['$numberLong'])
            port = host['vport']
            mac = convert_mac_format(host['mac']['$numberLong'])

            cmd = command_beginning + " connectHost " +\
                  str(tenantId) +\
                  " " +\
                  str(dpid) +\
                  " " +\
                  str(port) +\
                  " " + str(mac)
            commands.append(cmd)

        start_network = command_beginning + "startNetwork " + str(tenantId)
        commands.append(start_network)

main()