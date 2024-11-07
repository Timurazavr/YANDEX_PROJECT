from PyQt6 import QtCore, QtGui, QtWidgets
from db import read_txt


def main_ui(self: QtWidgets.QMainWindow):
    self.setMinimumSize(self.width(), self.height())
    self.setStyleSheet(
        """MainWindow#mainWindow {border-image: url("main_background.png")};"""
    )
    self.centralwidget = QtWidgets.QWidget(parent=self)
    self.centralwidget.setObjectName("centralwidget")
    label = QtWidgets.QLabel(parent=self.centralwidget)
    label.setGeometry(
        QtCore.QRect(
            self.width() // 4,
            self.height() // 4,
            self.width() // 2,
            self.height() // 4,
        )
    )
    font = QtGui.QFont()
    font.setPointSize(56)
    font.setFamily("Segoe Print")
    font.setBold(True)
    font.setWeight(1000)
    label.setFont(font)
    label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    label.setObjectName("label")
    shadow = QtWidgets.QGraphicsDropShadowEffect(
        self,
        blurRadius=30.0,
        color=QtGui.QColor(255, 255, 255),
        offset=QtCore.QPointF(0.0, 0.0),
    )
    label.setGraphicsEffect(shadow)
    self.menuButton = QtWidgets.QPushButton(parent=self.centralwidget)
    self.menuButton.setGeometry(
        QtCore.QRect(
            self.width() // 3,
            self.height() // 2,
            self.width() // 3,
            self.height() // 4,
        )
    )
    self.fontBtn, self.styleBtn = (
        QtGui.QFont(),
        "background: rgb(91,44,11); border-radius: 30px",
    )
    self.col = QtGui.QColor(255, 255, 255)
    self.col_text = QtGui.QColor(0, 0, 0)
    self.col_d = self.col.darker(130)
    self.col_d_text = QtGui.QColor(255, 255, 255)
    self.fontBtn.setFamily("Franklin Gothic Medium")
    self.fontBtn.setPointSize(36)
    self.menuButton.setFont(self.fontBtn)
    self.menuButton.setStyleSheet(self.styleBtn)
    self.menuButton.setObjectName("menuButton")

    _translate = QtCore.QCoreApplication.translate
    label.setText(_translate("mainWindow", "Сапёр PRO"))
    self.menuButton.setText(_translate("mainWindow", "Начать"))

    self.setCentralWidget(self.centralwidget)


def setup_ui(self):
    self.centralwidget = QtWidgets.QWidget(parent=self)
    self.centralwidget.setObjectName("centralwidget")
    self.startButton = QtWidgets.QPushButton(parent=self.centralwidget)
    self.startButton.setGeometry(
        QtCore.QRect(
            int(self.width() * 0.267),
            int(self.height() * 0.562),
            int(self.width() * 0.466),
            int(self.height() * 0.312),
        )
    )
    self.startButton.setFont(self.fontBtn)
    self.startButton.setStyleSheet(self.styleBtn)
    self.startButton.setObjectName("startButton")
    self.redesignButton = QtWidgets.QPushButton(parent=self.centralwidget)
    self.redesignButton.setGeometry(
        QtCore.QRect(
            self.width() // 15,
            self.height() // 8,
            self.width() // 3,
            self.height() // 4,
        )
    )
    self.redesignButton.setFont(self.fontBtn)
    self.redesignButton.setStyleSheet(self.styleBtn)
    self.redesignButton.setObjectName("redesignButton")
    self.analyticsButton = QtWidgets.QPushButton(parent=self.centralwidget)
    self.analyticsButton.setGeometry(
        QtCore.QRect(
            int(self.width() * 0.6),
            self.height() // 8,
            self.width() // 3,
            self.height() // 4,
        )
    )
    self.analyticsButton.setFont(self.fontBtn)
    self.analyticsButton.setStyleSheet(self.styleBtn)
    self.analyticsButton.setObjectName("analyticsButton")

    _translate = QtCore.QCoreApplication.translate
    self.startButton.setText(_translate("MainWindow", "Играть"))
    self.redesignButton.setText(_translate("MainWindow", "Смена дизайна"))
    self.analyticsButton.setText(_translate("MainWindow", "Аналитика игр"))

    self.setCentralWidget(self.centralwidget)


def setup_game_ui(self):
    self.centralwidget = QtWidgets.QWidget(parent=self)
    self.centralwidget.setObjectName("centralwidget")
    label = QtWidgets.QLabel(parent=self.centralwidget)
    label.setGeometry(
        QtCore.QRect(
            int(self.width() * 0.267),
            self.height() // 32,
            int(self.width() * 0.466),
            self.height() // 8,
        )
    )
    font = QtGui.QFont()
    font.setPointSize(50)
    font.setFamily("Segoe Print")
    font.setBold(True)
    font.setWeight(1000)
    label.setFont(font)
    label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    label.setObjectName("label")
    self.plainButton = QtWidgets.QPushButton(parent=self.centralwidget)
    self.plainButton.setGeometry(
        QtCore.QRect(
            int(self.width() * 0.267),
            int(self.height() * 0.187),
            int(self.width() * 0.466),
            self.height() // 8,
        )
    )
    self.plainButton.setFont(self.fontBtn)
    self.plainButton.setStyleSheet(self.styleBtn)
    self.plainButton.setObjectName("plainButton")
    self.averageButton = QtWidgets.QPushButton(parent=self.centralwidget)
    self.averageButton.setGeometry(
        QtCore.QRect(
            int(self.width() * 0.267),
            int(self.height() * 0.343),
            int(self.width() * 0.466),
            self.height() // 8,
        )
    )
    self.averageButton.setFont(self.fontBtn)
    self.averageButton.setStyleSheet(self.styleBtn)
    self.averageButton.setObjectName("averageButton")
    self.complicatedButton = QtWidgets.QPushButton(parent=self.centralwidget)
    self.complicatedButton.setGeometry(
        QtCore.QRect(
            int(self.width() * 0.267),
            self.height() // 2,
            int(self.width() * 0.466),
            self.height() // 8,
        )
    )
    self.complicatedButton.setFont(self.fontBtn)
    self.complicatedButton.setStyleSheet(self.styleBtn)
    self.complicatedButton.setObjectName("complicatedButton")
    self.expertButton = QtWidgets.QPushButton(parent=self.centralwidget)
    self.expertButton.setGeometry(
        QtCore.QRect(
            int(self.width() * 0.267),
            int(self.height() * 0.656),
            int(self.width() * 0.466),
            self.height() // 8,
        )
    )
    self.expertButton.setFont(self.fontBtn)
    self.expertButton.setStyleSheet(self.styleBtn)
    self.expertButton.setObjectName("expertButton")
    self.customizableButton = QtWidgets.QPushButton(parent=self.centralwidget)
    self.customizableButton.setGeometry(
        QtCore.QRect(
            int(self.width() * 0.267),
            int(self.height() * 0.812),
            int(self.width() * 0.466),
            self.height() // 8,
        )
    )
    self.customizableButton.setFont(self.fontBtn)
    self.customizableButton.setStyleSheet(self.styleBtn)
    self.customizableButton.setObjectName("customizableButton")

    self.setCentralWidget(self.centralwidget)

    _translate = QtCore.QCoreApplication.translate
    label.setText(_translate("MainWindow", "Режим игры:"))
    self.plainButton.setText(_translate("MainWindow", "Простой"))
    self.averageButton.setText(_translate("MainWindow", "Средний"))
    self.complicatedButton.setText(_translate("MainWindow", "Сложный"))
    self.expertButton.setText(_translate("MainWindow", "Эксперт"))
    self.customizableButton.setText(_translate("MainWindow", "Настраиваемый"))


def redesign_ui(self):
    self.centralwidget = QtWidgets.QWidget(parent=self)
    self.centralwidget.setObjectName("centralwidget")
    self.backButton = QtWidgets.QPushButton(parent=self.centralwidget)
    self.backButton.setGeometry(
        QtCore.QRect(
            self.width() // 30,
            self.height() // 8,
            int(self.width() * 0.45),
            self.height() // 4,
        )
    )
    self.backButton.setFont(self.fontBtn)
    self.backButton.setStyleSheet(self.styleBtn)
    self.backButton.setObjectName("backButton")
    self.colorButton = QtWidgets.QPushButton(parent=self.centralwidget)
    self.colorButton.setGeometry(
        QtCore.QRect(
            self.width() // 30,
            int(self.height() * 0.625),
            int(self.width() * 0.45),
            self.height() // 4,
        )
    )
    self.colorButton.setFont(self.fontBtn)
    self.colorButton.setStyleSheet(self.styleBtn)
    self.colorButton.setObjectName("colorButton")
    self.flagButton = QtWidgets.QPushButton(parent=self.centralwidget)
    self.flagButton.setGeometry(
        QtCore.QRect(
            int(self.width() * 0.516),
            self.height() // 8,
            int(self.width() * 0.45),
            self.height() // 4,
        )
    )
    self.flagButton.setFont(self.fontBtn)
    self.flagButton.setStyleSheet(self.styleBtn)
    self.flagButton.setObjectName("flagButton")
    self.mineButton = QtWidgets.QPushButton(parent=self.centralwidget)
    self.mineButton.setGeometry(
        QtCore.QRect(
            int(self.width() * 0.516),
            int(self.height() * 0.625),
            int(self.width() * 0.45),
            self.height() // 4,
        )
    )
    self.mineButton.setFont(self.fontBtn)
    self.mineButton.setStyleSheet(self.styleBtn)
    self.mineButton.setObjectName("mineButton")

    _translate = QtCore.QCoreApplication.translate
    self.backButton.setText(_translate("MainWindow", "Назад"))
    self.colorButton.setText(_translate("MainWindow", "Сменить цвет кнопки"))
    self.flagButton.setText(_translate("MainWindow", "Сменить символ флага"))
    self.mineButton.setText(_translate("MainWindow", "Сменить символ мины"))

    self.setCentralWidget(self.centralwidget)


def analytics_ui(self):
    self.centralwidget = QtWidgets.QWidget(parent=self)
    self.centralwidget.setObjectName("centralwidget")
    self.backButton = QtWidgets.QPushButton(parent=self.centralwidget)
    self.backButton.setGeometry(
        QtCore.QRect(
            self.width() // 30,
            self.height() // 16,
            int(self.width() * 0.266),
            self.height() // 8,
        )
    )
    self.backButton.setFont(self.fontBtn)
    self.backButton.setStyleSheet(self.styleBtn)
    self.backButton.setObjectName("backButton")
    self.statisticButton = QtWidgets.QPushButton(parent=self.centralwidget)
    self.statisticButton.setGeometry(
        QtCore.QRect(
            int(self.width() * 0.7),
            self.height() // 16,
            int(self.width() * 0.266),
            self.height() // 8,
        )
    )
    self.statisticButton.setFont(self.fontBtn)
    self.statisticButton.setStyleSheet(self.styleBtn)
    self.statisticButton.setObjectName("statisticButton")
    label = QtWidgets.QLabel(parent=self.centralwidget)
    label.setGeometry(
        QtCore.QRect(
            int(self.width() * 0.3),
            self.height() // 16,
            int(self.width() * 0.4),
            self.height() // 8,
        )
    )
    font = QtGui.QFont()
    font.setPointSize(50)
    font.setFamily("Segoe Print")
    font.setBold(True)
    font.setWeight(1000)
    label.setFont(font)
    label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    label.setObjectName("label")
    self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
    self.tableWidget.setGeometry(
        QtCore.QRect(
            int(self.width() * 0.3),
            self.height() // 4,
            int(self.width() * 0.4),
            int(self.height() * 0.688),
        )
    )
    self.tableWidget.setObjectName("tableWidget")
    self.tableWidget.setColumnCount(3)
    self.tableWidget.setHorizontalHeaderLabels(
        ("Имя сохранения", "Дата сохранения", "Нажмите для загрузки")
    )
    self.tableWidget.setRowCount(0)

    _translate = QtCore.QCoreApplication.translate
    self.backButton.setText(_translate("MainWindow", "Назад"))
    self.statisticButton.setText(_translate("MainWindow", "Статистика"))
    label.setText(_translate("MainWindow", "Сохранения:"))

    self.setCentralWidget(self.centralwidget)


def game_ui(self, fl=True):
    self.centralwidget = QtWidgets.QWidget(parent=self)
    self.centralwidget.setObjectName("centralwidget")
    font, style = (
        QtGui.QFont(),
        "background: rgb(91,44,11); border-radius: 5px",
    )
    font.setFamily("Franklin Gothic Medium")
    font.setPointSize(24)
    self.leaveButton = QtWidgets.QPushButton(parent=self.centralwidget)
    self.leaveButton.setGeometry(
        QtCore.QRect(
            self.width() // 60,
            self.height() // 32,
            int(self.width() * 0.133),
            self.height() // 16,
        )
    )
    self.leaveButton.setStyleSheet(style)
    self.leaveButton.setFont(font)
    self.leaveButton.setObjectName("leaveButton")
    self.saveButton = QtWidgets.QPushButton(parent=self.centralwidget)
    self.saveButton.setGeometry(
        QtCore.QRect(
            int(self.width() * 0.166),
            self.height() // 32,
            int(self.width() * 0.133),
            self.height() // 16,
        )
    )
    self.saveButton.setStyleSheet(style)
    self.saveButton.setFont(font)
    self.saveButton.setObjectName("saveButton")
    self.mineLabel = QtWidgets.QLabel(parent=self.centralwidget)
    self.mineLabel.setGeometry(
        QtCore.QRect(
            int(self.width() * 0.5),
            self.height() // 32,
            self.width() // 15,
            self.height() // 16,
        )
    )
    self.mineLabel.setFont(font)
    self.mineLabel.setObjectName("mineLabel")
    self.timerLabel = QtWidgets.QLabel(parent=self.centralwidget)
    self.timerLabel.setGeometry(
        QtCore.QRect(
            int(self.width() * 0.7),
            self.height() // 32,
            self.width() // 15,
            self.height() // 16,
        )
    )
    self.timerLabel.setFont(font)
    self.timerLabel.setObjectName("timerLabel")

    _translate = QtCore.QCoreApplication.translate
    self.leaveButton.setText(_translate("MainWindow", "Выход"))
    self.saveButton.setText(_translate("MainWindow", "Сохранить"))
    self.timerLabel.setText(_translate("MainWindow", "0"))

    self.setCentralWidget(self.centralwidget)


class StatisticWindow(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(450, 260)
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 450, 260))
        font = QtGui.QFont()
        font.setPointSize(24)
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
            """Всего начато партий: {}
Выиграно: {}, Проиграно : {}

Рекорды:
Простой: {}, Средний: {},
Сложный: {}, Эксперт: {}""".format(
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
        self.spinBox.setMaximum(50)
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
        self.spinBox_2.setMaximum(50)
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
        self.close()
        self.parent().game_ui_run()

    def cancel(self):
        self.close()
