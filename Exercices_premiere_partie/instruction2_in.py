a = input("entrer des lettres ")

a_une_voyelle = False

for lettre in a:
    if lettre in "aeiouy":
        a_une_voyelle = True
        break


if a_une_voyelle:
    print (a, " a une voyelle")
else:
    print (a, " n'a pas voyelle")
