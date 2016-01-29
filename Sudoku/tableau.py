l1 = [1, 3, 4]
l2 = [5, 6, 8]
l3 = [9, 5, 4]
tableau = [l1, l2, l3]
print(tableau[2][2])


def extrait_colonne(sudoku, index):

    return [ligne[index] for ligne in sudoku]


def extrait_ligne(sudoku, index):

    return sudoku[index]

print(extrait_ligne(tableau, 0))



