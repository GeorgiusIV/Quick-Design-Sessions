from scipy.io import wavfile as wav
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolButton
from PyQt5.QtGui import QIcon
import sys
import pyaudio

class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()

        self.button = QToolButton() 
        self.button.setIcon(QIcon('PLAYBUTTON.jpg'))
        self.setCentralWidget(self.button)


class Audio():
    def __init__(self,filepath):
        self.samplerate, self.data = wav.read(filepath)
        self.nchannels = self.data.shape[1]
        self.nsamples = self.data.shape[0]
        self.length = self.nsamples / self.samplerate
        self.LChannel = self.data[0]
        self.RChannel = self.data[1]

    def __next__(self):
        n = self.nframe
        self.nframe += 1
        return self.LChannel[n], self.RChannel[n]

    def __iter__(self):
        self.nframe = 0
        return self

    def streamer(self):
        samplewidth = 2
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(samplewidth),
                       channels = self.nchannels,
                       rate = self.samplerate,
                       output = True)
        return stream



def main():
    app = QApplication(sys.argv)
    audio = Audio('SimpsonsShot14.wav')
    stream = audio.streamer()
    for LData, RData in audio:
        stream.write(LData)
        stream.write(RData)
    stream.stop_stream()
    stream.close()
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()

if __name__ == "__main__":
    main()