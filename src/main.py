import sys
from PyQt5.QtWidgets import QDialog, QApplication
from gui.MainUI import Ui_MainWindow
from PyQt5 import uic

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()  


def quitAction():
	sys.exit(app.exec_())

app = QApplication(sys.argv)

window = uic.loadUi("./gui/MainUI.ui")
window.actionQuit.triggered.connect(quitAction)


window.show()

sys.exit(app.exec_())