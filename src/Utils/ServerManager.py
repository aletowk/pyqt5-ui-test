from PyQt5.QtCore import QThread
from PyQt5.QtNetwork import QHostAddress, QTcpServer

class ServerThread(QThread):
	def __init__(self,ip,port,textEditCSView):
		super().__init__()
		self.tcpServer = QTcpServer()
		self.clientList = []
		address = QHostAddress(ip)
		if not self.tcpServer.listen(address, port):
			print("cant listen!")
			self.tcpServer.close()
			return
		self.tcpServer.newConnection.connect(self.addConnection)
		self.console = textEditCSView
	
	def run(self):
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
		self.console.append(str(readData,encoding='ascii'))
		clientConnection.write(readData)

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