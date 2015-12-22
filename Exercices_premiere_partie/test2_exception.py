try:
    resultat = numerateur / denominateur
except NameError:
    print ("la variable numerateur ou denominateur n'est pas définie")
except TypeError:
    print ("la variable numerateur ou denominateur n'est pas un nombre")
except ZeroDivisionError:
    print ("le denominateur est égal à 0")


# capture et affichage d'un message d'exception

numerateur = 5
denominateur = 0

try:
    resultat = numerateur / denominateur

except ZeroDivisionError as exception_retournee:
    print ("voici l'erreur:", exception_retournee)
