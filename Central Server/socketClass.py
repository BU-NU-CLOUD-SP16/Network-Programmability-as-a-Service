#!/usr/bin python

import socket
import threading




class ClientSocket:

'''
usage 
c=ClientSocket()
c.connect("127.0.0.1",24566)
c.sendMsg("I am the message")
data=c.recvMsg()

'''


	def __init__(self):
		try :
			self.objSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			print "Socket Object Created"
		except Exception as e:
			print(e)
			sys.exit()
		return self.objSocket
	
	def connect(self,host_addr,port):
		host_addr=str(host_addr)
		port=int(port)
		try :
			self.objSocket.connect((host_addr , port))
			print "Connected to"+str(host_addr)+":"+str(port)
		except Exception as e:
			print(e)
			sys.exit()
	

	def sendMsg(self,msg):
		try:
			self.objSocket.sendall(message)
			
		except Exception as e:
			print(e)
			sys.exit()
	

	def recvMsg(self):
		while True:
			data=self.objSocket.recv(4096)
			if len(data) == 0:
				return
			else:
				break
		return data


class SSLClientSocket:

'''
usage 
c=SSLClientSocket()
c.connect("127.0.0.1",24566)
c.sendMsg("I am the message")
data=c.recvMsg()

'''
	def __init__(self):
		try :
			clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			self.objSocket = ssl.wrap_socket(clientSocket,ssl_version=ssl.PROTOCOL_TLSv1,certfile=None,server_side=False)
			
			print "SSL Socket Object Created"
		except Exception as e:
			print(e)
			sys.exit()
		return self.objSocket
	
	def connect(self,host_addr,port):
		host_addr=str(host_addr)
		port=int(port)
		try :
			self.objSocket.connect((host_addr , port))
			print "Connected to"+str(host_addr)+":"+str(port)
		except Exception as e:
			print(e)
			sys.exit()
	

	def sendMsg(self,msg):
		try:
			self.objSocket.sendall(message)
			
		except Exception as e:
			print(e)
			sys.exit()
	

	def recvMsg(self):
		while True:
			data=self.objSocket.recv(4096)
			if len(data) == 0:
				return
			else:
				break
		return data

class ServerSocket:

'''
usage 
c=ServerSocket()
c.bindTo("127.0.0.1",24566)
c.limitListentersTo(4)
c.run()

'''
	def __init__(self):
		
		self.threads = list()
		try :
			self.objSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			print "Socket Object Created"
		except Exception as e:
			print(e)
			sys.exit()
		return self.objSocket

	def bindTo(self,server_ip,server_port):
		
		try :
			self.objSocket.bind((str(server_ip),int(server_port)))
			print "Socket binded to"+str(server_ip)+":"+str(server_port)
		except Exception as e:
			print(e)
			sys.exit()

	def limitListentersTo(numConnections):
		numConnections=int(numConnections)
		try:
			self.objSocket.listen(numConnections)

		except Exception as e:
			print(e)
			sys.exit()


	
	def run(self):
		try:

			while True:
				clientConnSocket,clientAddress=self.objSocket.accept()

				client = ThreadedReceiverClient(clientConnSocket,clientAddress)
				client.start()
				self.threads.append(client)
		except Exception as e:
			print(e)
			sys.exit()
			
			
			
class SSLServerSocket:

'''
usage 
c=SSLServerSocket()
c.bindTo("127.0.0.1",24566)
c.limitListentersTo(4)
c.run()

'''
	def __init__(self):
		
		self.threads = list()
		try :
			serverSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			self.objSocket = ssl.wrap_socket(serverSocket,ssl_version=ssl.PROTOCOL_TLSv1,certfile=None,server_side=True)
			print "Socket Object Created"
		except Exception as e:
			print(e)
			sys.exit()
		return self.objSocket

	def bindTo(self,server_ip,server_port):
		
		try :
			self.objSocket.bind((str(server_ip),int(server_port)))
			print "Socket binded to"+str(server_ip)+":"+str(server_port)
		except Exception as e:
			print(e)
			sys.exit()

	def limitListentersTo(numConnections):
		numConnections=int(numConnections)
		try:
			self.objSocket.listen(numConnections)

		except Exception as e:
			print(e)
			sys.exit()


	
	def run(self):
		try:

			while True:
				clientConnSocket,clientAddress=self.objSocket.accept()

				client = ThreadedReceiverClient(clientConnSocket,clientAddress)
				client.start()
				self.threads.append(client)
		except Exception as e:
			print(e)
			sys.exit()


class ThreadedReceiverClient(threading.Thread):
	
	def __init__(self,clientConnSocket,clientAddress):	
		self.semaphore = threading.Semaphore(1)
		threading.Thread.__init__(self)
		self.objSocket = clientConnSocket
		self.client_addr = clientAddress
		

	def sendMsg(self,msg):
		try:
			self.objSocket.sendall(message)
			
		except Exception as e:
			print(e)
			sys.exit()

	def recvMsg(self):
		while True:
			data=self.objSocket.recv(4096)
			if len(data) == 0:
				return
			else:
				break
		return data

	
	