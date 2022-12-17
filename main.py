import sys

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import QUrl
from PyQt6.QtMultimedia import QAudioOutput, QMediaPlayer
from PyQt6 import uic, QtWidgets
from widgets.index import Index

import resource_rc as resource_rc

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("ui/form.ui", self)
        self.stackedWidget:QStackedWidget
        self.setFixedSize(1270, 720)
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.playAudioFile()

    def moveIndexWindow(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

    def playAudioFile(self):
        file_path = "music/승리를위하여.mp3"
        self.player.setAudioOutput(self.audio_output)
        self.player.setSource(QUrl.fromLocalFile(file_path))
        self.audio_output.setVolume(50)
        self.player.play()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 화면 전환용 Widget 설정
    widget = QtWidgets.QStackedWidget()

    # 레이아웃 인스턴스 생성
    mainwindow = MainWindow()
    indexWindow = Index()

    widget.addWidget(mainwindow)
    widget.addWidget(indexWindow)

    widget.show()
    sys.exit(app.exec())
