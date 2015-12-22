annee = input("Saisissez une année supérieure à 0 :")

try:
    
    annee = int(annee)  # Conversion de l'année

    assert annee > 0

except ValueError:

    print("Vous n'avez pas saisi un nombre.")

except AssertionError:

    print("L'année saisie est inférieure ou égale à 0.")
