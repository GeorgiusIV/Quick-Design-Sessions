
from PyQt5.QtWidgets import QApplication, QGridLayout, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
from scipy.io import wavfile as wav
import matplotlib.pyplot as plt
import numpy as np
import sys


GLOBAL_AUDIO_IMAGE_NAME = 'audioIMG'

class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()

        # create Pixmap
        self.audioPNG = QPixmap()
        self.label = QLabel()
        self.label.setPixmap(self.audioPNG)

        # create Gridlayout
        self.grid = QGridLayout()
        self.grid.addWidget(self.label,1,1)
        self.setLayout(self.grid)


    def takeVisualisation(self):
        self.audioPNG.load(GLOBAL_AUDIO_IMAGE_NAME)
        self.setCentralWidget = self.audioPNG

class AudioObject():
    def __init__(self,filepath):
        self._samplerate, self._data = wav.read(filepath)
        self.nChannels = self._data.shape[0]
        self.nSamples = self._data.shape[1]
        self.LChannel = self._data[0]
        self.RChannel = self._data[1]
        self.length = self.nSamples / self._samplerate

    def getVisualisation(self):
        time = np.linspace(0, self.length, self.nSamples)
        plt.plot(time, self.LChannel)
        plt.savefig(GLOBAL_AUDIO_IMAGE_NAME)

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    filepath = 'SimpsonsShot14.wav'
    audioObject = AudioObject(filepath)
    audioObject.getVisualisation()
    mainWindow.takeVisualisation()
    mainWindow.show()
    app.exec()

if __name__ == "__main__":
    main()

