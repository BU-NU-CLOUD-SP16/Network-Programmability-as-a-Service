#!/usr/bin python

import socket
import json
import threading
import sys
import Queue

sema_for_count = threading.Semaphore(1)
msg_queue = Queue.Queue(20)
ack_recv_queue = Queue.Queue(2)
ack_recv_count = 0

MASTER_PORT = 50000
OVX_RECEIVER_PORT = 49999


def get_ip_address():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]

class MasterReceiver(threading.Thread):
    def __init__(self, (client_conn, client_addr)):
        threading.Thread.__init__(self)
        self.client_conn = client_conn
        self.client_addr = client_addr
        self.size = 1024
        self.len_of_mac = 12

    def run(self):
        global msg_queue
        global ack_recv_queue
        global ack_recv_count
        global sema_for_count
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
                    if 'op' in data:
                        print("OP : " + str(data['op']))
                        if 'ADD' == data['op'] or 'DELETE' == data['op']:
                            print("Adding to queue")
                            msg_queue.put((self.client_addr, data), block=True, timeout=0.2)
                            print("Added to queue")
                        else:
                            sema_for_count.acquire()
                            if ack_recv_count == (len(ip_list) - 1):
                                ack_recv_count = 0
                                ack_recv_queue.put("COMPLETE", block=True, timeout=None)
                            else:
                                ack_recv_count += 1
                            sema_for_count.release()

                    if 'tenantId' in data:
                        print("TenantID : " + str(data['tenantId']))
                    if 'hostId' in data:
                        print("HostID : " + str(data['hostId']))


                except ValueError:
                    continue

            self.client_conn.close()
            break


class MasterSender(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global ip_list
        while True:
            data = msg_queue.get(True, None)
            recv_addr = data[0]
            msg = data[1]
            print("Received at sender : " + str(data))

            for ip in ip_list:
                if recv_addr != ip:
                    serv_addr = (ip, OVX_RECEIVER_PORT)
                    tcp_sock = None
                    try:
                        tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        tcp_sock.connect(serv_addr)
                        tcp_sock.sendto(json.dumps(msg), serv_addr)
                        tcp_sock.close()
                    except socket.error:
                        print("Error in socket")
                        if tcp_sock:
                            tcp_sock.close()

            recvd = ack_recv_queue.get(True, None)
            print("Got all acks")


class Master:
    def __init__(self, port):
        self.host = get_ip_address()
        self.port = port
        self.threads = list()
        self.tcp_sock = None

    def create_socket(self):
        try:
            self.tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.tcp_sock.bind((self.host, self.port))
            print("Bound to %s on %s" %(self.port, self.host))
            self.tcp_sock.listen(2)
        except socket.error:
            if self.tcp_sock:
                self.tcp_sock.close()
            print("Failure to open socket")
            sys.exit(1)

    def run(self):
        sender = MasterSender()
        sender.start()
        self.create_socket()
        while True:
            client = MasterReceiver(self.tcp_sock.accept())
            client.start()
            self.threads.append(client)

def main():
    if len(sys.argv) < 2:
        print("Usage : python publisher.py <IP list>")
        exit(1)

    global ip_list
    ip_list_file = sys.argv[1]
    with open(ip_list_file, 'r') as fp:
        ip_list = fp.readlines()

    master = Master(MASTER_PORT)
    master.run()

if __name__ == '__main__':
    main()

