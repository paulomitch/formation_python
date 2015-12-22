annee = int(input("entrer une annee  "))
#print ("vous avez choisi ",annee)
#print ("par 4 = ",annee % 4)
#print ("par 100 = ",annee % 100)
#print ("par 400 = ",annee % 400)
resultat = "non définie"

if (annee % 4 == 0) and (annee % 100 != 0):
# si annee est un nombre divisible par 4 et pas divisible par 100
        resultat = ("bissextile")


elif (annee % 400 == 0):
#si annee est un nombre divisible par 400
        resultat = ("bissextile")

else:
        resultat = ("non bissextile")

if (annee < 2015):
        print ("cette annee était une annee ", resultat)
elif (annee > 2015):
        print ("cette annee sera une annee ", resultat)
else:
        print ("cette annee est ", resultat)

