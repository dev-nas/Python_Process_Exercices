#1/ programme complètement procédural

x = 1
y = 2
print(x + y)
....
#2/ ajout d'une fonction: saut d'adressage
def add(x, y):
    is_odd(x)
    # après l'exécution de la fonction, le programme va récupérer l'adresse de la pile
    return x + y

#3/ deuxième fonction: interêt d'une structure en pile
def is_odd(x):
    return not x % 2

px = 1
y = 2
# ici le processus va cacher l'adresse de l'instruction dans la pile
z = add(x, y)
print(z)


