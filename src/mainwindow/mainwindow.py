from PySide6.QtWidgets import QMainWindow

from .mainwindow_ui import Ui_MainWindow


class MainWindow(Ui_MainWindow):
    """ 应用主窗口 """
    def __init__(self, main) -> None:
        super().__init__()

        self.main = main
        self.main_win = QMainWindow()
        self.setupUi(self.main_win)
