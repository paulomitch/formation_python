# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cell_ui.ui'
#
# Created: Sun Jan 31 18:24:09 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Cell(object):
    def setupUi(self, Cell):
        Cell.setObjectName("Cell")
        Cell.resize(94, 50)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(Cell.sizePolicy().hasHeightForWidth())
        Cell.setSizePolicy(sizePolicy)
        Cell.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Lato")
        Cell.setFont(font)
        self.cell_frame = QtWidgets.QFrame(Cell)
        self.cell_frame.setGeometry(QtCore.QRect(0, 0, 50, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cell_frame.sizePolicy().hasHeightForWidth())
        self.cell_frame.setSizePolicy(sizePolicy)
        self.cell_frame.setStyleSheet("Qframe {border: 5px;\n"
"    background-color: rgb(217, 217, 217);\n"
"border-radius: 10px;}")
        self.cell_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.cell_frame.setObjectName("cell_frame")
        self.label = QtWidgets.QLabel(self.cell_frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Cell)
        QtCore.QMetaObject.connectSlotsByName(Cell)

    def retranslateUi(self, Cell):
        _translate = QtCore.QCoreApplication.translate
        Cell.setWindowTitle(_translate("Cell", "Form"))

