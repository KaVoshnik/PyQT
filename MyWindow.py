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
        self.timer_input.setRange(1, 3600)  # 1-3600 seconds

        self.start_button = QtWidgets.QPushButton("Start")
        self.start_button.clicked.connect(self.start_timer)

        self.remaining_time_label = QtWidgets.QLabel("Remaining time: ")
        self.remaining_time_label.setAlignment(QtCore.Qt.AlignCenter)

        self.close_button = QtWidgets.QPushButton("Close")
        self.close_button.clicked.connect(self.close)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.time_label)
        self.layout.addWidget(self.timer_label)
        self.layout.addWidget(self.timer_input)
        self.layout.addWidget(self.start_button)
        self.layout.addWidget(self.remaining_time_label)
        self.layout.addWidget(self.close_button)

        self.setLayout(self.layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_timeout)

        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.update_time)
        self.update_timer.start(1000)  # update every 1 second

        self.remaining_time = 0

    def start_timer(self):
        self.remaining_time = self.timer_input.value()
        self.timer.start(1000)  # update every 1 second

    def timer_timeout(self):
        self.remaining_time -= 1
        self.remaining_time_label.setText(f"Remaining time: {self.remaining_time} seconds")
        if self.remaining_time <= 0:
            self.timer.stop()
            QMessageBox.information(self, "Timer", "Time's up!")

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.time_label.setText(current_time)

    def close(self):
        self.update_timer.stop()
        self.timer.stop()
        self.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Current Time")
    window.resize(300, 250)
    window.show()
    sys.exit(app.exec_())