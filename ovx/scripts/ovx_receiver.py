#!/usr/bin python

import socket
import json
import threading
import sys
from db_util import DBUtil

OVX_RECEIVER_PORT = 49999
MASTER_PORT = 50000
central_server_ip = None

class Client(threading.Thread):
    def __init__(self, (client_conn, client_addr)):
        threading.Thread.__init__(self)
        self.client_conn = client_conn
        self.client_addr = client_addr
        self.size = 1024
        #self.len_of_mac = 12
        #self.command_beginning = "sudo python ovxctl.py -n "
        #self.ovx_dir = "/home/ubuntu/OpenVirteX/utils"

    def run(self):
        global central_server_ip
        while True:
            data = None
            try:
                data = self.client_conn.recv(self.size)
            except socket.error, e:
                print(e.message)

            if data is not None:
                try:
                    data = json.loads(data)
                    print("Received : " + str(data))
                    db_util = DBUtil()
                    db_util.update_database(data)
                except ValueError:
                    continue

                serv_addr = (central_server_ip, MASTER_PORT)
                tcp_sock = None
                msg = {'op' : 'ACK'}
                try:
                    tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    tcp_sock.connect(serv_addr)
                    tcp_sock.sendto(json.dumps(msg), serv_addr)
                    tcp_sock.close()
                except socket.error:
                    print("Error in socket")
                    if tcp_sock:
                        tcp_sock.close()

                continue

            self.client_conn.close()
            break
    '''
    def update_database(self, data):
        op = data['op']
        content = data['data']
        tenantId = content['tenantId']

        commands = list()
        stop_network = self.command_beginning + " stopNetwork " + str(tenantId)
        commands.append(stop_network)

        command = ''

        if op == 'ADD':
            switchId = content['switchId']
            port = content['port']
            mac = content['mac']
            command = self.command_beginning + \
                      " connectHost " + \
                      str(tenantId) + " " + \
                      str(switchId) + " " + \
                      str(port) + " " + \
                      str(mac)
        else:
            command = self.command_beginning + \
                      " disconnectHost " + \
                      str(tenantId) + " " + \
                      str(content['hostId'])

        commands.append(command)

        start_network = self.command_beginning + "startNetwork " + str(content['tenantId'])
        commands.append(start_network)

        os.chdir(self.ovx_dir)
        for cmd in commands:
            tmp = os.popen(cmd).read()
            print(tmp)

    '''

class Receiver:
    def __init__(self, port):
        self.host = self.get_ip_address()
        self.port = port
        self.threads = list()
        self.tcp_sock = None
        self.semaphore = threading.Semaphore(1)

    def get_ip_address(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]


    def create_socket(self):
        try:
            self.tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.tcp_sock.bind((self.host, self.port))
            self.tcp_sock.listen(2)
        except socket.error:
            if self.tcp_sock:
                self.tcp_sock.close()
            print("Failure to open socket")
            sys.exit(1)

    def run(self):
        self.create_socket()
        while True:
            client = Client(self.tcp_sock.accept())
            client.start()
            self.threads.append(client)

def main():
    if len(sys.argv) < 2:
        print("Usage : python ovx_receiver.py <serverIP>")
        exit(1)

    global central_server_ip
    central_server_ip = sys.argv[1]
    receiver = Receiver(OVX_RECEIVER_PORT)
    receiver.run()

if __name__ == '__main__':
    main()

