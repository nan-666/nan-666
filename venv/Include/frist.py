
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
class Hello(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Hello")
        self.resize(300,300)
        lable = QLabel()
        lable.setText("hello")
        vbox = QVBoxLayout()
        vbox.addWidget(lable)
        self.setLayout(vbox)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    hello = Hello()
    hello.show()
    sys.exit(app.exec_())
