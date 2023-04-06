import os, json, threading
from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox

from .config_ui import Ui_Form


class Config(Ui_Form):
    """ 首次配置界面 """
    def __init__(self, main) -> None:
        super().__init__()
        
        self.main = main
        self.config_win = QWidget()
        self.setupUi(self.config_win)
        self.hide_baidu()  # 默认将百度语音识别的接口隐藏

        # 绑定事件
        self.data_button.clicked.connect(self.choose_data_path)
        self.save_button.clicked.connect(self.choose_save_path)
        self.submit.clicked.connect(self.config_submit)
        self.baidu_asr.stateChanged.connect(self.baidu_choose_change)
    
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
    
    def baidu_choose_change(self):
        """ 百度语音识别接口的复选框状态发生变化 """
        if self.baidu_asr.isChecked():
            self.show_baidu()
        else:
            self.hide_baidu()
    
    def hide_baidu(self):
        """ 隐藏百度语音识别相关的配置项 """
        self.api_key.hide()
        self.api_key_info.hide()
        self.secret_key.hide()
        self.secret_key_info.hide()

    def show_baidu(self):
        """ 显示百度语音识别相关的配置项 """
        self.api_key.show()
        self.api_key_info.show()
        self.secret_key.show()
        self.secret_key_info.show()
    
    def config_submit(self):
        """ 用户提交配置信息 """
        
        # 获取用户提交的配置信息
        flag, info = self.get_config_info()

        # 配置信息通过检查，开始创建配置文件并进入主程序
        if flag:
            # 生成配置文件
            self.create_config_file(info)
            
            # 切换到主程序窗口
            self.main.info = info
            self.main.load_ding()
            self.config_win.close()
            self.main.mainwindow.main_win.show()
            self.main.mainwindow.name_info.setText(info["username"])
            self.main.mainwindow.setting_player()
            # 使用线程防止网络请求阻塞程序
            asr = threading.Thread(self.main.mainwindow.asr)
            asr.start()
            
    def get_config_info(self):
        """ 获取配置信息并做相应的限制检查 """
        info = {
            "username": self.name_info.text(),
            "datapath": self.data_path_info.text(),
            "savepath": self.save_path_info.text(),
            "baiduchoose": self.baidu_asr.isChecked(),
            "apikey": self.api_key_info.text(),
            "secretkey": self.secret_key_info.text()
        }
        
        # 如果用户不使用百度语音识别服务，不论是否提交了key，我们都不存储
        if not info["baiduchoose"]:
            info["apikey"] = ''
            info["secretkey"] = ''
        
        # 检查前三项为必填项
        flag = True
        for item in ["username", "datapath", "savepath"]:
            if info[item] == '':
                QMessageBox.warning(self.config_win, "警告", f"前三项不能为空")
                flag = False
                break
        
        # 如果使用百度语音识别服务，其key不能为空
        if info["baiduchoose"]:
            for item in ["apikey", "secretkey"]:
                if info[item] == '':
                    QMessageBox.warning(self.config_win, "警告", f"{item} 不能为空")
                    flag = False
                    break
        
        # savepath 进行重构，在存储路径的基础上，存储文件根据 datapath 进行重命名
        if flag:
            info["savepath"] = os.path.join(
                info["savepath"], "result-{}-{}.csv".format(os.path.basename(info["datapath"]), info["username"])
            )
        
        return flag, info
    
    def create_config_file(self, info):
        """ 创建配置文件 """
        # 存储配置文件
        with open("./info.json", "w") as f:
            f.write(json.dumps(info, indent=4))
        
        # 创建标注文件
        with open(info["savepath"], "w") as f:
            f.write(
                "{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(
                    "音频文件", "标注人", "内容没有听懂", "内容不全", "包含敏感信息", "静音过长",
                    "全为杂音", "首尾杂音", "音量偏小", "时长偏短", "时长偏长", "客服开头", "客服结尾",
                    "音频内容", "音频角色", "情感标签", "愉悦维", "激活维"
                )
            )
