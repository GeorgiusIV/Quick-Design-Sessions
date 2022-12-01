

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QByteArray
import sys
import numpy as np


class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()

        # create a label and strap a pixmap to it
        self.im = QPixmap()
        self.im.loadFromData(self.getData())
        self.label = QLabel()
        self.label.setPixmap(self.im)

        self.setCentralWidget(self.label)

    def getData(self):

        # initialise image parameters
        im_width = 5175
        im_height = 3608

        # load the image into a list of appropriate dimensions
        with open('geodil1.jpg','rb') as im:
            f = im.read()
            bar = list()
            for r in range(im_height):
                b = f[r : r + (im_width*3)]
                bar.append(b)

        # convert list to numpy matrix
        rgb_matrix = np.asarray(bar)

        # convert numpy matrix back to bytes
        in_bytes = rgb_matrix.tobytes('F')

        # convert bytes to QBytes for QPixmap
        in_qbytes = QByteArray(in_bytes)

        return in_qbytes


def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()

if __name__ == "__main__":
    main()