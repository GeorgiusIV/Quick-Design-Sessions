
import sys
import ffmpeg
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QVBoxLayout
import matplotlib.pyplot as plt
import numpy as np

class MainWindow(QMainWindow):
    def __init__(self, vframes):
        super(QMainWindow,self).__init__()

        self.vframes = vframes

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot()
        self.ax.imshow(self.vframes[0])
        self.canvas = FigureCanvas(self.fig)

        self.setCentralWidget(self.canvas)


def getFrames(filename):

    height,width = 720,960
    
    process = (ffmpeg
               .input(filename)
               .output('pipe:',format='rawvideo',pix_fmt='rgb24')
               .run_async(pipe_stdout=True))

    vframes = list()
    while True:
        in_bytes = process.stdout.read(height*width*3)
        if not in_bytes:
            break

        rgb_matrix = np.frombuffer(in_bytes,np.uint8)
        rgb_matrix = np.reshape(rgb_matrix,[height,width,3])

        vframes.append(rgb_matrix)

    print(vframes)
    return vframes


def main():
    app = QApplication(sys.argv)
    vframes = getFrames('SimpsonsShot14.mov')
    mainWindow = MainWindow(vframes)
    mainWindow.show()
    app.exec()
    
main()