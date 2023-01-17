import random

def IA(grille):
    choix = random.randint(1, 9)
    while grille[(choix - 1) // 3][(choix - 1) % 3] != "-":
        choix = random.randint(1, 9)
    return choix
