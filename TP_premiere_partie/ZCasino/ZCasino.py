#Le casino

#import de toutes les fonction du module "random"
import random
#import de la fonction "ceil" (arrondi >) du module "math"
from math import ceil


#création de la fonction (donne_couleur_tirage)
def donne_couleur_tirage(numero):

    if numero % 2 == 0:
        return "noire"
    else:
        return "rouge"

solde = 0.0

banque = float(input("combien voulez-vous jouer (max = 1000 $)"))

if banque > 1000.0:
    print("jeu max = 1000 $, votre solde est donc de 1000 $")
    solde = 1000.0
else:
    solde = banque

premier_jeu = 1
encaissement = "n"

while solde > 0:

    #question encaissement sautée si premier jeu
    if premier_jeu > 1:
        encaissement = input("voulez-vous encaisser? oui tapez o, non tapez n")
    
    if encaissement == "o":
        print ("vous encaissez ", solde, "$")
        
        if solde > banque:
            bilan = solde - banque
            print ("vous avez gagné %s€ (%s - %s)" % (bilan, solde, banque))
        else:
            bilan = banque - solde
            print("vous avez perdu %s€" % bilan)
        
        #termine le while
        break

    else:
        try:
            jeu = int(input("entrez votre jeu "))
            if jeu >= 50 or jeu < 0:
                raise ValueError

            #appel à fontion (donne_couleur_tirage)
            couleur_jeu = donne_couleur_tirage(jeu)

            mise = float(input("quelle est votre mise "))

            if mise > solde:
                print("mise top importante, votre jeu max est: ", solde)
                continue

        except ValueError:
            print ("la valeur entrée n'est pas un entier de 0 à 49")
            continue

        tirage = int(random.randrange(50))
        #tirage = int(input("numero_essai "))

        #appel à fonction (donne_couleur_tirage)
        couleur_tirage = donne_couleur_tirage(tirage)

        #initialisation
        gain = 0.0
        resultat_couleur = "mauvaise couleur"
        resultat_numero = "mauvais numéro"

        if tirage == jeu:
            resultat_numero = "bon numéro"
            resultat_couleur = "bonne couleur"
            gain = mise * 3

        elif couleur_tirage == couleur_jeu:
            resultat_couleur = "bonne couleur"
            gain = mise * 0.5

        else:
            gain = 0.0

        print ("le tirage est le ", tirage)
        print (resultat_couleur, "et", resultat_numero)

        #arrondi du gain à la valeur >
        gain = ceil(gain)

        print ("votre gain est de ", gain, "$")

        #calcul du nouveau solde
        if gain == 0:
            print ("vous perdez votre mise")
            solde = solde - mise
        else:
            print ("vous gardez votre mise")
            solde = solde + gain

        print ("votre solde est de ", solde, "$")

        premier_jeu += 1

