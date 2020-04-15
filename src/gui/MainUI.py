# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './MainUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.serverConfigWidget = QtWidgets.QWidget(MainWindow)
        self.serverConfigWidget.setObjectName("serverConfigWidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.serverConfigWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(360, 10, 431, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.serverSettingsLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.serverSettingsLayout.setContentsMargins(0, 0, 0, 0)
        self.serverSettingsLayout.setObjectName("serverSettingsLayout")
        self.ipLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.ipLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.ipLineEdit.setClearButtonEnabled(False)
        self.ipLineEdit.setObjectName("ipLineEdit")
        self.serverSettingsLayout.addWidget(self.ipLineEdit, 0, 0, 1, 1)
        self.portLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.portLineEdit.setObjectName("portLineEdit")
        self.serverSettingsLayout.addWidget(self.portLineEdit, 0, 1, 1, 1)
        self.openConnectionButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.openConnectionButton.setCheckable(False)
        self.openConnectionButton.setObjectName("openConnectionButton")
        self.serverSettingsLayout.addWidget(self.openConnectionButton, 0, 2, 1, 1)
        self.closeConnectionButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.closeConnectionButton.setCheckable(False)
        self.closeConnectionButton.setObjectName("closeConnectionButton")
        self.serverSettingsLayout.addWidget(self.closeConnectionButton, 1, 2, 1, 1)
        self.consoleViewTextEdit = QtWidgets.QTextEdit(self.serverConfigWidget)
        self.consoleViewTextEdit.setGeometry(QtCore.QRect(40, 300, 731, 271))
        self.consoleViewTextEdit.setObjectName("consoleViewTextEdit")
        MainWindow.setCentralWidget(self.serverConfigWidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ipLineEdit.setText(_translate("MainWindow", "127.0.0.1"))
        self.portLineEdit.setText(_translate("MainWindow", "5505"))
        self.openConnectionButton.setText(_translate("MainWindow", "OpenConnection"))
        self.closeConnectionButton.setText(_translate("MainWindow", "CloseConnection"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+W"))
