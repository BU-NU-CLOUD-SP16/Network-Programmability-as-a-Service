#!/usr/bin/python

import socket
import threading
import re
import Queue
from socketClass import ClientSocket,ServerSocket,SSLClientSocket,SSLServerSocket

#instruction_queue=list()
msgId=0
data_dict=dict()
class CentralServer:
	
	def __init__(self,list_ip):
		self.sock=ServerSocket()
		self.sock.bindTo("127.0.0.1",50000)
		self.sock.limitListenersTo(4)	
		self.semaphore = threading.Semaphore(1)
		threading.Thread.__init__(self)
		self.ip_dict=dict()
		self.ip_list=list_ip
		for ip in ip_dict.keys():
			c=ClientSocket()
			c.connect(ip,49999)
			self.ip_dict[str(ip)]=c

	
	def createThread(self):
		while True:
			sockObj,ip=self.sock.acceptConnection()
			self.ip_dict[str(ip)]=sockObj
			self.tReciever=ThreadedReciever(sockObj,ip,self.semaphore,self.ip_dict)
			self.tReciever.start()
		#assuming somehow threads have been created and 
		# and there is a dict generated	
	def start(self):
		
		createThread()
		
		


class ThreadedReciever(threading.Thread):
	def __init__(self,sockObj,ip,sema,ip_dict):
		self.clientSocket=sockObj
		self.ip_addr=ip
		self.semaphore=sema
		#self.instruction_queue=list()
		self.ip_dict=ip_dict
		self.data_dict=dict()
		
	def sendMsg(self,sockObj,msg):
		try:
			sockObj.sendall(message)
			
		except Exception as e:
			print(e)
			sys.exit()

	def recvMsg(self):
		while True:
			data=self.clientSocket.recv(4096)
			if len(data) == 0:
				return
			else:
				break
		return data

	def appendInstruction(self,data):
		print("Recieved instruction from "+self.ip_addr+" :"+data
		self.semaphore.acquire()
		#self.instruction_queue.append(data)
		data_dict[str(msgId)]=data
		self.semaphore.release()

	def sendOP(self,data,msgId):
		#send the data with the message ID
		data1=data+msgID
		for ip in self.ip_dict.keys():
			if ip!=self.ip_addr:
				sendMsg(ip_dict[ip],data1)
		
	def removeInstruction(self,msgID):
		self.semaphore.acquire()
		#self.instruction_queue.append(data)
		del data_dict[str(msgId)]
		self.semaphore.release()

	def run(self):
		
		while True:
			data=None
			data=self.clientSocket.recvMsg()
			if data is not None:
				if "op" in data:
					oper=data["op"]

					self.appendInstruction(data)
					msgID+=1
					sendOP(data,msgID)

				elif ACK in data:
					#somehow extract msgId from this msg		
					self.removeInstruction(msgID)	
				
											
			
if __name__="__main__":
	list_ip=["192.168.99.102","192.168.99.104","192.168.99.103"]
	c=CentralServer(list_ip)
	c.start()
