# table de 1 à la valeur de "maxi"  de la valeur "multiplicateur"


def table(nb, maxi=12):
        """fonction de choix de table avec 12 opérations de façon implicite"""

        i = 1

        while i <= maxi:
                print(i, "*", nb, "=", i * nb)
                i += 1


multiplicateur = 0
maxi = 0
maxi = input("maxi = ")
multiplicateur = int(input("multiplicateur = "))

if maxi == "":
        table(multiplicateur)
# execute la fonction "table" avec uniquement le parametre "nb"
else:
        table(multiplicateur, int(maxi))
# execute la fonction "table" avec les 2 parametres "nb" et "maxi"
