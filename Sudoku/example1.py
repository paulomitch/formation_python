#!/usr/bin/env python3

from gui import Gui
from sudoku_fonction import generate_tableau2
from sudoku_fonction import resoudre
from sudoku_fonction import avancer
from sudoku_fonction import avancer_plus
from sudoku_fonction import verification_ligne
from sudoku_fonction import verification_colonne

tableau = generate_tableau2()
#print(tableau)


def init_interface(tableau, gui):
    print(tableau)
    for x, ligne in enumerate(tableau):
        for y, index in enumerate(ligne):
            gui.setValue(x, y, tableau[x][y])


def go():
    #ajout = 0
    #init_interface(tableau, gui)
    #resoudre(tableau, gui)
    #ajout = 0
    #avancer(tableau, gui)
    print(avancer(tableau, gui))
    #if ajout == 0:
        #avancer_plus(tableau, gui)
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
init_interface(tableau, gui)
#gui.setCallBack(go)
gui.start()


