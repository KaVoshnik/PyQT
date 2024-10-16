import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtWidgets import QMessageBox

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.time_label = QtWidgets.QLabel()
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)

        self.timer_label = QtWidgets.QLabel("Timer:")
        self.timer_input = QtWidgets.QSpinBox()
        self.timer_input.setRange(1, 3600)

        self.start_button = QtWidgets.QPushButton("Start")
        self.start_button.clicked.connect(self.start_timer)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.time_label)
        self.layout.addWidget(self.timer_label)
        self.layout.addWidget(self.timer_input)
        self.layout.addWidget(self.start_button)

        self.setLayout(self.layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_timeout)

        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.update_time)
        self.update_timer.start(1000)

    def start_timer(self):
        self.timer.start(self.timer_input.value() * 1000)  # convert seconds to milliseconds

    def timer_timeout(self):
        self.timer.stop()
        QMessageBox.information(self, "Timer", "Cool time")

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.time_label.setText(current_time)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Timer")
    window.resize(300, 200)
    window.show()
    sys.exit(app.exec_())