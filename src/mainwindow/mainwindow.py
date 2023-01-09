import os
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl, QSize
from PySide6.QtGui import QIcon

from .mainwindow_ui import Ui_MainWindow


class MainWindow(Ui_MainWindow):
    """ 应用主窗口 """
    def __init__(self, main) -> None:
        super().__init__()

        self.main = main
        self.main_win = QMainWindow()
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
    
    def setting_player(self):
        """ 设置播放器 """
        if self.main.ding["id"] == self.main.ding["end"]:  # 标注完成
            QMessageBox.information(self.main_win, "提示", "该数据已标注完成，请退出程序")
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
