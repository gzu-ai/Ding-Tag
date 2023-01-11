import os
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl, QSize
from PySide6.QtGui import QIcon

from .mainwindow_ui import Ui_MainWindow


class MyQMainWindow(QMainWindow):
    """ 尝试重写主窗口关闭事件 """
    def __init__(self, mainwindow) -> None:
        super().__init__()
        # 将应用主窗口类传递进来，关闭窗口时方便进行ding.json文件保存
        self.mainwindow = mainwindow
    
    def closeEvent(self, event):
        """ 重写关闭事件 """
        reply = QMessageBox.question(self, "退出程序", "确定退出吗？")
        if reply == QMessageBox.Yes:
            self.mainwindow.main.exit_save_ding()
            event.accept()
        else:
            event.ignore()


class MainWindow(Ui_MainWindow):
    """ 应用主窗口 """
    def __init__(self, main) -> None:
        super().__init__()

        self.main = main
        self.main_win = MyQMainWindow(self)
        self.setupUi(self.main_win)

        # 媒体播放器
        self.player = QMediaPlayer()
        self.audioOutput = QAudioOutput()
        self.player.setAudioOutput(self.audioOutput)
        self.audioOutput.setVolume(1)  # 设置音量，范围为0~1

        # 一些标志
        self.player_flag = "pause"

        # 绑定事件
        self.play.clicked.connect(self.play_button)
        self.player.playbackStateChanged.connect(self.player_state_change)
        self.player.durationChanged.connect(self.setting_overall_process)
        self.player.positionChanged.connect(self.setting_process)
        self.replay.clicked.connect(self.replay_button)
        self.pleasure_info.valueChanged.connect(self.pleasure_change)
        self.action_info.valueChanged.connect(self.action_change)
        self.submit.clicked.connect(self.submit_event)
    
    def setting_player(self):
        """ 设置播放器 """
        if self.main.ding["id"] == self.main.ding["end"]:  # 标注完成
            QMessageBox.information(self.main_win, "提示", "该数据已标注完成，请退出程序")
            self.main_win.close()
        else:
            self.path_info.setText(
                self.main.ding["filelist"][self.main.ding["id"]].split(os.sep)[1]
            )
            self.player.setSource(
                QUrl.fromLocalFile(self.main.ding["filelist"][self.main.ding["id"]])
            )
    
    def play_button(self):
        """ 播放按键控制播放状态 """
        if self.player_flag == "pause":  # 停止 --> 播放
            self.palyer_stoptoplay()
            self.player.play()
        else:  # 播放 --> 停止
            self.player_playtostop()
            self.player.pause()
    
    def player_state_change(self, state):
        """ 播放器状态发生改变对应的事件 """
        if state == QMediaPlayer.PlaybackState.StoppedState:
            self.player_playtostop()
    
    def replay_button(self):
        """ 重播按键对应的事件 """
        self.player.stop()  # 先将播放器统一到停止状态
        self.player.setPosition(0)  # 将播放进度归零
        # 重新进入播放状态
        self.palyer_stoptoplay()
        self.player.play()
    
    def setting_overall_process(self, duration):
        """ 设置进度条的总进度 """
        self.t_bar.setMaximum(duration)
    
    def setting_process(self, position):
        """ 设置当前的播放进度 """
        self.t_bar.setValue(position)
    
    def palyer_stoptoplay(self):
        """ 播放器 停止 --> 播放 """
        self.player_flag = "play"
        temp_icon = QIcon()
        temp_icon.addFile(u"./static/icons/pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.play.setIcon(temp_icon)
    
    def player_playtostop(self):
        """ 播放器 播放 --> 停止 """
        self.player_flag = "pause"
        temp_icon = QIcon()
        temp_icon.addFile(u"./static/icons/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.play.setIcon(temp_icon)
    
    def pleasure_change(self, value):
        """ 愉悦维滑动的值 """
        self.pleasure_show.setText("{:.1f}".format(value / 10))
    
    def action_change(self, value):
        """ 激活维滑动的值 """
        self.action_show.setText("{:.1f}".format(value / 10))
    
    def info_table(self):
        """ 获取所有标注信息 """
        info_table = {
            "name": self.name_info.text(),
            "flag1": self.flag1.isChecked(), "flag2": self.flag2.isChecked(),
            "flag3": self.flag3.isChecked(), "flag4": self.flag4.isChecked(),
            "role": "", "emotion": "",
            "text": self.text_info.toPlainText(),
            "pleasure": self.pleasure_show.text(), "action": self.action_show.text()
        }
        # 单独处理角色和离散标签
        value = self.emotion_info.currentText()
        if not value == "":
            info_table["role"], info_table["emotion"] = value.split("-")
        return info_table
    
    def save_result(self, info_table):
        """ 存储标注结果 """
        with open(os.path.join(self.main.info["savepath"], "result.csv"), "a") as f:
            f.write(
                "{},{},{},{},{},{},{},{},{},{},{}\n".format(
                    self.path_info.text(),
                    info_table["name"], info_table["flag1"], info_table["flag2"],
                    info_table["flag3"], info_table["flag4"], info_table["role"],
                    info_table["text"], info_table["emotion"],
                    info_table["pleasure"], info_table["action"]
                )
            )
    
    def recovery_ding(self):
        """ 将标注项全部复原 """
        self.flag1.setChecked(False)
        self.flag2.setChecked(False)
        self.flag3.setChecked(False)
        self.flag4.setChecked(False)
        self.text_info.clear()
        self.emotion_info.setCurrentIndex(-1)
        self.pleasure_info.setValue(0)
        self.action_info.setValue(0)
    
    def submit_event(self):
        """ 提交标注信息 """
        info_table = self.info_table()
        # 检查音频有无异常情况下
        flag_normal = True
        for flag in ["flag1", "flag2", "flag3", "flag4"]:
            if info_table[flag]:
                flag_normal = False
                break
        # 音频无异常情况，则所有字段不能为空
        normal = True
        if flag_normal:
            for check in ["role", "emotion", "text"]:
                if info_table[check] == "":
                    QMessageBox.warning(self.main_win, "警告", f"音频无异常，音频文本与情感分类不能为空")
                    normal = False
                    break
        # 通过检查，请用户确认
        if normal:
            box = QMessageBox.question(self.main_win, "用户确定", "确定该样本标注无误吗？")
            if box == QMessageBox.Yes:
                # 标注无误，存储结果
                self.save_result(info_table)
                # 修改样本索引
                self.main.ding["id"] += 1
                # 重新设置播放器
                self.setting_player()
                # 重新设置标注项
                self.recovery_ding()
