#!/usr/bin/env python3

from gui import Gui
from sudoku_fonction import generate_tableau
from sudoku_fonction import resoudre
from sudoku_fonction import verification_ligne
from sudoku_fonction import verification_colonne

tableau = generate_tableau()


def init_interface(tableau, gui):
    for x, ligne in enumerate(tableau):
        for y, index in enumerate(ligne):
            gui.setValue(x, y, tableau[x][y])


def go():
    init_interface(tableau, gui)
    resoudre(tableau, gui)
    verification_ligne(tableau)
    verification_colonne(tableau)
    #gui.setValue(0, 0, 1)
    #gui.setValue(0, 1, 2)
    #gui.setValue(0, 2, 7)
    #gui.setValue(0, 3, None)
    #gui.setValue(0, 4, 9)
    #gui.setColor(0, 0, "green")
    #gui.setColor(0, 1, "green")
    #gui.setColor(0, 2, "green")
    #gui.setColor(0, 3, "green")
    #gui.setColor(0, 4, "green")

    #gui.setValue(1, 0, 1)
    #gui.setValue(1, 1, 4)
    #gui.setValue(1, 2, 8)
    #gui.setValue(1, 3, "")
    #gui.setValue(1, 4, 9)


#def fin():
    #verification_ligne(tableau)
    #verification_colonne(tableau)


gui = Gui()
gui.setCallBack(go)
gui.start()
