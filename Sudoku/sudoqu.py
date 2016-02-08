import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication)
from PyQt5.QtCore import QObject
from gui_ui import Ui_MainWindow
from cell import Cell


class Gui(QMainWindow, Ui_MainWindow):

    def __init__(self):
        QObject.__init__(self)
        super(Gui, self).__init__()

        self.cell_matrix = [[None for y in range(10)]
                            for x in range(10)]

        for x in range(10):
            for y in range(10):
                cell = Cell(self)
                self.cell_matrix[x][y] = cell
                self.grid.addWidget(cell, y, x)

        self.show()

    def setCallBack(self, callback):
        self.goButton.clicked.connect(callback)

    def start(self):
        app = QApplication(sys.argv)
        app.exec_()
