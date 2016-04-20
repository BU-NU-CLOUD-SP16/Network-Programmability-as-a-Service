#!/usr/bin python

import socket
import json


PORT = 49999


class MessageSender:
    def send_to_peers(self, active_ips, data):

        for peer_ip in active_ips:
            serv_addr = (peer_ip, PORT)
            tcp_sock = None
            try:
                tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                tcp_sock.connect(serv_addr)
                tcp_sock.sendto(json.dumps(data), serv_addr)
                tcp_sock.close()
            except socket.error:
                print("Error in socket")
                tcp_sock.close()

