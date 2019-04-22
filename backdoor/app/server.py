from PyQt5 import QtGui, QtCore, QtWidgets
import sys
import os
from PyQt5.QtMultimedia import QSound
from server import Ui_Frame

class server(Ui_Frame):
    def __init__(self, w):
        self.setupUi(w)

def main():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.    prog = server(w)
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main() 