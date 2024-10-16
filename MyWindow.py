from PyQt5 import QtCore, QtWidgets
import sys
import datetime

class MyWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        x = datetime.datetime.now()
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel(x.strftime("%x"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.btnQuit = QtWidgets.QPushButton("&Закрыть")
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btnQuit)
        self.setLayout(self.vbox)
        self.btnQuit.clicked.connect(QtWidgets.qApp.quit)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Data time")
    window.resize(300, 70)
    window.show()
    sys.exit(app.exec_())
