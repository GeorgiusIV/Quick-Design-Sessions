
import cv2 as cv
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
import sys


def filter_frame(vframe, selected_filter = None):

    def example_long(vframe):
        '''
        a bunch of code here
        to do a more complicated idea
        '''
        
        pass

    newvframe = vframe
    selected_filter = selected_filter.lower()

    if selected_filter == 'blur':
        newvframe = cv.blur(vframe, (3,3))
    
    
    elif selected_filter == 'smooth':
        pass
    
    
    else:
        pass


    return newvframe 



def MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()

        n = 4
        self.pixmap = QPixmap()
        self.loadframe(4)
        self.label = QLabel()
        self.label.setPixmap = self.pixmap
        self.setCentralWidget(self.label)


    def loadFrame(n):
        #plt.imshow(vframes[n])
        self.pixmap.load('Libby.jpg')

def main():

    filename = 'SimpsonsShot14.mov'
    video = cv.VideoCapture(filename)

    # load video frames into vframe
    vframes = list()
    while True:
        frame_exists,vframe = video.read()
        vframes.append(vframe)
        if not frame_exists:
            break

    # handle Qt Window
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    mainWindow.show()
    app.exec()

if __name__ == "__main__":
    main()