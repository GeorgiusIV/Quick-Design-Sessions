
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QHBoxLayout, QToolButton, QLabel
from PyQt5.QtGui import QPixmap, QIcon
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        # initialize window
        super(QMainWindow,self).__init__()

        # define the image widget
        self._imagepath = 'Libby.jpg'
        self._image = QPixmap()
        self._image.load('Libby.jpg')
        self._label = QLabel()
        self._label.setPixmap(self._image)

        # define the button widget
        self._toolButton = QToolButton()
        self._toolButton.clicked.connect(self.btnClicked)
        self._icon = QIcon('PLAYBUTTON.png')
        self._toolButton.setIcon(self._icon)

        # define the widget layout
        layout = QHBoxLayout()
        layout.addWidget(self._toolButton)
        layout.addWidget(self._label)

        # define the mainWindow layout
        self._widget = QWidget()
        self._widget.setLayout(layout)
        self.setCentralWidget(self._widget)

    def btnClicked(self):
        # swap pictures
        if self._imagepath == 'Libby.jpg': self._imagepath = 'Miller.jpg'
        else: self._imagepath = 'Libby.jpg'
        self._image = QPixmap()
        self._image.load(self._imagepath)
        self._label.setPixmap(self._image)


def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()

if __name__ == "__main__":
    main()