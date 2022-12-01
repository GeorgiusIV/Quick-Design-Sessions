
from PyQt5.QtWidgets import QGridLayout, QWidget, QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt
import sys

starting_sudoku = [[9,0,0,5,0,0,0,6,0],
                   [0,0,6,0,4,0,0,8,2],
                   [7,0,0,2,8,0,3,0,0],
                   [4,8,2,1,0,0,0,5,6],
                   [0,1,7,0,5,9,0,3,0],
                   [3,9,5,6,2,0,0,0,0],
                   [0,7,0,0,0,5,6,0,8],
                   [0,0,9,7,6,0,0,0,3],
                   [2,0,4,3,0,0,0,7,9]]


class MainWindow(QMainWindow):
    def __init__(self,grid):
        super(QMainWindow,self).__init__()

        labels = list()
        
        for i in range(0,81):
            new_label = QLabel()
            entry = str(grid.get(i))
            new_label.setText(entry)
            new_label.setAlignment(Qt.AlignCenter)
            labels.append(new_label)
        
        layout = QGridLayout()

        for i,label in enumerate(labels):
            layout.addWidget(label,i//9,i%9)
        
        base = QWidget()
        base.setLayout(layout)
        self.setCentralWidget(base)

def modifyDict(d):
    return d

grid = dict()
index = 0
for row in starting_sudoku:
    for entry in row:
        grid.update({index:entry})
        index += 1
    

app = QApplication(sys.argv)
mainWindow = MainWindow(grid)
mainWindow.show()
app.exec()

