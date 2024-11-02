from PyQt6 import QtCore, QtGui, QtWidgets
from datetime import datetime
from core import MineField, settings
from db import write_db, read_db, write_txt, read_txt


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
                "Версия игры: release, рабочий интерфейс, без нормального оформления",
            )
        )

        QtCore.QMetaObject.connectSlotsByName(self)

        self.ingame = False
        self.startButton.clicked.connect(self.setupUiStart)


class UiStartMenu:
    def setupUiStart(self):
        self.ingame = False
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

        self.pushButton_3.clicked.connect(self.setupUiStat)
        try:
            del self.minefield
        except:
            pass


class UiStat:
    def setupUiStat(self):
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(910, 50, 161, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 60, 111, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(480, 60, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(130, 180, 871, 531))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.setCentralWidget(self.centralwidget)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Статистика"))
        self.pushButton_2.setText(_translate("MainWindow", "Назад"))
        self.label.setText(_translate("MainWindow", "Сохранения:"))

        QtCore.QMetaObject.connectSlotsByName(self)

        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(
            ("Имя сохранения", "Дата сохранения", "Нажмите для загрузки")
        )
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(read_db()):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                if isinstance(elem, str):
                    obj = QtWidgets.QTableWidgetItem(elem)
                    self.tableWidget.setItem(i, j, obj)
                else:
                    obj = QtWidgets.QPushButton("+", self.tableWidget)
                    obj.field = elem
                    obj.clicked.connect(self.down_save)
                    self.tableWidget.setCellWidget(i, j, obj)
        self.tableWidget.resizeColumnsToContents()

        self.pushButton_2.clicked.connect(self.setupUiStart)
        self.pushButton.clicked.connect(self.run_stat)

    def down_save(self):
        self.minefield = self.sender().field
        self.settings = (
            self.minefield.cols,
            self.minefield.rows,
            sum(i.count("x") for i in self.minefield.field),
        )
        self.setupUiGame(fl=False)

    def run_stat(self):
        StatisticWindow(self).show()


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
        self.pushButton_2.clicked.connect(self.setupUiGame)
        self.pushButton_3.clicked.connect(self.setupUiGame)
        self.pushButton_4.clicked.connect(self.setupUiGame)
        self.pushButton_5.clicked.connect(self.dial)

    def dial(self):
        obj = DialogWindow(self)
        obj.show()


class UiGame:
    def setupUiGame(self, *args, fl=True):
        write_txt("all")
        self.slsh = self.sender().text()
        if self.sender().text() in settings:
            self.settings = settings[self.sender().text()]
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 10, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lcdNumber = QtWidgets.QLCDNumber(parent=self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(260, 0, 111, 51))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(parent=self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(450, 0, 111, 51))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber.display(self.settings[2])
        self.btns = [[] for _ in range(self.settings[1])]
        if fl:
            self.minefield = 0
        self.btn_size = min(
            (self.geometry().height() - 100) // self.settings[1],
            (self.geometry().width() - 100) // self.settings[0],
        )
        for i in range(self.settings[1]):
            for j in range(self.settings[0]):
                x = QtWidgets.QPushButton(parent=self.centralwidget)
                x.setGeometry(
                    QtCore.QRect(
                        50 + j * self.btn_size,
                        50 + i * self.btn_size,
                        self.btn_size,
                        self.btn_size,
                    )
                )
                x.coord = (i, j)
                x.clicked.connect(self.clicked_item)
                self.btns[i].append(x)
        self.btn_geometry = QtCore.QRect(
            50, 50, self.settings[0] * self.btn_size, self.settings[1] * self.btn_size
        )

        if not fl:
            self.ingame = True
            self.lcdNumber.display(
                self.settings[2]
                - sum(i.count("F") for i in self.minefield.visual_field)
            )
            result = False
            for i in range(self.settings[1]):
                if "x" in self.minefield.visual_field[i]:
                    result = True
                    break
            for i in range(self.settings[1]):
                for j in range(self.settings[0]):
                    obj_b = self.btns[i][j]
                    if result or self.minefield.visual_field[i][j] == "0":
                        obj_b.setEnabled(False)
                    if self.minefield.visual_field[i][j] != "0":
                        obj_b.setText(self.minefield.visual_field[i][j])
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)

        self.setCentralWidget(self.centralwidget)
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("MainWindow", "Выход"))
        self.pushButton_2.setText(_translate("MainWindow", "Сохранить"))
        QtCore.QMetaObject.connectSlotsByName(self)

        self.pushButton.clicked.connect(self.setupUiStart)
        self.pushButton_2.clicked.connect(self.save_game)

    def save_game(self):
        if self.minefield:
            name, fl = QtWidgets.QInputDialog.getText(
                self, "Диалоговое окно", "Введите имя сохранения:"
            )
            if fl:
                write_db(name, datetime.now(), self.minefield)

    def mousePressEvent(self, ev: QtGui.QMouseEvent):
        if self.ingame and ev.button() == QtCore.Qt.MouseButton.RightButton:
            if ev.position().toPoint() in self.btn_geometry:
                pos = ev.position().toPoint()
                i, j = (pos.y() - 50) // self.btn_size, (pos.x() - 50) // self.btn_size
                obj = self.btns[i][j]
                if obj.text() == "":
                    obj.setText("F")
                    obj.disconnect()
                elif obj.text() == "F":
                    obj.setText("?")
                elif obj.text() == "?":
                    obj.setText("")
                    obj.clicked.connect(self.clicked_item)
                self.minefield.visual_field[i][j] = obj.text()
                self.lcdNumber.display(
                    self.settings[2]
                    - sum(i.count("F") for i in self.minefield.visual_field)
                )


class GameLogic:
    def clicked_item(self):
        self.ingame = True
        obj, result = self.sender(), None
        if not self.minefield:
            self.minefield = MineField(*self.settings, obj.coord)
            self.minefield.c = 0
        if obj.text() == "":
            result = self.minefield.open(*obj.coord)
        elif obj.text() in "12345678":
            result = self.minefield.click_num(*obj.coord)
        for i in range(self.settings[1]):
            for j in range(self.settings[0]):
                obj_b = self.btns[i][j]
                if result or self.minefield.visual_field[i][j] == "0":
                    obj_b.setEnabled(False)
                if self.minefield.visual_field[i][j] != "0":
                    obj_b.setText(self.minefield.visual_field[i][j])
        if result:
            self.timer.stop()
            write_txt(result)
            if result == "win":
                write_txt(**{self.slsh: self.minefield.c})

    def showTime(self):
        if self.ingame:
            self.minefield.c += 1
            self.lcdNumber_2.display(self.minefield.c)


class StatisticWindow(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 400, 200))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Диалоговое окно"))

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        sl = read_txt()
        self.label.setText(
            """
Всего начато партий: {}, Выиграно: {}, Проиграно : {},
Рекорды:
Простой: {}
Средний: {}
Сложный: {}
Эксперт: {}
""".format(
                sl["all"], sl["win"], sl["lose"], *sl["records"].values()
            )
        )


class DialogWindow(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setGeometry(QtCore.QRect(70, 240, 261, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.widget1 = QtWidgets.QWidget(parent=Dialog)
        self.widget1.setGeometry(QtCore.QRect(70, 60, 261, 121))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(parent=self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.spinBox = QtWidgets.QSpinBox(parent=self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox.setFont(font)
        self.spinBox.setMinimum(2)
        self.spinBox.setMaximum(999)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout.addWidget(self.spinBox)
        self.spinBox_2 = QtWidgets.QSpinBox(parent=self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_2.sizePolicy().hasHeightForWidth())
        self.spinBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setMinimum(2)
        self.spinBox_2.setMaximum(999)
        self.spinBox_2.setObjectName("spinBox_2")
        self.verticalLayout.addWidget(self.spinBox_2)
        self.spinBox_3 = QtWidgets.QSpinBox(parent=self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_3.sizePolicy().hasHeightForWidth())
        self.spinBox_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_3.setFont(font)
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(3)
        self.spinBox_3.setObjectName("spinBox_3")
        self.verticalLayout.addWidget(self.spinBox_3)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Диалоговое окно"))
        self.pushButton.setText(_translate("Dialog", "Ок"))
        self.pushButton_2.setText(_translate("Dialog", "Отмена"))
        self.label.setText(_translate("Dialog", "Длина:"))
        self.label_2.setText(_translate("Dialog", "Ширина:"))
        self.label_3.setText(_translate("Dialog", "Кол-во мин:"))

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.ok)
        self.pushButton_2.clicked.connect(self.cancel)
        self.spinBox.valueChanged.connect(self.run)
        self.spinBox_2.valueChanged.connect(self.run)

    def run(self):
        self.spinBox_3.setMaximum(self.spinBox.value() * self.spinBox_2.value() - 1)

    def ok(self):
        self.parent().settings = (
            self.spinBox.value(),
            self.spinBox_2.value(),
            self.spinBox_3.value(),
        )
        self.destroy(True)
        self.parent().setupUiGame()

    def cancel(self):
        self.destroy(True)
