def afficher(*parametres, sep=' ', fin='\n'):
    parametres = list(parametres)
    for i, parametre in enumerate(parametres):
        parametres[i] = str(parametre)
    chaine = sep.join(parametres)
    chaine += fin
    print(chaine, end='')

afficher(2, "un", 2.55)
