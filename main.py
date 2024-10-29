import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from start_menu import StartMenu


class MainWin(QMainWindow):
    def setupUi(self):
        self.setObjectName("MainWindow")
        self.showMaximized()
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 130, 355, 136))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(50)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.startButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(250, 290, 355, 221))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Сапёр"))
        self.label.setText(_translate("MainWindow", "Сапёр PRO"))
        self.startButton.setText(_translate("MainWindow", "Начать"))

    def __init__(self):
        super().__init__()
        self.setupUi()
        self.startButton.clicked.connect(self.startmenu)

    def startmenu(self):
        StartMenu(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_form = MainWin()
    main_form.show()
    sys.exit(app.exec())