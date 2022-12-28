import sys
import cv2
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QMainWindow, QWidget, QPushButton, QApplication,
                             QLabel, QFileDialog, QStyle, QVBoxLayout)
from multiscreens import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.init_ui()
               
        pass  # end of __init__ function 
    def init_ui(self):
        self.mediaPlayer_1.setVideoOutput(self.videoWidget_1)
        self.mediaPlayer_2.setVideoOutput(self.videoWidget_2)
        self.mediaPlayer_3.setVideoOutput(self.videoWidget_3)
        self.mediaPlayer_4.setVideoOutput(self.videoWidget_4)
        self.mediaPlayer_5.setVideoOutput(self.videoWidget_5)
        self.mediaPlayer_6.setVideoOutput(self.videoWidget_6)
        self.mediaPlayer_7.setVideoOutput(self.videoWidget_7)
        self.mediaPlayer_8.setVideoOutput(self.videoWidget_8)
        self.open_video_btn.clicked.connect(self.open_file)
        self.close_button.clicked.connect(self.close)
        self.play_btn.clicked.connect(self.play_video)
        pass   # end of init_ui
    def open_file(self):
        self.filename, _ = QFileDialog.getOpenFileName(self, "Open Video")  
        
    def play_video(self):   
        if self.filename != '':
            combvalue = self.comboBox.currentText()
            combvalue = int(combvalue)
            if combvalue >= 1:
               self.mediaPlayer_1.setMedia(QMediaContent(QUrl.fromLocalFile(self.filename)))
               self.mediaPlayer_1.play()
               if combvalue >= 2:
                  self.mediaPlayer_2.setMedia(QMediaContent(QUrl.fromLocalFile(self.filename)))
                  self.mediaPlayer_2.play()
                  if combvalue >= 3:
                     self.mediaPlayer_3.setMedia(QMediaContent(QUrl.fromLocalFile(self.filename)))
                     self.mediaPlayer_3.play()
                     if combvalue >= 4:
                        self.mediaPlayer_4.setMedia(QMediaContent(QUrl.fromLocalFile(self.filename)))
                        self.mediaPlayer_4.play()
                        if combvalue >= 5:
                           self.mediaPlayer_5.setMedia(QMediaContent(QUrl.fromLocalFile(self.filename)))
                           self.mediaPlayer_5.play()
                           if combvalue >= 6:
                              self.mediaPlayer_6.setMedia(QMediaContent(QUrl.fromLocalFile(self.filename)))
                              self.mediaPlayer_6.play()
                              if combvalue >= 7:
                                 self.mediaPlayer_7.setMedia(QMediaContent(QUrl.fromLocalFile(self.filename)))
                                 self.mediaPlayer_7.play()
                                 if combvalue >= 8:
                                    self.mediaPlayer_8.setMedia(QMediaContent(QUrl.fromLocalFile(self.filename)))
                                    self.mediaPlayer_8.play()         

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())