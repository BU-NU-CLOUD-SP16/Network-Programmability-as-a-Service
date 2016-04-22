#!/usr/bin python

import socket
import json
import threading
import sys
from db_util import DBUtil
from cryptoLib import AesCtr,Hmac


class Client(threading.Thread):
    def __init__(self, (client_conn, client_addr), sema):
        threading.Thread.__init__(self)
        self.client_conn = client_conn
        self.client_addr = client_addr
        self.size = 4096
        self.len_of_mac = 12
        self.sema = sema
		
		
    def run(self):
        while True:
            dataRaw = None
            try:
                dataRaw = self.client_conn.recv(self.size)
                iv,dataEnc,dataHmac=dataRaw.split("nonce")
				dataAuth=verHmac(dataEnc,dataHmac)
				if not dataAuth:
                    continue
				else:
					dataChecked=decrypt(dataEnc,iv)
            except socket.error, e:
                print(e.message)

            if dataRaw is not None:
                try:
                    data = json.loads(dataChecked)
                    print("Received : " + str(data))
                    dbutil = DBUtil()
                    self.sema.acquire()
                    dbutil.update_database(data)
                    self.sema.release()
                except ValueError:
                    continue

            self.client_conn.close()
            break
	def verHmac(dataHmac,dataEnc):
        hmObj1=Hmac(dataEnc)
        l=hmObj1.verifyHmac(dataHmac)
        return l
    def decrypt(dataEnc,iv):
        e2=AesCtr()
        unEnc=e2.decryptData(enc,iv)

		

class Receiver:
    def __init__(self,port):
        self.host ="127.0.0.1"
		#why not "127.0.0.1"
        self.port = port
        self.threads = list()
        self.udp_sock = None
        self.semaphore = threading.Semaphore(1)

    def get_ip_address(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]


    def create_socket(self):
        try:
            self.udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.udp_sock.bind((self.host, self.port))
            #self.udp_sock.listen(2)
        except socket.error:
            if self.udp_sock:
                self.udp_sock.close()
            print("Failure to open socket")
            sys.exit(1)

    def run(self):
        self.create_socket()
        while True:
            client = Client(self.udp_sock.accept(), self.semaphore)
            client.start()
            self.threads.append(client)

def main():
    receiver = Receiver(49999)
    receiver.run()

if __name__ == '__main__':
    main()

