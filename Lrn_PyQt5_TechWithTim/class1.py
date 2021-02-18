from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

'''
Learnings

*Class
*Init UI
*Label adjust size
'''


class MyWindow(QMainWindow):

    # creating a Window[Size  & Title]
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle("Sai Prasanth V")
        self.initUI()

    def initUI(self):

        # creating Label[Name , Size]
        self.label = QtWidgets.QLabel(self)
        self.label.setText('My 1st Label')
        self.label.move(80, 80)

        # creating Push button [Name , Action]
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText('Click hear')
        self.b1.clicked.connect(self.clicked)

    # Clicking action testing
    def clicked(self):
        self.label.setText('CLICKED .....................aa')
        self.update()

    # Auto Lable size adjustment
    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)

    win = MyWindow()

    # Displaying Window
    win.show()

    # Closing Window
    sys.exit(app.exec())


window()
