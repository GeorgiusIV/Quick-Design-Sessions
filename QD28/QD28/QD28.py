
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider
from random import randint
import cv2 as cv
import numpy as np
import sys



class VideoObj():
    def __init__(self,filepath):
        video = cv.VideoCapture(filepath)
        self.vframes = [frame for frame in video.read()]
        self.nframes = len(self.vframes)

    def applyFilter(self,frame,filterName):
        return frame

    def randomFrame(self):
        idx = randint(0,self.nframes-1)
        return self.vframes[idx], idx

    def saveImage(self,filename,img):
        cv.imwrite(filename,img)

    def findSimilarity(self,frameIDX1, frameIDX2):
        suggestedSlices = list()
        frame1 = self.vframes[frameIDX1]
        frame2 = self.vframes[frameIDX2]
        edge1 = cv.Canny(frame1,150,250)
        edge2 = cv.Canny(frame2,150,250)
        sharedEdges = np.multiply(edge1,edge2)
        similarity = np.sum(sharedEdges)

        return similarity

    def findSlices(self):
        suggestedSlices = list()
        for f in range(vframes):
            if f != 0: similarity = self.findSimilarity(f,f-1)
            if similarity:
                if similarity < threshold:
                    suggestedSlices.append(f)
        return suggestedSlices
            
        
class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()

        slider = QSlider()
        self.setCentralWidget(slider)


def main():
    app = QApplication(sys.argv)
    video = VideoObj('SimpsonsShot14.mov')
    video.saveImage('TEST_IMAGE.png', video.applyFilter(video.randomFrame(),'BLUR'))
    idx1 = randint(1,10)
    idx2 = randint(1,10)
    video.findSimilarity(idx1,idx2)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()

if __name__ == "__main__":
    main()
