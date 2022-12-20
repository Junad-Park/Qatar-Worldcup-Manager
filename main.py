import sys, webbrowser
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import uic, QtWidgets
from utils.audio import Audio
from utils.qatarWcApi import QatarWcApi
import resource_rc as resource_rc

ui = ["ui/form.ui", "ui/index.ui", "ui/highlight.ui", "ui/schedule.ui", "ui/news.ui",]
news_url = [
    'https://www.fifa.com/fifaplus/en/articles/a-tribute-to-lionel-messi-legend-argentina-fifa-world-cup-qatar-2022-quotes-stats-stories-goals',
    'https://www.fifa.com/fifaplus/en/articles/world-cup-2022-qatar-france-mbappe-argentina-return',
    'https://www.fifa.com/fifaplus/en/watch/LClFVl7N4EGxNeVV4Rb1eg',
    'https://www.fifa.com/fifaplus/en/articles/top-assisters-at-world-cup-qatar-2022',
    'https://www.fifa.com/fifaplus/en/articles/world-cup-qatar-2022-final-argentina-messi-mbappe-france-videos-reaction',
    'https://www.fifa.com/fifaplus/en/watch/bg6S7A_nRE2qSJGKZhg-Bw'
]
highlight_url = [
    'https://www.fifa.com/fifaplus/en/watch/63XwuAOoqYgNW0Q3E9PxJG',
    'https://www.fifa.com/fifaplus/en/watch/5BAGunqVa9YUoPdZxI8MTm',
    'https://www.fifa.com/fifaplus/en/watch/783zSqR6RRJrx6UiakMYc4',
    'https://www.fifa.com/fifaplus/en/watch/ib6UqdiMuU-_jkJh_fIZrg',
    'https://www.fifa.com/fifaplus/en/watch/Orm8DY9ZfUKa60iQfkTU4g',
    'https://www.fifa.com/fifaplus/en/watch/fdSBZWNGRU24DaEyFo35tA',
    'https://www.fifa.com/fifaplus/en/watch/wSlRFrP5fUCOmvXM65cHlA',
    'https://www.fifa.com/fifaplus/en/watch/f0PDBzheQEme4I9mDxnHSg'
    ]

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(ui[0], self)
        self.setFixedSize(1270, 720)
        self.audio = Audio()
        self.wc = QatarWcApi()
        self.page = 0
        self.visited = []

    def preprocessData(self):
        raw_data = self.wc.getLatestMatch()
        p_data = []
        for elem in raw_data:
            p_data.append([
                elem['type'], elem['local_date'], 
                elem['home_team_en'], elem['away_team_en'], 
                elem['home_score'], elem['away_score'],elem['time_elapsed']
            ])
        return p_data

    def changeShedule(self):
        match_lables = []
        for elem in self.__dict__:
            if 'match' in elem:
                match_lables.append(elem)

        if len(match_lables) != 0:
            s_lables = sorted(match_lables, key=lambda x : int(x[6:]))
            matchInfo = self.preprocessData()
            self.changeScheduleText(s_lables, matchInfo)

    def changeScheduleText(self, lables:list[dict], matchInfo:list):
        per_match_lables = 4 # %51<s%11s
        match_num = len(lables)//per_match_lables
        for i in range(match_num):
            for j in range(per_match_lables):
                if (j+1)%per_match_lables == 1:
                    self.__dict__[lables[i*per_match_lables+j]].setText(
                        f"{matchInfo[i][0]:<56s}{matchInfo[i][1][:-6]}")
                elif (j+1)%per_match_lables == 2:
                    self.__dict__[lables[i*per_match_lables+j]].setText(
                        f"{matchInfo[i][6]}")
                elif (j+1)%per_match_lables == 3:
                    self.__dict__[lables[i*per_match_lables+j]].setText(
                        f"{matchInfo[i][2]:60s}{matchInfo[i][4]}")
                elif (j+1)%per_match_lables == 0:
                    self.__dict__[lables[i*per_match_lables+j]].setText(
                        f"{matchInfo[i][3]:60s}{matchInfo[i][5]}")

    def webOpen(self):
        target = self.sender()
        target_num = int(target.objectName().split('_')[1])
        if self.page in [1, 2]:
            webbrowser.open(highlight_url[target_num-1])
        elif self.page == 4:
            webbrowser.open(news_url[target_num-1])

    def movePage(self):
        target = self.sender()
        target_num = int(target.objectName().split('_')[1])
        uic.loadUi(ui[target_num], self)
        self.page = target_num
        self.visited.append(self.page)
        self.changeShedule()
        
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
