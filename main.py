import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from datetime import datetime
from db import write_db, read_db, write_txt
from core import *
from ui import *


class MainWindow(QMainWindow):
    def setupUi(self):
        self.setObjectName("mainWindow")
        self.showMaximized()
        self.setCursor(QtGui.QCursor(QtGui.QPixmap("shovel.png")))
        self.setWindowIcon(QtGui.QIcon("icon.ico"))
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
        redesign_ui(self)

        self.backButton.clicked.connect(self.setup_ui_run)
        self.colorButton.clicked.connect(self.color_change)
        self.flagButton.clicked.connect(self.flag_change)
        self.mineButton.clicked.connect(self.mine_change)

    def color_change(self):
        self.col = QtWidgets.QColorDialog.getColor(parent=self, title="Выберите цвет:")
        col_text = (0, 0, 0) if self.col.black() < 128 else (255, 255, 255)
        self.col_text = QtGui.QColor(*col_text)
        self.col_d = self.col.darker(130)
        col_d_text = (0, 0, 0) if self.col_d.black() < 128 else (255, 255, 255)
        self.col_d_text = QtGui.QColor(*col_d_text)

    def flag_change(self):
        name, fl = QtWidgets.QInputDialog.getText(
            self, "Диалоговое окно", "Введите символ флага:"
        )
        if name and fl and name != settings["mine_sim"] and not name[0].isdigit():
            settings["flag_sim"] = name[0]

    def mine_change(self):
        name, fl = QtWidgets.QInputDialog.getText(
            self, "Диалоговое окно", "Введите символ мины:"
        )
        if name and fl and name != settings["flag_sim"] and not name[0].isdigit():
            settings["mine_sim"] = name[0]

    def analytics_ui_run(self):
        analytics_ui(self)

        font = QtGui.QFont()
        font.setPointSize(28)
        for i, row in enumerate(read_db()):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            name, date, btn = (
                QtWidgets.QTableWidgetItem(row[0]),
                QtWidgets.QTableWidgetItem(row[1]),
                QtWidgets.QPushButton("+", self.tableWidget),
            )
            name.setFont(font), date.setFont(font)
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
        self.settings = self.minefield.settings
        for i in range(self.settings[1]):
            for j in range(self.settings[0]):
                if (
                    self.minefield.visual_field[i][j]
                    == self.minefield.setin["mine_sim"]
                ):
                    self.minefield.visual_field[i][j] = settings["mine_sim"]
                elif (
                    self.minefield.visual_field[i][j]
                    == self.minefield.setin["flag_sim"]
                ):
                    self.minefield.visual_field[i][j] = settings["flag_sim"]
                if self.minefield.field[i][j] == self.minefield.setin["mine_sim"]:
                    self.minefield.field[i][j] = settings["mine_sim"]
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
        elif self.complexity == "Ок":
            write_txt("all")
            self.minefield = 0
        else:
            self.ingame = True
            for i in range(self.settings[1]):
                if settings["mine_sim"] in self.minefield.visual_field[i]:
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
                x = QtWidgets.QPushButton(
                    parent=self.centralwidget,
                )
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
                x.setStyleSheet(
                    f"color: rgb({','.join(map(str, self.col_text.getRgb()[:-1]))});"
                    + f"background: rgb({','.join(map(str, self.col.getRgb()[:-1]))});"
                    + f"border: 1px solid rgb({','.join(map(str, self.col_text.getRgb()[:-1]))});"
                )
                font = QtGui.QFont()
                font.setPointSize(16)
                x.setFont(font)
                self.btns[i].append(x)
                if self.ingame:
                    if self.minefield.visual_field[i][j] == "0":
                        x.hide()
                        x.setEnabled(False)
                    if result:
                        x.setEnabled(False)
                    if self.minefield.visual_field[i][j] != "0":
                        x.setText(self.minefield.visual_field[i][j])
                    if self.minefield.visual_field[i][j].isdigit():
                        x.setStyleSheet(
                            f"color: rgb({','.join(map(str, self.col_d_text.getRgb()[:-1]))});"
                            + f"background: rgb({','.join(map(str, self.col_d.getRgb()[:-1]))});"
                            + f"border: 1px solid rgb({','.join(map(str, self.col_d_text.getRgb()[:-1]))});"
                        )
        self.btn_geometry = QtCore.QRect(
            50, 100, self.settings[0] * self.btn_size, self.settings[1] * self.btn_size
        )
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)
        if result:
            self.timer.stop()

        self.leaveButton.clicked.connect(self.setup_ui_run)
        self.saveButton.clicked.connect(self.save_game)

    def clicked_item(self):
        self.ingame = True
        obj, result = self.sender(), None
        if not self.minefield:
            self.minefield = MineField(*self.settings, obj.coord)
            self.minefield.c = 0
            self.minefield.setin = settings
        if obj.text() == "":
            result = self.minefield.open(*obj.coord)
        elif obj.text() in "12345678":
            result = self.minefield.click_num(*obj.coord)
        for i in range(self.settings[1]):
            for j in range(self.settings[0]):
                obj_b = self.btns[i][j]
                if self.minefield.visual_field[i][j] == "0":
                    obj_b.hide()
                    obj_b.setEnabled(False)
                if result:
                    obj_b.setEnabled(False)
                if self.minefield.visual_field[i][j] != "0":
                    obj_b.setText(self.minefield.visual_field[i][j])
                if self.minefield.visual_field[i][j].isdigit():
                    obj_b.setStyleSheet(
                        f"color: rgb({','.join(map(str, self.col_d_text.getRgb()[:-1]))});"
                        + f"background: rgb({','.join(map(str, self.col_d.getRgb()[:-1]))});"
                        + f"border: 1px solid rgb({','.join(map(str, self.col_d_text.getRgb()[:-1]))});"
                    )
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
            if name and fl:
                write_db(name, datetime.now(), self.minefield)

    def mousePressEvent(self, ev: QtGui.QMouseEvent):
        if self.ingame and ev.button() == QtCore.Qt.MouseButton.RightButton:
            if ev.position().toPoint() in self.btn_geometry:
                pos = ev.position().toPoint()
                i, j = (pos.y() - 100) // self.btn_size, (pos.x() - 50) // self.btn_size
                obj = self.btns[i][j]
                if obj.text() == "":
                    obj.setText(settings["flag_sim"])
                    obj.disconnect()
                elif obj.text() == settings["flag_sim"]:
                    obj.setText("?")
                elif obj.text() == "?":
                    obj.setText("")
                    obj.clicked.connect(self.clicked_item)
                self.minefield.visual_field[i][j] = obj.text()
                self.mineLabel.setText(
                    str(
                        self.settings[2]
                        - sum(
                            i.count(settings["flag_sim"])
                            for i in self.minefield.visual_field
                        )
                    )
                )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_form = MainWindow()
    main_form.show()
    sys.exit(app.exec())
