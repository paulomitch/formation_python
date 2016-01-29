def afficher_flottant(flottant):
    if type(flottant) is not float:
        raise TypeError(("la valeur doit être un flottant, type : "
                         + str(type(flottant))))

    flottant = str(flottant)
    partie_entiere, partie_flottante = flottant.split(".")
    return ",".join([partie_entiere, partie_flottante[:3]])

valeur = float((input("entrer un nombre décimal")))
resultat = afficher_flottant(valeur)
print(resultat)

