from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

'''
Learnings

*Open Window
*Label
*Push Button
'''

# Clicking action testing


def clicked():
    print("CLicked")


def window():
    app = QApplication(sys.argv)

    # creating a Window[Size  & Title]
    win = QMainWindow()
    win.setGeometry(300, 300, 400, 400)
    win.setWindowTitle("Sai Prasanth V")

    # creating Label[Name , Size]
    label = QtWidgets.QLabel(win)
    label.setText('My 1st Label')
    label.move(40, 40)

    # creating Push button [Name , Action]
    b1 = QtWidgets.QPushButton(win)
    b1.setText('Click hear')
    b1.clicked.connect(clicked)

    # Displaying Window
    win.show()

    # Closing Window
    sys.exit(app.exec())


window()
