import os
import json
import glob
from PySide6.QtWidgets import QApplication

from src.config.config import Config
from src.mainwindow.mainwindow import MainWindow


class Main:
    """ 程序主类 """
    def __init__(self) -> None:
        
        # 所有的页面
        self.config = Config(self)
        self.mainwindow = MainWindow(self)

        # 公共配置信息
        self.info = None
        self.ding = None

        # 开始运行，如果首次运行，则需要进行配置
        if os.path.exists("./info.json"):
            with open("./info.json", 'r') as f:
                self.info = json.load(f)
            self.load_ding()
            self.mainwindow.name_info.setText(self.info["username"])
            self.mainwindow.main_win.show()
            self.mainwindow.setting_player()
        else:
            self.config.config_win.show()
    
    def load_ding(self):
        """ 加载标注的记录文件 """
        if os.path.exists("./ding.json"):
            with open("./ding.json", 'r') as f:
                self.ding = json.load(f)
        else:
            self.ding = {
                "filelist": glob.glob(self.info["datapath"] + "/*.mp3"),
                "id": 0
            }
            self.ding["end"] = len(self.ding["filelist"])
            with open("./ding.json", "w") as f:
                f.write(json.dumps(self.ding, indent=4))


if __name__ == "__main__":
    app = QApplication()
    main = Main()
    app.exec()
