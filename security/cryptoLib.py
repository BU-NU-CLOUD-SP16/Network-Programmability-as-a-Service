#!/usr/bin python


import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
'''
Usage
obj=PKDF('OVXpassword')
key=obj.genKeyPKDF()
#print key

hmObj1=Hmac('data1',key)
hmObj2=Hmac('data2',key)
#hm1=hmObj1.createHmac()
hm2=hmObj2.createHmac()
l=hmObj1.verifyHmac(hm2)
print l

'''



class AesCtr:
	def __init__(self):
		f=open("encKey","r")
		m=f.read()
		self.key=m
		#print("length of key is "+str(len(self.key)))
			
		self.backend = default_backend()

	def encryptData(self,dataS,iv):
		self.data=str(dataS).encode()
		self.iv=iv
		cipher = Cipher(algorithms.AES(self.key), modes.CTR(self.iv), backend=self.backend)
		encryptor = cipher.encryptor()
		self.encryptedData = encryptor.update(self.data) + encryptor.finalize()
		return self.encryptedData

	def decryptData(self,encryptedData,iv):
		self.iv=iv
		cipher = Cipher(algorithms.AES(self.key), modes.CTR(self.iv), backend=self.backend)
		decryptor = cipher.decryptor()
		self.unEncryptedData=decryptor.update(encryptedData) + decryptor.finalize()
		return self.unEncryptedData
	

class Hmac:
	def __init__(self,dataS,key):
		f=open("hmacKey","r")
		m=f.read()
		self.dataS=dataS	
		self.data=str(self.dataS).encode()
		self.key=m

	def createHmac(self):
		
		h = hmac.HMAC(self.key, hashes.SHA256(), backend=default_backend())
				
		h.update(self.data)
		self.hmac=h.finalize()
		return self.hmac

	def verifyHmac(self,hmac2):
		#hm=self.hmacFinalize
		#hy=bytes('data1')	
		d=self.data
		h = hmac.HMAC(self.key, hashes.SHA256(), backend=default_backend())
		h.update(d)
		try:
			h.verify(hmac2)
			return True
		except Exception as e:
			print(e)
			return False			
