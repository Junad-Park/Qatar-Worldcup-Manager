from PyQt6.QtMultimedia import QAudioOutput, QMediaPlayer
from PyQt6.QtCore import QUrl

class Audio():
    def __init__(self):
        # Audio settings
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.audioPath = ["music/승리를위하여.mp3","music/bts.mp3"]
        self.audioIdx = 0

        self.playAudioFile()
    
    def muteAudio(self):
        self.audio_output.setMuted(not self.audio_output.isMuted())

    def nextAudio(self):
        self.player.stop()
        if self.audioIdx == len(self.audioPath)-1:
            self.audioIdx = 0
        else:
            self.audioIdx +=1
        self.playAudioFile()

    def previousAudio(self):
        self.player.stop()
        if self.audioIdx == 0:
            self.audioIdx = len(self.audioPath)
        self.audioIdx -=1
        self.playAudioFile()
        
    def playAudioFile(self):
        file_path = self.audioPath[self.audioIdx]
        self.player.setAudioOutput(self.audio_output)
        self.player.setSource(QUrl.fromLocalFile(file_path))
        self.audio_output.setVolume(50)
        self.player.play()