l0 = [1, "", "", "", 5, 2, "", 9, 3]
l1 = ["", 7, "", 1, 9, "", "", 5, 2]
l2 = [5, "", "", "", 7, 3, "", "", ""]
l3 = ["", "", 2, "", "", 7, "", "", 8]
l4 = [8, 3, "", "", "", "", 9, 1, ""]
l5 = ["", "", "", 3, "", "", "", 6, 7]
l6 = ["", "", "", 5, 2, "", "", "", 1]
l7 = [4, 5, 1, 7, 3, "", "", "", ""]
l8 = [2, 9, 3, "", "", 4, 6, "", ""]

tableau = [l0, l1, l2, l3, l4, l5, l6, l7, l8]

#print(tableau[0][0])
#if (tableau[1][0]) == (""):
#    print("rien")


def extrait_ligne(sudoku, index):
    return sudoku[index]


def extrait_colonne(sudoku, index):
    return [ligne[index] for ligne in sudoku]


def extrait_carre(sudoku, ligne, colonne):
    resultat = []
    for x in range(ligne*3, ligne*3+3):
        for y in range(colonne*3, colonne*3+3):
            resultat.append(sudoku[x][y])
    return resultat


def manquant(suite):
    manque = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in (suite):
        for j in (manque):
            if i == j:
                manque.remove(i)
    return manque
x = 2
y = 2
print(extrait_ligne(tableau, x))
ligne = extrait_ligne(tableau, x)

print(extrait_colonne(tableau, y))
colonne = extrait_colonne(tableau, y)

print(extrait_carre(tableau, x, y))
carre = extrait_carre(tableau, x, y)

print(manquant(ligne))
print(manquant(colonne))
print(manquant(carre))

y = 0
x = 0
blanc = []

for x, ligne in enumerate(tableau):
    for y, index in enumerate(ligne):
        if index == "":
            print (x, y)
            blanc.append([x, y])
            #liste des coordonnées (ligne, colonne) des cases blanches
print(blanc)

i = 0
j = 0
reste = []
while i < len(blanc):
    (x, y) = blanc[i]
    print(x, y)
    ligne = extrait_ligne(tableau, x)
    colonne = extrait_colonne(tableau, y)
    print(manquant(ligne))
    print(manquant(colonne))
    for i in enumerate(manquant(ligne)):
        print(i)
        for j in enumerate(manquant(colonne)):
            if i == j:
                reste.append(i)
            j = j + 1
        i = i + 1
    print(reste)
