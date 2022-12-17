import sys

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import uic, QtWidgets


import resource_rc as resource_rc

class Index(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.stackedWidget:QStackedWidget
        uic.loadUi("ui/main.ui", self)
        self.setFixedSize(1270, 720)