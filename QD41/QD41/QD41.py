
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QPixmap
import matplotlib.pyplot as plt
import numpy as np
import ffmpeg
import sys

FIXED_VIDEO_WIDTH = 800

def loadFile():
    
    height,width = 720,960

    process = (ffmpeg
               .input('SimpsonsShot14.mov')
               .output('pipe:', format='rawvideo', pix_fmt='rgb24')
               .run_async(pipe_stdout = True))

    vframes = list()
    while True:
         
        in_bytes = process.stdout.read(height*width*3)
        if not in_bytes:
            break
        
        rgb_matrix = np.frombuffer(in_bytes,np.uint8)
        rgb_matrix = np.reshape(rgb_matrix,[height,width,3])

        vframes.append(rgb_matrix)

    return vframes



class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()

        self.BlackBar1 = QLabel()
        self.VideoFrame = QLabel()
        self.BlackBar2 = QLabel()

        self.BlackBar1_im = QPixmap()
        self.VideoFrame_im = QPixmap()
        self.BlackBar2_im = QPixmap()

        
        self.VLayout = QVBoxLayout()
        self.HLayout = QHBoxLayout()
        self.HLayout.addLayout(self.VLayout)

        self.VLayout.addWidget(self.BlackBar1)
        self.VLayout.addWidget(self.VideoFrame)
        self.VLayout.addWidget(self.BlackBar2)

        self.widget = QWidget()
        self.widget.setLayout(self.HLayout)
        self.setCentralWidget(self.widget)

    def updateFrame(self,rgb_matrix):

        #image = rgb_matrix.tobytes()
        #print(image)
        #self.VideoFrame_im.loadFromData(image)
        self.VideoFrame_im.load(plt.imshow(rgb_matrix))
        self.VideoFrame_im.scaledToWidth(FIXED_VIDEO_WIDTH)
        

    def getBlackBars(self):
        
        videoHeight = self.VideoFrame_im.height
        BBHeight = 800 - videoHeight//2

        zeroes = np.zeroes([BBHeight,FIXED_VIDEO_WIDTH])
        image = plt.imshow(zeroes)
        self.BlackBar1_im.setPixmap(image)
        self.BlackBar2_im.setPixmap(image)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    vframes = loadFile() 
    mainWindow.show()
    for frame in vframes:
        mainWindow.updateFrame(frame)
        input()
    mainWindow.getBlackBars()
    
    app.exec()


