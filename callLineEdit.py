import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QApplication

from layout import *

class Myform(QDialog):

    def __init__(self):
        super().__init__()
        #self.ui = Ui_Dialog()
        #self.ui.setupUi(self)
        self.ui = uic.loadUi("layout.ui", self)
        self.ui.ButtonClickMe.clicked.connect(self.dispmessage)
        self.show()


    def dispmessage(self):
        self.ui.label.setText("hejka pokaz go " + self.ui.lineEditName.text())

if  __name__ =="__main__":
    app = QApplication(sys.argv)
    window = Myform()
    window.show()
    sys.exit(app.exec())