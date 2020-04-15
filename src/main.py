#!/usr/bin/python3
import time
import sys,os
from PyQt5.QtWidgets import QApplication, QMainWindow 
from gui.MainUI import Ui_MainWindow

from Utils.ServerManager import ServerThread

class AppWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.linkFunctionsToActions()

		self.tcpServerThread = None

	def linkFunctionsToActions(self):
		self.ui.openConnectionButton.clicked.connect(self.openConnection)
		self.ui.closeConnectionButton.clicked.connect(self.closeConnection)

	def closeConnection(self):
		print("Closing server ")
		if self.tcpServerThread:
			if self.tcpServerThread.isRunning():
				print("Thread in running...")
				self.tcpServerThread.closeAllTCPClient()
				self.tcpServerThread.tcpServer.close()
				self.tcpServerThread.exit()

	def openConnection(self):
		ipStr = self.ui.ipLineEdit.text()
		portInt = int(self.ui.portLineEdit.text())
		print("IP : ",ipStr, " | Port : ",portInt)

		if self.tcpServerThread is None:
			self.tcpServerThread = ServerThread(ipStr,portInt,self.ui.consoleViewTextEdit)
		else:
			del self.tcpServerThread
			self.tcpServerThread = ServerThread(ipStr,portInt,self.ui.consoleViewTextEdit)
		self.tcpServerThread.start()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = AppWindow()
	
	print(os.getpid())

	win.show()
	app.exec_()