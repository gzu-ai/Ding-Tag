import json
from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox

from .config_ui import Ui_Form


class Config(Ui_Form):
    """ 首次配置界面 """
    def __init__(self, main) -> None:
        super().__init__()
        
        self.main = main
        self.config_win = QWidget()
        self.setupUi(self.config_win)

        # 绑定事件
        self.data_button.clicked.connect(self.choose_data_path)
        self.save_button.clicked.connect(self.choose_save_path)
        self.submit.clicked.connect(self.config_submit)
    
    def choose_dir(self):
        """ 选择文件夹 """
        dir_path = QFileDialog.getExistingDirectory(
            self.config_win,
            "选择指定文件夹",
            "./"
        )
        return dir_path

    def choose_data_path(self):
        """ 数据文件夹路径 """
        dir_path = self.choose_dir()
        self.data_path_info.setText(dir_path)
    
    def choose_save_path(self):
        """ 标注文件存储路径 """
        dir_path = self.choose_dir()
        self.save_path_info.setText(dir_path)
    
    def config_submit(self):
        """ 用户提交配置信息 """
        info = {
            "username": self.name_info.text(),
            "datapath": self.data_path_info.text(),
            "savepath": self.save_path_info.text()
        }

        info_k = {
            "username": "姓名",
            "datapath": "数据文件夹",
            "savepath": "标注文件存储路径"
        }
        
        # 检查必填字段，不能为空
        flag = True
        for k, v in info.items():
            if v == "":
                QMessageBox.warning(self.config_win, "警告", f"{info_k[k]}不能为空")
                flag = False
                break

        # 字段非空，开始创建配置文件并进入主程序
        if flag:
            # 存储配置文件
            with open("./info.json", "w") as f:
                f.write(json.dumps(info, indent=4))
            
            # 切换到主程序窗口
            self.main.info = info
            self.main.load_ding()
            self.config_win.close()
            self.main.mainwindow.main_win.show()
            self.main.mainwindow.name_info.setText(info["username"])
            self.main.mainwindow.setting_player()
