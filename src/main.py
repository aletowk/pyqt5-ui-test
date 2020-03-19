#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow 
from PyQt5.QtCore import QThread, QByteArray, QDataStream, QIODevice
from gui.MainUI import Ui_MainWindow

from PyQt5.QtNetwork import QHostAddress, QTcpServer

from Utils.ServerManager import ServerManager

class AppWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.linkFunctionsToActions()


		self.show()

	def quitAction(self):
		sys.exit(app.exec_())

	def linkFunctionsToActions(self):
		self.ui.actionQuit.triggered.connect(self.quitAction)
		self.ui.openConnectionButton.clicked.connect(self.openConnection)

	def openConnection(self):
		print("Pushed")
		ipStr = self.ui.ipLineEdit.text()
		portInt = int(self.ui.portLineEdit.text())
		print("IP : ",ipStr, " | Port : ",portInt)

		self.thread = ServerThread(ipStr,portInt)
		self.thread.finished.connect(app.exit)
		self.thread.start()
		

class ServerThread(QThread):
	def __init__(self,ip,port):
		super().__init__()
		self.tcpServer = QTcpServer(self)
		address = QHostAddress(ip)
		if not self.tcpServer.listen(address, port):
			print("cant listen!")
			self.close()
			return
		self.tcpServer.newConnection.connect(self.dealCommunication)

	def __del__(self):
		self.wait()

	def dealCommunication(self):
		# Get a QTcpSocket from the QTcpServer
		clientConnection = self.tcpServer.nextPendingConnection()
		blockToWrite = self.writeMessageToData("Bye Bye")
		# wait until the connection is ready to read
		clientConnection.waitForReadyRead()
		# read incomming data
		instr = clientConnection.readAll()
		# in this case we print to the terminal could update text of a widget if we wanted.
		print(str(instr, encoding='ascii'))
		# get the connection ready for clean up
		clientConnection.disconnected.connect(clientConnection.deleteLater)
		# now send the QByteArray.
		clientConnection.write(blockToWrite)
		# now disconnect connection.
		clientConnection.disconnectFromHost()

	def writeMessageToData(self,message):
		# instantiate a QByteArray
		block = QByteArray()
		# QDataStream class provides serialization of binary data to a QIODevice
		out = QDataStream(block, QIODevice.ReadWrite)
		# We are using PyQt5 so set the QDataStream version accordingly.
		out.setVersion(QDataStream.Qt_5_0)
		out.writeUInt16(0)
		# this is the message we will send it could come from a widget.
		message = "Goodbye!"
		# get a byte array of the message encoded appropriately.
		message = bytes(message, encoding='ascii')
		# now use the QDataStream and write the byte array to it.
		out.writeString(message)
		out.device().seek(0)
		out.writeUInt16(block.size() - 2)
		return block		


if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = AppWindow()
	
	win.show()
	app.exec_()
	sys.exit(app.exec_())