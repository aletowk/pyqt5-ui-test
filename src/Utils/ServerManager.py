from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtNetwork import QHostAddress, QTcpServer

class ServerThread(QThread):
	def __init__(self,ip,port,console):
		super().__init__()
		self.ip = ip
		self.port = port
		self.tcpServer = QTcpServer()
		self.clientList = []
		address = QHostAddress(self.ip)
		if not self.tcpServer.listen(address, self.port):
			print("cant listen!")
			self.tcpServer.close()
			return
		self.tcpServer.newConnection.connect(self.addConnection)
		self.receviedDataSignal =  pyqtSignal(str)
		# This generate error Attribue No attribute connect ! 
		# self.receviedDataSignal.connect(console.receivePacket)
	def run(self):
		self.tcpServer.moveToThread(self.thread())
		while True:
			for conn in self.clientList:
				self.echoConnection(conn)
		self.closeAllTCPClient()

	def addConnection(self):
		connectionToAdd = self.tcpServer.nextPendingConnection()
		self.clientList.append(connectionToAdd)

	def echoConnection(self,clientConnection):
		readData = self.readFromTCPSocket(clientConnection)
		print("[HOST] Received from ",clientConnection.localAddress().toString(),clientConnection.localPort())
		print(readData)
		# Add write to our console
		# self.receviedDataSignal.emit(readData)

	def readFromTCPSocket(self,tcpSocket):
		tcpSocket.waitForReadyRead()
		data = tcpSocket.readAll()
		return data

	def closeAllTCPClient(self):
		for conn in self.clientList:
			conn.disconnectFromHost()

	def readNewConnection(self):
		conn = self.tcpServer.nextPendingConnection()
		self.echoConnection(conn)