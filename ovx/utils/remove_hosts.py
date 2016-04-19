from pymongo import MongoClient
import os

len_of_mac = 12

def insert_colons_in_string(inp_str):
    return (':'.join(inp_str[i] +
                     inp_str[i+1]
                     for i in xrange(0, len(inp_str), 2)))

def convert_mac_format(mac):
    hex_value = str(hex(int(mac)))
    hex_value = hex_value.replace("0x", "")
    prefix_string = "0" * (len_of_mac - len(hex_value))
    hex_value = prefix_string + hex_value

    return insert_colons_in_string(hex_value)

def get_host_id(tenantId, mac):
    list_of_host_macs = set()
    is_tenant_present = False
    connection = MongoClient('mongodb://localhost:27017/')
    db = connection['OVX']
    collection = db['VNET']
    cursor = collection.find({'tenantId' : tenantId}, {'hosts' : 1})
    obj = next(cursor, None)

    if obj is not None:
    	is_tenant_present = True
        hosts = obj['hosts']
        for host in hosts:
            if 'mac' in host:
                mac_addr = host['mac']
                if mac == convert_mac_format(mac_addr):
                    return host['hostId']
        return -1

def disconnect_host(tenantId, hostId):
    commands=[]
    commands.append("sudo python ovxctl.py -n stopNetwork "+str(tenantId))
    commands.append("sudo python ovxctl.py -n disconnectHost "+str(tenantId)+" "+str(hostId))
    commands.append("sudo python ovxctl.py -n startNetwork "+str(tenantId))
    os.chdir("/home/ovx/OpenVirteX/utils")
    for c in commands: 
	print os.popen(c).read()

f = open('remove_hosts.txt')
lines = f.readlines()
f.close()
line =[]
for i in lines:
    line.append(i.split())

for i in line:
    disconnect_host(int(i[0]),get_host_id(int(i[0]),i[1]))

