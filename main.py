import sys, webbrowser

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import uic, QtWidgets

from utils.audio import Audio
from utils.qatarWcApi import QatarWcApi

import resource_rc as resource_rc

ui = ["ui/form.ui", "ui/index.ui", "ui/highlight.ui", "ui/schedule.ui", "ui/news.ui",]

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(ui[0], self)
        self.setFixedSize(1270, 720)

        self.audio = Audio()
        self.wc = QatarWcApi()
        

    def webOpen(self):
        target = self.sender()
        target_link = target
        webbrowser.open("https://www.fifa.com/fifaplus/en/watch/1wjjV5kxwpSHRjeEkxidIC")

    def movePage(self):
        target = self.sender()
        target_num = int(target.objectName().split('_')[1])
        uic.loadUi(ui[target_num], self)

    def muteAudio(self):
        self.audio.muteAudio()

    def nextAudio(self):
        self.audio.nextAudio()
    
    def previousAudio(self):
        self.audio.previousAudio()
    
    def playAudioFile(self):
        self.audio.playAudioFile()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec())
