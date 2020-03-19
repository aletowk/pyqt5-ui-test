import socket
import struct
import sys

class ServerManager():
	"""docstring for ServerManager"""
	def __init__(self,host,port,buffSize):
		self.host = host
		self.port = port
		self.bufferSize = buffSize
		self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.connectionArray = []
	
	def open(self):
		try:
			self.server.bind((self.host, self.port))
			self.server.listen(1)
			conn, addr = self.server.accept()
			print("Connection from ",conn);
			self.connectionArray.append(conn);
		except:
			print("Execption : ",sys.exc_info()[0])
	
	def close(self):
		for el in self.connectionArray:
			el.close();

	def fromByteToArray(byteArr):
		toReturn = []
		for el in byteArr:
			print("Elem is ",el)
			toReturn.append(struct.unpack('B',el)[0])
		return toReturn