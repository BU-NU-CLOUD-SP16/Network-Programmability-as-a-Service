#!/usr/bin python

import socket
import json
import os
from cryptoLib import AesCtr,Hmac

PORT = 49999


class MessageSender:
    def __init__(self,port):
		self.port=port
    def send_to_peers(self, active_ips, data):

        for peer_ip in active_ips:
            serv_addr = (peer_ip, PORT)
            udp_sock = None
            try:
                udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                data1=json.dumps(data)		
                
				enc_data,iv=encrypt(data1)
                hmac_data=findHmac(enc_data)
				data_final=iv+"nonce"+enc_data+"nonce"+hmac_data
                udp_sock.sendto(data_final, serv_addr)
                udp_sock.close()
            except Exception as e:
                print(e)
                udp_sock.close()
                



    def findHmac(data):
        hm=Hmac(data)
        return hm.createHmac()
        
    def encrypt(data):
        iv=os.urandom(16)
        e1=AesCtr()
        enc=e1.encryptData(data,iv)
		return [enc,iv]
        	