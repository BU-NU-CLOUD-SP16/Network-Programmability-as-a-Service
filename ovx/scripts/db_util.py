from pymongo import MongoClient
import os

class DBUtil:
    def __init__(self):
        self.len_of_mac = 12
        self.command_beginning = "sudo python ovxctl.py -n "
        self.ovx_dir = "/home/ubuntu/OpenVirteX/utils"

    # Insert colon into the string to make it a proper format
    def insert_colons_in_string(self, inp_str):
        return (':'.join(inp_str[i] +
                         inp_str[i+1]
                         for i in xrange(0, len(inp_str), 2)))


    # Convert the integer value of MAC to its hexadecimal value in appropriate format
    def convert_mac_format(self, mac):
        hex_value = str(hex(int(mac)))
        hex_value = hex_value.replace("0x", "")
        prefix_string = "0" * (self.len_of_mac - len(hex_value))
        hex_value = prefix_string + hex_value

        return self.insert_colons_in_string(hex_value)


    # Convert the integer value of DPID to its hexadecimal value in appropriate format
    def convert_dpid_format(self, dpid):
        hex_value = str(hex(int(dpid)))
        hex_value = hex_value.replace("0x", "00")
        return self.insert_colons_in_string(hex_value)

    # Get the mac address of all the hosts for this tenant
    def get_all_hosts_for_tenant(self, tenantId):
        list_of_host_macs = dict()
        is_tenant_present = False
        connection = MongoClient('mongodb://localhost:27017/')
        db = connection['OVX']
        collection = db['VNET']

        cursor = collection.find({'tenantId' : tenantId}, {'hosts' : 1})
        obj = next(cursor, None)

        if obj is not None:
            is_tenant_present = True
            if 'hosts' in obj:
                hosts = obj['hosts']
                for host in hosts:
                    if 'mac' in host:
                        mac_addr = host['mac']
                        list_of_host_macs[self.convert_mac_format(mac_addr)] = host['hostId']

        return list_of_host_macs, is_tenant_present

    '''
    def update_database(self, data):
        #tenantId = data['tenantId']
        for tenantId, hosts in data.iteritems():
            connection = MongoClient('mongodb://localhost:27017/')
            db = connection['OVX']
            collection = db['VNET']

            cursor = collection.find({'tenantId' : tenantId})
            obj = next(cursor, None)

            if obj is not None:
                if 'hosts' in obj:
                    if cmp(hosts, obj['hosts']) == 0:
                        continue

                stop_network = self.command_beginning + " stopNetwork " + str(tenantId)
                os.chdir(self.ovx_dir)
                tmp = os.popen(stop_network).read()
                print(tmp)
                collection.update({'_id' : obj['_id']}, {'$set' : {'hosts' : hosts}})
                start_network = self.command_beginning + "startNetwork " + str(tenantId)
                os.chdir(self.ovx_dir)
                tmp = os.popen(start_network).read()
                print(tmp)





        receiver_hosts, is_tenant_present = self.get_all_hosts_for_tenant(tenantId)

        if not is_tenant_present:
            return

        sender_hosts = dict()
        for host in data['hosts']:
            sender_hosts[self.convert_mac_format(host['mac'])] = host

        #extra_in_sender = set(sender_hosts.keys()).difference(receiver_hosts.keys())
        #extra_in_receiver = set(receiver_hosts.keys()).difference(sender_hosts.keys())

        # Insert
        inserted = False
        for host in extra_in_sender:
            inserted = True
            print("Changed to : Inserted")
            self.update_hosts(tenantId, sender_hosts[host], self.operation['insert'])

        if not inserted:
            print("Not inserted. Deleting")
            for host in extra_in_receiver:
                self.update_hosts(tenantId, receiver_hosts[host], self.operation['delete'])


    def update_hosts(self, tenantId, host, op):
        commands = list()
        stop_network = self.command_beginning + " stopNetwork " + str(tenantId)
        commands.append(stop_network)

        command = ''

        if op == self.operation['insert']:
            dpid = self.convert_dpid_format(host['vdpid'])
            port = host['vport']
            mac = self.convert_mac_format(host['mac'])
            command = self.command_beginning + \
                      " connectHost " + \
                      str(tenantId) + " " + \
                      str(dpid) + " " + \
                      str(port) + " " + \
                      str(mac)
        else:
            command = self.command_beginning + \
                      " disconnectHost " + \
                      str(tenantId) + " " + \
                      str(host['hostId'])

        commands.append(command)

        start_network = self.command_beginning + "startNetwork " + str(tenantId)
        commands.append(start_network)

        os.chdir(self.ovx_dir)
        for cmd in commands:
            tmp = os.popen(cmd).read()
            print(tmp)

    '''
    def is_mac_exists(self, tenantId, mac):
        list_of_host_macs, is_tenant_present = self.get_all_hosts_for_tenant(tenantId)
        if is_tenant_present and mac in list_of_host_macs:
            return True, list_of_host_macs[mac]

        return False, None


    def update_database(self, data):
        op = data['op']
        content = data['data']
        tenantId = content['tenantId']
        mac = content['mac']

        commands = list()
        stop_network = self.command_beginning + " stopNetwork " + str(tenantId)
        #commands.append(stop_network)

        command = ''

        mac_exists, hostId = self.is_mac_exists(tenantId, mac)

        if op == 'ADD':
            if mac_exists:
                del commands
                return

            switchId = content['switchId']
            port = content['port']

            command = self.command_beginning + \
                      " connectHost " + \
                      str(tenantId) + " " + \
                      str(switchId) + " " + \
                      str(port) + " " + \
                      str(mac)
        else:
            if not mac_exists:
                del commands
                return

            command = self.command_beginning + \
                      " disconnectHost " + \
                      str(tenantId) + " " + \
                      str(hostId)

        commands.append(command)

        start_network = self.command_beginning + "startNetwork " + str(tenantId)
        #commands.append(start_network)

        os.chdir(self.ovx_dir)
        for cmd in commands:
            tmp = os.popen(cmd).read()
            print(tmp)

        del commands
