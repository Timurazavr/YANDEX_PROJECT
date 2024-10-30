import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui_forms import UiMain, UiStartMenu, UiSetupGame, UiGame, GameLogic


class MainWin(QMainWindow, UiMain, UiStartMenu, UiSetupGame, UiGame, GameLogic):
    def __init__(self):
        super().__init__()
        self.setupUi()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_form = MainWin()
    main_form.show()
    sys.exit(app.exec())
