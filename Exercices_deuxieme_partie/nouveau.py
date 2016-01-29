inventaire = [
    ("pomme", 22),
    ("melon", 4),
    ("poire", 18),
    ("fraise", 76),
    ("prune", 51),
]
inventaire_inverse = [(qtt, nom_fruit) for nom_fruit, qtt in inventaire]

# On n'a plus qu'à trier dans l'ordre décroissant l'inventaire inversé

# On reconstitue l'inventaire trié

inventaire = [(nom_fruit, qtt) for qtt, nom_fruit 
              in sorted(inventaire_inverse, reverse=True)]
