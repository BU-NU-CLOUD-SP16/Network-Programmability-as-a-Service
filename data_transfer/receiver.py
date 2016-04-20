#!/usr/bin python

import socket
import json
#from nmap_util import get_active_ips

PORT = 49999

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def start_server():
    dest_addr = (get_ip_address(), 49999)
    tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_sock.bind(dest_addr)
    tcp_sock.listen(1)

    while True:
        data = None
        connection, client_addr = tcp_sock.accept()
        try:
            data = connection.recv(2048)
        except socket.error, e:
            print(e.message)

        if data is not None:
            data = json.loads(data)
            print("Received : " + str(data))
            if 'mydata' in data:
                print(data['mydata'])

        connection.close()


def main():
    active_ips = get_active_ips()
    start_server()

if __name__ == '__main__':
    main()

