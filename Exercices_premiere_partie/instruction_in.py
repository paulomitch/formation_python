a = input("entrer une lettre ")

if a == "":
    print ("vous n'avez pas entré de lettre")
elif a in "aeiouy":
#le contenu de "a" est-il dans la chaine "aeiouy"
    print (a, "est une voyelle")
else:
    print (a, "est une  consonne")
