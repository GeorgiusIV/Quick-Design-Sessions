
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QByteArray

import numpy as np
from PIL import Image
import sys



class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()

        self.widget = QWidget()
        self.im = QPixmap()
        print(self.im.loadFromData(self.getNPARRAY()))
        self.label = QLabel()
        self.label.setPixmap(self.im)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)

        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)


    def getNPARRAY(self):
        
        RGB_matrix = Image.open('Libby.jpg')
        RGB_matrix = np.asarray(RGB_matrix)
        print(RGB_matrix)
        #RGB_matrix = RGB_matrix.astype(np.ubyte)
        
        tobytes = bytearray(RGB_matrix.data)
        #print(tobytes)

        return QByteArray(tobytes)



def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()


if __name__ == "__main__":
    main()



