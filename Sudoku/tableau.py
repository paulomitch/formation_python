import sudoku_fonction
#ajout = 2

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

total_ajout = 0
dernier_ajout = 1
while dernier_ajout > 0:
    dernier_ajout = sudoku_fonction.avancer(tableau)
    total_ajout = total_ajout + dernier_ajout
tableau_final = tableau
print("nombre de valeur ajoutée =", total_ajout)
print(tableau_final)

#tableau_final[3][1] = 9
#print(tableau_final)

print(sudoku_fonction.tracer_tableau(tableau_final))

print(sudoku_fonction.verification_carre(tableau_final))

print(sudoku_fonction.verification_ligne(tableau_final))

print(sudoku_fonction.verification_colonne(tableau_final))
