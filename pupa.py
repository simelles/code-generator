import os
from time import sleep

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1000, 500)
        MainWindow.setStyleSheet("background-color: #22222e;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.clicked.connect(self.btn2_click)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 50, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("background-color: #FFFFFF;\n"
                                        "border: 2px solid #fffff;\n"
                                        "border-radius: 30;\n"
                                        "color: #00000;\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.clicked.connect(self.btn3_click)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 150, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: #FFFFFF;\n"
                                        "border: 2px solid #fffff;\n"
                                        "border-radius: 30;\n"
                                        "color: #00000;\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "")
        self.pushButton_3.setObjectName("pushButton_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(0, 100, 207, 34))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet("background-color: #FFFFFF;\n"
                                    "border: 2px solid #fffff;\n"
                                    "border-radius: 30;\n"
                                    "color: #00000;\n"
                                    "\n"
                                    "\n"
                                    "\n"
                                    "")
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContents)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(265, 71, 731, 431))
        self.listWidget.setStyleSheet("background-color: #FFFFFF;\n"
                                      "border: 2px solid #fffff;\n"
                                      "border-radius: 30;\n"
                                      "color: #00000;\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "")
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1011, 501))
        self.label.setText("")
        path = os.path.dirname(os.path.abspath(r'D:\Python\xak_24.11.22\img\1o 1.png'))
        self.label.setPixmap(QtGui.QPixmap(os.path.join(path, '1o 1.png')))
        self.label.setObjectName("label")
        self.label.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.comboBox.raise_()
        self.listWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "i0 GENERATOR"))
        self.pushButton_2.setText(_translate("MainWindow", "Запись голоса"))
        self.pushButton_3.setText(_translate("MainWindow", "Запуск"))
        self.comboBox.setItemText(0, _translate("MainWindow", "C++                           "))
        self.comboBox.setItemText(1, _translate("MainWindow", "Python"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Java Script"))

    def btn3_click(self):
        choice = self.comboBox.currentIndex()
        if choice == 0:
            os.startfile(r'D:\Python\xak_24.11.22\dist\main_cpp\main_cpp.exe')
            sleep(2)
            if os.path.exists(r'D:\Python\xak_24.11.22\cpp\test.cpp'):
                with open(r'D:\Python\xak_24.11.22\cpp\test.cpp', 'r', encoding='UTF-8') as file:
                    for i in file:
                        self.listWidget.addItem(i)

        elif choice == 1:
            os.startfile(r'D:\Python\xak_24.11.22\dist\main\main.exe')
            sleep(2)
            if os.path.exists(r'D:\Python\xak_24.11.22\py\test.py'):
                with open(r'D:\Python\xak_24.11.22\py\test.py', 'r', encoding='UTF-8') as file:
                    for i in file:
                        self.listWidget.addItem(i)
        else:
            os.startfile(r'D:\Python\xak_24.11.22\dist\main_js\main_js.exe')
            sleep(2)
            if os.path.exists(r'D:\Python\xak_24.11.22\js\test.js'):
                with open(r'D:\Python\xak_24.11.22\js\test.js', 'r', encoding='UTF-8') as file:
                    for i in file:
                        self.listWidget.addItem(i)

    def btn2_click(self):
        os.startfile(r'D:\Python\xak_24.11.22\dist\speech_rec\speech_rec.exe')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
