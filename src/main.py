#!/usr/bin/python3
import time
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication, QMainWindow 
from gui.MainUI import Ui_MainWindow

from Utils.ServerManager import ServerThread


from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtGui import QPalette,QColor,QBrush
from PyQt5.QtCore import pyqtSignal

class Console(QPlainTextEdit):
    def __init__(self,parentWidget):
        super().__init__(parentWidget)

        self.document().setMaximumBlockCount(100)
        self.initPalette()

    def receivePacket(self,string):
        self.appendPlainText(string)

    def initPalette(self):
        palette = QPalette()
        brush = QBrush(QColor(115, 210, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush = QBrush(QColor(115, 210, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        brush = QBrush(QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        brush = QBrush(QColor(239, 235, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        self.setPalette(palette)

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.linkFunctionsToActions()

        self.tcpServerThread = None

        self.console = Console(self.ui.consoleParentWidget)

    def linkFunctionsToActions(self):
        self.ui.actionQuit.triggered.connect(quit)
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
            self.tcpServerThread = ServerThread(ipStr,portInt,self.console)
        else:
            del self.tcpServerThread
            self.tcpServerThread = ServerThread(ipStr,portInt,self.console)
        self.tcpServerThread.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = AppWindow()

    win.show()
    app.exec_()