from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject
from gui_ui import Ui_MainWindow
from cell import Cell
from PyQt5.QtWidgets import QApplication
import sys


class Gui(QMainWindow, Ui_MainWindow):

    def __init__(self):
        app = QApplication(sys.argv)
        QObject.__init__(self)
        super(Gui, self).__init__()
        self.app = app
        self.setupUi(self)
        self.gridLayoutWidget.setStyleSheet("background-color: "
                                            "rgb(117,117,117);")
        self.cell_matrix = [[None for y in range(9)]
                            for x in range(9)]

        for f_x in range(3):
            for f_y in range(3):
                frame = QtWidgets.QFrame(self.gridLayoutWidget)
                widget = QtWidgets.QWidget(frame)
                widget.setStyleSheet("background-color: rgb(170,170,170);")
                # widget.setGeometry(QRect(160, 170, 160, 80))
                gridLayout = QtWidgets.QGridLayout(widget)

                gridLayout.setContentsMargins(0, 0, 0, 0)
                for x in range(3):
                    for y in range(3):
                        cell = Cell(self)
                        self.cell_matrix[(f_x*3)+x][(f_y*3)+y] = cell
                        cell.setStyleSheet("QLabel{background-color: white;}")
                        gridLayout.addWidget(cell, y, x)
                self.grid.addWidget(frame, f_y, f_x)

        self.show()

    def setCallBack(self, callback):
        if not callable(callback):
            raise TypeError("callback is not a function : %s"
                            % str(type(callback)))
        self.goButton.clicked.connect(callback)

    def start(self):
        self.app.exec_()

    def setValue(self, x, y, value):
        if type(x) != int:
            raise TypeError("Invalid type for x : %s must be a int" % type(x))
        if x < 0 or x > 8:
            raise ValueError("Invalid x index : %s must be in [0;9]" % x)
        if type(y) != int:
            raise TypeError("Invalid type for y : %s must be a int" % type(y))
        if y < 0 or y > 8:
            raise ValueError("Invalid y index : %s must be in [0;9]" % x)

        if value == "" or value is None:
            text = ""
        else:
            text = str(value)
        self.cell_matrix[x][y].label.setText(text)

    def setColor(self, x, y, color):
        if type(x) != int:
            raise TypeError("Invalid type for x : %s must be a int" % type(x))
        if x < 0 or x > 8:
            raise ValueError("Invalid x index : %s must be in [0;9]" % x)
        if type(y) != int:
            raise TypeError("Invalid type for y : %s must be a int" % type(y))
        if y < 0 or y > 8:
            raise ValueError("Invalid y index : %s must be in [0;9]" % x)

        self.cell_matrix[x][y].setStyleSheet("QLabel{background-color: %s;}"
                                             % color)
