
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtGui import QPixmap
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
import sys




class Video():
    def __init__(self, filepath):
        video = cv.VideoCapture(filepath)
        self.vframes = list()
        frames_exist = True
        while frames_exist: 
            print('INSIDE')
            frames_exist, frame = video.read()
            self.vframes.append(frame)
            cv.waitKey(1)
        self.nframes = len(self.vframes)

    def __next__(self):
        if self.nframe < self.nframes:
            n = self.nframe
            n += 1
            return self.vframes[n]
        else:
            return StopIteration

    def __iter__(self):
        self.nframe = 0
        return self

class PixMap(QWidget):
    def __init__(self):
        super(QWidget,self).__init__()


class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()

        self.im = None
        self.label = QLabel()
        self.widget = QWidget()
        self.Horizontal = QHBoxLayout()
        self.Vertical = QVBoxLayout()
        self.Vertical.addLayout(self.Horizontal)
        self.Vertical.addWidget(self.label)
        self.widget.setLayout(self.Vertical)
        

        self.setCentralWidget(self.widget)

    def setPIXMAP(self, filepath):
        self.im = QPixmap(filepath)
        self.label.setPixmap(self.im)
          
        
def main():
    app = QApplication(sys.argv)
    filepath = 'SimpsonsShot14.mov'
    video = Video(filepath)
    mainWindow = MainWindow()
    mainWindow.show()
    for frame in video:
        mainWindow.setPIXMAP(plt.imshow(frame,))
    
    app.exec()

if __name__ == "__main__":
    main()