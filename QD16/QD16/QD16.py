from bs4 import BeautifulSoup as bs
from PyQt5.QtWidgets import QMainWindow, QTableView, QApplication
from PyQt5.QtCore import Qt, QAbstractTableModel
import sys
import requests


def getPTagsFromUrl(url):
    page = requests.get(url)
    soup = bs(page.text,'html.parser')
    ptags = soup.findAll('p')
    return ptags

# (aside) index must be part of the QAbstractTableModel
# you must then define a class for it
# Define the Abstract Model for the Table
class TableModel(QAbstractTableModel):
    def __init__(self,data):
        super(TableModel,self).__init__()
        self._data = data

    def data(self,index,role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self,index):
        return len(self._data)

    def columnCount(self,index):
        return len(self._data[0])

# Define the Main Window that will include the Table inside.
class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()
        self.table = QTableView()

        data = [getPTagsFromUrl('https://www.politifact.com/personalities/donald-trump/'),['test']]

        self.model = TableModel(data)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
