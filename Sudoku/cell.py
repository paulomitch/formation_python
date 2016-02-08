from PyQt5.QtWidgets import QWidget
from cell_ui import Ui_Cell


class Cell(QWidget, Ui_Cell):
    def __init__(self, parent):
        super(Cell, self).__init__(parent)
        self.setupUi(self)
        
