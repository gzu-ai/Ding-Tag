from PySide6.QtWidgets import QMainWindow
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput

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
