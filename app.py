import os
import json
from PySide6.QtWidgets import QApplication

from src.config.config import Config
from src.mainwindow.mainwindow import MainWindow


class Main:
    """ 程序主类 """
    def __init__(self) -> None:
        
        # 所有的页面
        self.config = Config(self)
        self.mainwindow = MainWindow(self)
        self.info = None

        # 开始运行，如果首次运行，则需要进行配置
        if os.path.exists("./info.json"):
            with open("./info.json", 'r') as f:
                self.info = json.load(f)
            self.mainwindow.name_info.setText(self.info["username"])
            self.mainwindow.main_win.show()
        else:
            self.config.config_win.show()


if __name__ == "__main__":
    app = QApplication()
    main = Main()
    app.exec()
