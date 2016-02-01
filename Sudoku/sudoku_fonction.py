def extrait_ligne(sudoku, index):
    return sudoku[index]


def extrait_colonne(sudoku, index):
    return [ligne[index] for ligne in sudoku]


def extrait_carre(sudoku, ligne, colonne):
    resultat = []
    if ligne < 3:
        ligne = 0
    elif ligne > 5:
        ligne = 2
    else:
        ligne = 1
    if colonne < 3:
        colonne = 0
    elif colonne > 5:
        colonne = 2
    else:
        colonne = 1
    for ux in range(ligne*3, ligne*3+3):
        for uy in range(colonne*3, colonne*3+3):
            resultat.append(sudoku[ux][uy])
    return resultat


def manquant(suite):
    """Renvoi un tableau contenant la liste des nombres manquants
    dans la liste suite"""
    manque = []
    for i in range(1, 10):
        if i not in suite:
            manque.append(i)
    return manque
   
                                     
def commun(liste1, liste2):
    reste = []
    for a in liste1:
        for b in liste2:
            #print(a, b)
            if a == b:
                #print(a)
                #print(reste)
                reste.append(a)
                #print(reste)
    return reste


def avancer(tableau):
    ajout = 0
    reste = []
    for x, ligne in enumerate(tableau):
        for y, index in enumerate(ligne):
            if index == "":
                print(x, y)
                ligne = extrait_ligne(tableau, x)
                #print(ligne)
                colonne = extrait_colonne(tableau, y)
                #print(colonne)
                carre = extrait_carre(tableau, x, y)
                #print(carre)
                #print(manquant(ligne))
                #print(manquant(colonne))
                manquant_ligne = manquant(ligne)
                manquant_colonne = manquant(colonne)
                manquant_carre = manquant(carre)
                reste = commun(manquant_ligne, manquant_colonne)
                reste = commun(reste, manquant_carre)
                print("manque le ", reste)
                print("len = ", len(reste))
                if len(reste) == 1:
                    print("placer ", reste[0], "à la case ", x, y)
                    tableau[x][y] = reste[0]
                    ajout = ajout + 1
                    print("ajout = ", ajout)                 
                   
    return int(ajout)
