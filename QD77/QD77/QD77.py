from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QMessageBox, QLineEdit, QPushButton, QLabel, QWidget, QComboBox
import ffmpeg
import sys
import os



class Error(Exception):
    pass


class UserExtensionError(Error):
    '''called if the user has not entered a valid extension'''
    pass

class UnsupportedExtension(Error):
    '''called if ffmpeg cannot work with the chosen file extension'''
    pass

class NoFilenameError(Error):
    '''called if a file has a blank name'''
    pass

class OverwriteError(Error):
    '''called if a file would be overwritten'''
    pass






class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        self.inpLabel = QLabel('IN:')
        self.outLabel = QLabel('OUT:')

        self.hBox = QHBoxLayout()
        self.hBox.addWidget(self.inpLabel)
        self.hBox.addWidget(self.outLabel)

        self.inpEdit = QLineEdit()
        self.outEdit = QLineEdit()

        self.filterSelect = QComboBox()
        self.supportedFilters = {'No Filter':None, 'Colour Temperature':'colortemperature'}
        for key in self.supportedFilters.keys(): self.filterSelect.addItem(key)

        self.confBtn = QPushButton('Convert!')
        self.confBtn.clicked.connect(self.processFile)

        self.vBox = QVBoxLayout()
        self.vBox.addWidget(self.inpEdit)
        self.vBox.addWidget(self.filterSelect)
        self.vBox.addWidget(self.outEdit)
        self.vBox.addWidget(self.confBtn)

        self.coreLayout = QVBoxLayout()
        self.coreLayout.addLayout(self.hBox)
        self.coreLayout.addLayout(self.vBox)

        self.widget = QWidget()
        self.widget.setLayout(self.coreLayout)

        self.setCentralWidget(self.widget)


    def processFile(self):
        in_name = self.inp_edit.text()
        in_extension = in_name[:-4]
        out_name = self.out_edit.text()
        out_extension = out_name[:-4]

        selectedFilter = self.supportedFilters[self.filterSelect.currentText()]

        loading = (ffmpeg
                   .input(in_name, format=in_extension)
                   .filter_(in_name, selectedFilter)
                   .output(out_name, format=out_extension))

        loading.run()

    def validateInputs(self):
        in_name = self.inp_edit.text()
        out_name = self.out_edit.text()

        supported_extensions = ['.mov','.mp4']

        # check if the string is long enough to contain an filename + extension
        if len(in_name) > 5:

            # store the filename + extension
            filename = in_name[:-4]
            extension = in_name[-4:]
            
            # check the extension is of the format '.XXX'
            if extension[0] != '.' or '.' in extension[1:4]:
                raise UserExtensionError

            # check the extension is supported
            if extension not in supported_extensions:
                raise UnsupportedExtension

            # check the filename is not a duplicate within the file
            path = os.path.abspath(filename)
            directory = os.path.dirname(path)



def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()


if __name__ == "__main__":
    main()
