import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from datetime import datetime
from db import write_db, read_db, write_txt
from core import MineField, settings
from ui import *


class MainWindow(QMainWindow):
    def setupUi(self):
        self.setObjectName("mainWindow")
        self.showMaximized()
        self.setCursor(QtGui.QCursor(QtGui.QPixmap("shovel.png")))
        self.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.engineButton = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.engineButton.setFont(font)
        self.engineButton.setObjectName("engineButton")
        self.gridLayout.addWidget(self.engineButton, 0, 0, 1, 1)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("mainWindow", "Сапёр PRO"))
        self.engineButton.setText(_translate("mainWindow", "Запуск"))

        self.setCentralWidget(self.centralwidget)

    def __init__(self):
        super().__init__()
        self.ingame = False
        self.setupUi()
        self.engineButton.clicked.connect(self.main_ui_run)

    def main_ui_run(self):
        main_ui(self)
        self.menuButton.clicked.connect(self.setup_ui_run)

    def setup_ui_run(self):
        setup_ui(self)
        self.ingame = False
        self.startButton.clicked.connect(self.setup_game_ui_run)
        self.redesignButton.clicked.connect(self.redesign_ui_run)
        self.analyticsButton.clicked.connect(self.analytics_ui_run)

    def redesign_ui_run(self):
        pass

    def analytics_ui_run(self):
        analytics_ui(self)

        for i, row in enumerate(read_db()):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            font = QtGui.QFont()
            font.setPointSize(28)
            name, date, btn = (
                QtWidgets.QTableWidgetItem(row[0]),
                QtWidgets.QTableWidgetItem(row[1]),
                QtWidgets.QPushButton("+", self.tableWidget),
            )
            name.setFont(font)
            date.setFont(font)
            self.tableWidget.setItem(i, 0, name)
            self.tableWidget.setItem(i, 1, date)
            btn.field = row[2]
            btn.clicked.connect(self.upload_save)
            self.tableWidget.setCellWidget(i, 2, btn)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

        self.backButton.clicked.connect(self.setup_ui_run)
        self.statisticButton.clicked.connect(self.statistic_run)

    def statistic_run(self):
        StatisticWindow(self).show()

    def upload_save(self):
        self.minefield = self.sender().field
        self.settings = (
            self.minefield.cols,
            self.minefield.rows,
            sum(i.count("x") for i in self.minefield.field),
        )
        self.game_ui_run()

    def setup_game_ui_run(self):
        setup_game_ui(self)
        self.plainButton.clicked.connect(self.game_ui_run)
        self.averageButton.clicked.connect(self.game_ui_run)
        self.complicatedButton.clicked.connect(self.game_ui_run)
        self.expertButton.clicked.connect(self.game_ui_run)
        self.customizableButton.clicked.connect(self.customizable_ui_run)

    def customizable_ui_run(self):
        DialogWindow(self).show()

    def game_ui_run(self):
        game_ui(self)

        self.complexity, result = self.sender().text(), False
        if self.complexity in settings:
            write_txt("all")
            self.settings, self.minefield = settings[self.complexity], 0
        else:
            self.ingame = True
            for i in range(self.settings[1]):
                if "x" in self.minefield.visual_field[i]:
                    result = True
                    break
        self.mineLabel.setText(str(self.settings[2]))
        self.btns = [[] for _ in range(self.settings[1])]
        self.btn_size = min(
            (self.height() - 125) // self.settings[1],
            (self.width() - 100) // self.settings[0],
        )
        for i in range(self.settings[1]):
            for j in range(self.settings[0]):
                x = QtWidgets.QPushButton(parent=self.centralwidget)
                x.setGeometry(
                    QtCore.QRect(
                        50 + j * self.btn_size,
                        100 + i * self.btn_size,
                        self.btn_size,
                        self.btn_size,
                    )
                )
                x.coord = (i, j)
                x.clicked.connect(self.clicked_item)
                self.btns[i].append(x)
                if self.ingame:
                    if result or self.minefield.visual_field[i][j] == "0":
                        x.setEnabled(False)
                    if self.minefield.visual_field[i][j] != "0":
                        x.setText(self.minefield.visual_field[i][j])
        self.btn_geometry = QtCore.QRect(
            50, 50, self.settings[0] * self.btn_size, self.settings[1] * self.btn_size
        )
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)

        self.leaveButton.clicked.connect(self.setup_ui_run)
        self.saveButton.clicked.connect(self.save_game)

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
                write_txt(**{self.complexity: self.minefield.c})

    def showTime(self):
        if self.ingame:
            self.minefield.c += 1
            self.timerLabel.setText(str(self.minefield.c))

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
                i, j = (pos.y() - 100) // self.btn_size, (pos.x() - 50) // self.btn_size
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
                self.mineLabel.setText(
                    str(
                        self.settings[2]
                        - sum(i.count("F") for i in self.minefield.visual_field)
                    )
                )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_form = MainWindow()
    main_form.show()
    sys.exit(app.exec())
