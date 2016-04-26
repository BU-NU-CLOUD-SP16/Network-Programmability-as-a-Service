
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, hmac


class PKDF:
	def __init__(self,password,length):
		self.password=password
		self.length=length		

	def genKeyPKDF(self):
		backend=default_backend()
		salt=os.urandom(256)
		passW=str(self.password).encode()
		kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),length=self.length,salt=salt,iterations=100000,backend=backend)
		self.key=kdf.derive(passW)
		return self.key

	def verifyPKDFkey(self,key):
		passW=str(self.password).encode()
		kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),length=256,salt=salt,iterations=100000,backend=backend)
		kdf.verify(passW, key)
	
	def writeKey(self,filename):		
		f=open(filename,"w")
		f.write(self.key)

	def loadKey(self,filename):
		f=open(filename,"r")
		m=f.read()
		return m

if __name__=="__main__":
	hmacObj=PKDF('HmacPassword',256)
	hmacObj.genKeyPKDF()
	hmacObj.writeKey("hmacKey")
	print("generate hmac key of size "+str(len(hmacObj.key)))
	encObj=PKDF('EncryptionPassword',32)
	encObj.genKeyPKDF()
	encObj.writeKey("encKey")
	print("generate encryption key of size "+str(len(encObj.key)))
