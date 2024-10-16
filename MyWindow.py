import sys
from PyQt5 import QtWidgets, QtCore
import datetime

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel()
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # update every 1 second

    def update_time(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.label.setText(current_time)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Current Time")
    window.resize(300, 100)
    window.show()
    sys.exit(app.exec_())