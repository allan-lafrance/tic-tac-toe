import random

def afficher_grille(grille):
    for ligne in grille:
        print(" ".join(ligne))
        print(""*9)
    print()

def jouer(grille, joueur, choix):
    ligne = (choix - 1) // 3 
    colonne = (choix - 1) % 3
    if grille[ligne][colonne] != '-':
        print("Case déjà jouée. Choisissez une autre case.")
        return False
    grille[ligne][colonne] = joueur
    return True

def est_gagnant(grille, joueur):
    # Vérifier les lignes
    for ligne in grille:
        if ligne == [joueur, joueur, joueur]:
            return True
    # Vérifier les colonnes
    for i in range(3):
        if grille[0][i] == joueur and grille[1][i] == joueur and grille[2][i] == joueur:
            return True
    # Vérifier les diagonales
    if grille[0][0] == joueur and grille[1][1] == joueur and grille[2][2] == joueur:
        return True
    if grille[0][2] == joueur and grille[1][1] == joueur and grille[2][0] == joueur:
        return True
    return False

def est_plein(grille):
    for ligne in grille:
        if '-' in ligne:
            return False
    return True

from ia import IA

# Initialiser la grille de jeu
grille = [["-","-","-"], ["-","-","-"], ["-","-","-"]]

# Initialiser le joueur courant
joueur_courant = 'X'

mode_de_jeu = input("Entrez '1' pour joueur contre joueur ou '2' pour joueur contre IA : ")

# Boucle du jeu
while True:
    afficher_grille(grille)
    if mode_de_jeu == '1':
        choix = int(input(f"Joueur {joueur_courant}, entrez le numéro de la case (1-9) où vous souhaitez jouer : "))
    elif mode_de_jeu == '2':
        if joueur_courant == 'X':
            choix = int(input("Entrez le numéro de la case (1-9) où vous souhaitez jouer : "))
        else:
            choix = IA(grille)
    jouer(grille, joueur_courant, choix)
    if est_gagnant(grille, joueur_courant):
        afficher_grille(grille)
        print(f"Le joueur {joueur_courant} a gagné !")
        break
    if est_plein(grille):
        afficher_grille(grille)
        print("Match nul.")
        break
    joueur_courant = 'X' if joueur_courant == 'O' else 'O'