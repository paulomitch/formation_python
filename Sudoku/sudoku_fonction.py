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


def avancer(tableau, gui):
    ajout = 0
    reste = []
    for x, ligne in enumerate(tableau):
        for y, index in enumerate(ligne):
            if index == "":
                #print(x, y)
                ligne = extrait_ligne(tableau, x)
                #print(ligne)
                colonne = extrait_colonne(tableau, y)
                #print(colonne)
                carre = extrait_carre(tableau, x, y)
                #print(carre)
                #pint(manquant(ligne))
                #pint(manquant(colonne))
                manquant_ligne = manquant(ligne)
                #print(manquant_ligne)
                if len(manquant_ligne) == 1:
                    print("red")
                    if manquant_ligne not in colonne and carre:
                        print("manque le ", manquant_ligne[0], "ligne ", x)
                        tableau [x][y] = manquant_ligne[0]
                        gui.setColor(x, y, "red")
                        gui.setValue(x, y, manquant_ligne[0])
                        ajout = ajout + 1

                manquant_colonne = manquant(colonne)
                #print(manquant_colonne)
                if len(manquant_colonne) == 1:
                    print("yellow")
                    if manquant_colonne not in ligne and carre:
                        print("manque le ", manquant_colonne[0], "colonne ", y)
                        tableau [x][y] = manquant_colonne[0]
                        gui.setColor(x, y, "yellow")
                        gui.setValue(x, y, manquant_colonne[0])
                        ajout = ajout + 1
                manquant_carre = manquant(carre)
                #print(manquant_carre)
                if len(manquant_carre) == 1:
                    print("orange")
                    if manquant_carre not in ligne and colonne:
                        print("manque le ", manquant_ligne[0], "carré ", x,y)
                        tableau [x][y] = manquant_carre[0]
                        gui.setColor(x, y, "orange")
                        gui.setValue(x, y, manquant_carre[0])
                        ajout = ajout + 1
                        
                if ajout == 0:
                    reste = commun(manquant_ligne, manquant_colonne)
                    reste = commun(reste, manquant_carre)
                    print("manque le ", reste)
                    #print("len = ", len(reste))
                    if len(reste) == 1:
                        print("placer ", reste[0], "à la case ", x, y)
                        tableau[x][y] = reste[0]
                        gui.setColor(x, y, "green")
                    #s = input("taper \"s\" pour suite")
                    #if s == s:
                        gui.setValue(x, y, reste[0])
                        ajout = ajout + 1
                    #print("ajout = ", ajout)
    if ajout == 0:
        avancer_plus(tableau, gui)

    return ajout


def affiche_2_valeurs(liste):
    valeur = " ".join(liste)
    return valeur


def avancer_plus(tableau, gui):
    for x, ligne in enumerate(tableau):
        for y, index in enumerate(ligne):
            if index == "":
                ligne = extrait_ligne(tableau, x)
                colonne = extrait_colonne(tableau, y)
                carre = extrait_carre(tableau, x, y)
                manquant_ligne = manquant(ligne)
                manquant_colonne = manquant(colonne)
                manquant_carre = manquant(carre)
                #print(manquant_ligne)
                if len(manquant_ligne) == 2:
                    valeur = manquant_ligne
                    print(valeur)
                    if manquant_ligne[0] in manquant_colonne and manquant_carre:
                        print(manquant_ligne[0])
                        gui.setColor(x, y, "grey")
                        gui.setValue(x, y, manquant_ligne[0])
                        tableau[x][y] = manquant_ligne[0]
                #print("colonne ", x, y, manquant_colonne)
                #print(manquant_carre)


#def 2_manquants_ligne:
    #if manquant_ligne[0] in manquant_carre:
        


def resoudre(tableau, gui):
    total_ajout = 0
    dernier_ajout = 1
    while dernier_ajout > 0:
        dernier_ajout = avancer(tableau, gui)
        total_ajout = total_ajout + dernier_ajout
        tableau_final = tableau
        print("nombre de valeur ajoutée =", total_ajout)
        print(tableau_final)
    dernier_ajout = avancer_plus(tableau, gui)


def tracer_tableau(tableau):
    print("+---+---+---+---+---+---+---+---+---+")
    for ligne in tableau:
        nb = " | ".join([str(i) for i in ligne])
        print("|", nb, "|")
        print("+---+---+---+---+---+---+---+---+---+")


#def verification_carre(tableau):
    x = 0
    y = 0

    for x in [0, 3, 6]:
        for y in [0, 3, 6]:
            carre = extrait_carre(tableau, x, y)
            carre_verif = set(carre)
            if len(carre_verif) == 9:
                coin = (tableau[x][y])
                print("carré de coin", coin, "OK")
            #else:
                #print("carré de coin", coin, y, "faux")

def verification(liste, x, nom):
    ref = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if "" in liste:
        print(nom, x, liste, "fausse")
    elif ref == list(set(liste)):
        print(nom, x, liste, "bonne")
    else:
        print(nom, x, liste, "fausse")



def verification_ligne(tableau):
    for x in range(0, 9):
        ligne = extrait_ligne(tableau, x)
        nom = "ligne"
        verification(ligne, x, nom)


def verification_colonne(tableau):
    for x in range(0, 9):
        colonne = extrait_colonne(tableau, x)
        nom = "colonne"
        verification(colonne, x, nom)


def generate_tableau1():
    l0 = [4, 3, 6, "", "", 7, "", "", ""]
    l1 = [2, 9, 1, "", "", 6, 4, "", ""]
    l2 = ["", "", 8, "", 4, "", "", "", ""]
    l3 = [5, "", "", "", 1, "", "", 8, 3]
    l4 = ["", 1, 9, 2, "", 5, 7, "", 6]
    l5 = [6, "", 4, "", 3, "", "", 5, 2]
    l6 = [8, "", "", "", "", 1, 2, 3, ""]
    l7 = ["", "", 2, 4, 7, 3, "", "", ""]
    l8 = ["", 4, "", "", "", 8, "", 9, ""]

    tableau = [l0, l1, l2, l3, l4, l5, l6, l7, l8]

    return tableau


def generate_tableau():
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

    return tableau


def generate_tableau2():
    l0 = ["", "", 2, 4, "", "", "", 1, 3]
    l1 = [8, 3, "", "", "", 1, "", "", ""]
    l2 = ["", "", "", 2, "", "", 6, "", ""]
    l3 = ["", "", "", "", 5, "", "", "", 4]
    l4 = [3, 9, "", "", "", "", "", "", ""]
    l5 = ["", "", "", 7, "", "", 9, "", ""]
    l6 = ["", 7, "", "", "", "", "", 3, ""]
    l7 = [1, 2, 5, "", "", "", "", "", 9]
    l8 = ["", "", "", 8, "", "", 4, "", 5]

    tableau = [l0, l1, l2, l3, l4, l5, l6, l7, l8]

    return tableau
