import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from pupa import Ui_MainWindow


class abra(QtWidgets.QMainWindow):
    def __init__(self):
        super(abra, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
