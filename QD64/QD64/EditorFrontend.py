
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QToolButton, QToolBar, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap, QIcon
import pyaudio
from threading import Thread
import time

import EditorBackend as bknd

class ReusableThread(Thread):
    def __init__(self, *args, **kwargs):
        Thread.__init__(self,*args,**kwargs)
        self._default_args = self._target, self._args, self._kwargs

    def run(self,*args,**kawrgs):
        super().run()
        self.reset(*args,**kawrgs)

    def reset(self,*args,**kwargs):
        self._target = self._default_args[0]
        self._args = args or self._default_args[1]
        self._kwargs = kwargs or self._default_args[2]

class EditorWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()

        
        
        # create instances of audio and video to be modified by the GUI
        self.video = bknd.Video()
        self.audio = bknd.Audio()

        # create a stream for audio playback
        p = pyaudio.PyAudio()
        self.audioStream = p.open(format = pyaudio.paInt16,
                                  channels = 2,
                                  rate = 48000,
                                  output = True)

        # create upper central lower layouts
        self.createUpperLayout()
        self.createCentralLayout()
        self.createLowerLayout()

        # add layouts to main-layout
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.upperLayout)
        self.mainLayout.addLayout(self.centralLayout)
        self.mainLayout.addLayout(self.lowerLayout)

        # display main-layout
        self.widget = QWidget()
        self.widget.setLayout(self.mainLayout)
        self.setCentralWidget(self.widget)


    def createUpperLayout(self):

        self.upperLayout = QVBoxLayout()
        #self.upperLayout.setFixedSize(1000,100)


    def createCentralLayout(self):

        # creating input box for loadFile
        self.loadFileInput = QLineEdit(self)
        self.loadFileInput.setFixedWidth(100)

        # creating tool buttons for the central-left-layout toolbar
        self.loadFile = QToolButton()
        self.loadFile.clicked.connect(self.clickLoadFile)
        self.loadFile.setIcon(QIcon('loadFile.png'))

        self.saveFile = QToolButton()
        self.saveFile.clicked.connect(self.clickSaveFile)
        self.saveFile.setIcon(QIcon('saveFile.png'))
        self.saveFile.setEnabled(False)

        self.playFile = QToolButton()
        self.playFile.clicked.connect(self.clickPlayFile)
        self.playFile.setIcon(QIcon('playbackAV.png'))
        self.playFile.setEnabled(False)

        self.pauseFile = QToolButton()
        #self.pauseFile.clicked.connect(self.clickPauseFile)
        self.pauseFile.setIcon(QIcon('pauseAV.jpg'))
        self.pauseFile.setEnabled(False)

        self.stopFile = QToolButton()
        #self.stopFile.clicked.connect(self.clickStopFile)
        self.stopFile.setIcon(QIcon('stopAV.png'))
        self.stopFile.setEnabled(False)

        # adding tools to toolbar
        self.toolbar = QToolBar()
        self.toolbar.addWidget(self.loadFile)
        self.toolbar.addWidget(self.loadFileInput)
        self.toolbar.addWidget(self.playFile)
        self.toolbar.addWidget(self.pauseFile)
        self.toolbar.addWidget(self.stopFile)
        
        # creating remaining widgets for central-left-layout
        self.selectionWindow = QLabel()                 # WIDGET TO BE DECIDED

        # adding objects to the central-left-layout
        self.centralLeftLayout = QVBoxLayout()
        self.centralLeftLayout.addWidget(self.toolbar)
        self.centralLeftLayout.addWidget(self.selectionWindow)

        # creating video-player for central-right-layout
        self.videoFigure = plt.figure(facecolor='black')
        self.videoAxes = self.videoFigure.add_subplot()
        self.videoAxes.set_axis_off()
        self.videoFigure.subplots_adjust(0,0,1,1)
        self.videoImage = self.videoAxes.imshow(bknd.getEmptyFrame(720,960))
        self.videoCanvas = FigureCanvas(self.videoFigure)
        self.videoCanvas.setFixedSize(600,400)
        
        # adding objects to the central-right-layout
        self.centralRightLayout = QVBoxLayout()
        self.centralRightLayout.addWidget(self.videoCanvas)
        self.centralRightLayout.setSizeConstraint(3)
        #self.centralRightLayout.setFixedSize(600,600)

        # adding central-left and central-right to the central-layout
        self.centralLayout = QHBoxLayout()
        self.centralLayout.addLayout(self.centralLeftLayout)
        self.centralLayout.addLayout(self.centralRightLayout)

    def createLowerLayout(self):

        # creating audio-timeline canvas for lower-layout
        self.aTimeFigure = plt.figure(facecolor='white')
        self.aTimeAxes = self.aTimeFigure.add_subplot()
        self.aTimeFigure.subplots_adjust(0,0,1,1)
        self.aTimeAxes.set_axis_off()
        self.aTimeCanvas = FigureCanvas(self.aTimeFigure)
        self.aTimeCanvas.setFixedHeight(100)

        # creating video-timeline canvas for lower-layout
        self.vTimeFigure = plt.figure(facecolor='white')
        self.vTimeAxes = self.vTimeFigure.add_subplot()
        self.vTimeFigure.subplots_adjust(0,0,1,1)
        self.vTimeAxes.set_axis_off()
        self.vTimeCanvas = FigureCanvas(self.vTimeFigure)
        self.vTimeCanvas.setFixedHeight(100)

        # creating exception-report object for lower-layout
        self.exceptionReport = QLabel('EXCEPTIONS',self)

        # adding objects to lower-layout
        self.lowerLayout = QVBoxLayout()
        self.lowerLayout.addWidget(self.vTimeCanvas)
        self.lowerLayout.addWidget(self.aTimeCanvas)
        self.lowerLayout.addWidget(self.exceptionReport)
        self.lowerLayout.setSizeConstraint(3)

    def clickLoadFile(self):
        try: 
            aframes, vframes = bknd.loadFile(self.loadFileInput.text())
            
            # create audio and video objects with the information that was loaded
            self.audio.setaframes(aframes)
            self.video.setvframes(vframes)
            
            # display audio timeline and video frame
            self.displayWaveForm()
            self.displayVFrame(0)

            # enable tool buttons
            self.playFile.setEnabled(True)
            self.pauseFile.setEnabled(True)
            self.stopFile.setEnabled(True)
            
            # begin at the first frame for video playback
            self.nframe = 0

        except Exception as e:
            raise e
        finally:
            self.loadFileInput.setText('')

    def clickSaveFile(self):
        pass

    def clickPlayFile(self):

        # initialize break conditions
        self.paused = False
        self.stopped = False

        audioThread = ReusableThread(target = self.playAudio)
        videoThread = ReusableThread(target = self.playVideo)
        audioThread.start()
        videoThread.start()

        # play through video until is paused, stopped, or finishes

        videoThread.run()
        audioThread.run()
        
        #how do I check if the button is pressed

        # the threads must contain the loops

    def playVideo(self, nframe = 0):

        while nframe < 1400:
            self.displayVFrame(nframe)
            nframe += 1
            time.sleep(0.04)

    def playAudio(self, nframe = 0):

        while nframe < 1400:
            self.playAFrame(nframe)
            nframe += 1
            time.sleep(0.04)


    def clickPauseFile(self):
        print('PAUSED')
        self.paused = True

    def clickStopFile(self):
        self.stopped = True


    def displayVFrame(self, nframe):
        
        vframe = self.video.vframes[nframe]
        self.videoImage.set_data(vframe)
        self.videoCanvas.draw()
        self.videoCanvas.flush_events()


    def playAFrame(self, nframe):

        aframe = self.audio.aframes[nframe]
        self.audioStream.write(aframe.tobytes())



            

    def displayWaveForm(self):
        data = (self.audio.LChannel)
        self.aTimeAxes.plot(data, scalex=1000, scaley=100)
        self.aTimeCanvas.draw()
        #self.aTimeCanvas.flush_events()




def main():
    app = QApplication(sys.argv)
    Editor = EditorWindow()
    Editor.show()
    app.exec()

if __name__ == "__main__":
    main()