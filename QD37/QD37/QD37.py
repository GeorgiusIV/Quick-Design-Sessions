

### GUI MODULE ###

from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QApplication, QToolButton
from PyQt5.QtGui import QPixmap
import matplotlib.pyplot as plt
import ffmpeg


class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()

        self.editorWindow = QWidget()
        self.playbackController = QWidget()

        self.ones = QVBoxLayout()
        self.ones.addWidget(self.topToolbar)
        self.ones.addWidget(self.editorWindow)
        self.ones.addWidget(self.playbackController)


        self.tens = QHBoxLayout()


    def createTopToolbar(self):

        self.minimize = QToolButton()
        self.expand = QToolButton()
        self.exit = QToolButton()

        self.minimize.connect(self.minimize)

        self.topToolbar = QHBoxLayout()
        self.topToolbar.addWidget(self.minimize)
        self.topToolbar.addWidget(self.expand)
        self.topToolbar.addWidget(self.exit)

    def minimize(self):
        pass

    def getvframes(self):
        pass

    def updateFrame(self,vframe):
        image = plt.imshow(vframe)
        self.videoFrame.load(image)


### BACKEND ### 
# all returns are numpy arrays

# backend.py
class VideoEditor():
    def __init__(self):
        self.vframes = list()

    def splitFrames(self):
        pass

    def applyFilter(self, filter_name = str()):
        '''
        uses OpenCV2 to apply various filters to all video frames

        '''

        if filter_name == 'blur':
            pass
        elif filter_name == 'edge':
            pass
        else:
            pass
        
        self.vframes = newvframes

    def getvframes(self):
        return self.vframes


class AudioEditor():
    def __init__(self):
        self.aframes = list()
        self.LChannel = list()
        self.RChannel = list()
        self.sample_rate = int()
        self.nsamples = len(list())
        self.length = self.nsamples / self.sample_rate

    def getaframes(self):
        return self.aframes

    def getChannelAudio(self):
        return self.LChannel, self.RChannel

