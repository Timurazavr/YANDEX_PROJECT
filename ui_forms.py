from PyQt6 import QtCore, QtGui, QtWidgets
from core import MineField


class UiMain:
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
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, -10, 411, 71))
        self.label_2.setObjectName("label_2")
        self.setCentralWidget(self.centralwidget)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Сапёр"))
        self.label.setText(_translate("MainWindow", "Сапёр PRO"))
        self.startButton.setText(_translate("MainWindow", "Начать"))
        self.label_2.setText(
            _translate(
                "MainWindow",
                "Версия игры: beta, просто основа игры, без нормального оформления",
            )
        )

        QtCore.QMetaObject.connectSlotsByName(self)

        self.startButton.clicked.connect(self.setupUiStart)


class UiStartMenu:
    def setupUiStart(self):
        font = QtGui.QFont()
        font.setPointSize(20)
        self.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 330, 701, 261))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton.setFont(font)
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 80, 271, 161))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(710, 80, 271, 161))
        self.pushButton_3.setObjectName("pushButton_3")
        self.setCentralWidget(self.centralwidget)

        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("MainWindow", "Играть"))
        self.pushButton_2.setText(_translate("MainWindow", "Смена дизайна"))
        self.pushButton_3.setText(_translate("MainWindow", "Аналитика игр"))

        QtCore.QMetaObject.connectSlotsByName(self)

        self.pushButton.clicked.connect(self.setupUiSetupGame)


class UiSetupGame:
    def setupUiSetupGame(self):
        font = QtGui.QFont()
        font.setPointSize(20)
        self.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 0, 371, 81))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 80, 291, 111))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 200, 291, 111))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 320, 291, 111))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(340, 440, 291, 111))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(340, 560, 291, 101))
        self.pushButton_5.setObjectName("pushButton_5")
        self.setCentralWidget(self.centralwidget)

        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "Режим игры:"))
        self.pushButton.setText(_translate("MainWindow", "Простой"))
        self.pushButton_2.setText(_translate("MainWindow", "Средний"))
        self.pushButton_3.setText(_translate("MainWindow", "Сложный"))
        self.pushButton_4.setText(_translate("MainWindow", "Эксперт"))
        self.pushButton_5.setText(_translate("MainWindow", "Настраиваемый"))

        QtCore.QMetaObject.connectSlotsByName(self)

        self.pushButton.clicked.connect(self.setupUiGame)


class UiGame:
    def setupUiGame(self):
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 60, 781, 571))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.setCentralWidget(self.centralwidget)

        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("MainWindow", "Выход"))

        QtCore.QMetaObject.connectSlotsByName(self)

        self.minefield = 0
        for i in range(5):
            for j in range(5):
                x = QtWidgets.QPushButton()
                x.coord = (i, j)
                self.gridLayout.addWidget(x, i, j)
                x.clicked.connect(self.clicked_item)


class GameLogic:
    def clicked_item(self):
        obj = self.sender()
        if not self.minefield:
            self.minefield = MineField(5, 5, 7, obj.coord)
        if obj.text() == "":
            self.minefield.open(*obj.coord)
            for i in range(5):
                for j in range(5):
                    self.gridLayout.itemAtPosition(i, j).widget().setText(
                        self.minefield.visual_field[i][j]
                    )
