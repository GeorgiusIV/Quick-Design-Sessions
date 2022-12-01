
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import ffmpeg


class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()

        # creating figure canvas for matplotlib
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        # create textbox
        self.txtbox = QLineEdit()

        # creating button and activation function
        self.button = QPushButton('Load File', self)
        self.button.clicked.connect(self.readtxt)

        # create layout and adding items
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.canvas)
        self.layout.addWidget(self.txtbox)
        self.layout.addWidget(self.button)

        # creating widget for layout and setting it for window
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

    def readtxt(self):

        # getting the text
        filename = self.txtbox.text()
        self.txtbox.setText('')

        # loading in the file
        f = open(filename)
        
        # reading the file and creating data
        i = 0
        l = 'firstline'
        x = list()
        y = list()
        while l:
            i += 1
            l = f.readline()
            x.append(i)
            y.append(len(l))

        # plotting the values
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(x,y)
        self.canvas.draw()



    def plotVideo(self):
 
        # getting textbox text
        filename = self.txtbox.text()
        self.txtbox.setText('')

        # loading in the file
        process = (ffmpeg
                   .input(filename)
                   .output('pipe:', format='rawvideo', pix_fmt='rgb24')
                   .run_async(pipe_stdout = True))

        # reading the file
        while True:
            in_bytes = process.stdout.read(height*width*3)
            if not in_bytes:
                break

            # convert bytes to matrix
            rgb_matrix = np.asarray(in_bytes)
            rgb_matrix = np.reshape(rgb_matrix,[height,width,3])




def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()

if __name__ == "__main__":
    main()




