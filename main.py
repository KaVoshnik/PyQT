from PyQt5 import QtCore, QtWidgets
import MyWindow
import sys

class MyDialog (QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.myWidget = MyWindow.MyWindow()
        self.myWidget.vbox.setContentsMargins(0, 0, 0, 0) 
        self.button - QtWidgets.QPushButton("Изменить надпись") 
        mainBox = QtWidgets.QVBoxLayout ()
        mainBox.addWidget(self.myWidget)
        mainBox.addwidget (self.button)
        self.setLayout (mainBox)
        self.button.clicked. connect (self.on_clicked)

    def on_clicked(self):
        self.myWidget.label.setText ("Новая надпись") 
        self.button.setDisabled(True)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyDialog()
    window.setWindowTitle("Преимущество ООП-стиля")
    window.resize(300, 100)
    window.show()
    sys.exit(app.exec_())