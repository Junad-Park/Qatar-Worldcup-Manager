import sys

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import uic, QtWidgets
from utils.audio import Audio

import resource_rc as resource_rc

class Index(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("ui/index.ui", self)
        self.setFixedSize(1270, 720)

        self.audio = Audio()
        
    def muteAudio(self):
        self.audio.muteAudio()

    def nextAudio(self):
        self.audio.nextAudio()
    
    def previousAudio(self):
        self.audio.previousAudio()
    
    def playAudioFile(self):
        self.audio.playAudioFile()