#!/usr/bin/python3.7

import random, math

#----------------------------------------------------------------Fonctions du ZCasino-------------------------------------------------------------------------------#

def menu():                                                      # Affiche le menu du Casino
    print("Bievenue au ZCasino")
    print("-------------------------------------------")
    print("Voici les jeux auxquels vous pouvez jouez : ")
    print("1 - Roulette russe")
    print("2 - Plus ou Moins")

def regle_roulette():                                             # Affiche les règles de la roulette russe
    print("Rappel des règles !")
    print("-------------------")
    print("""Le joueur mise sur un numéro compris entre 0 et 49 (50 numéros en tout). En choisissant son numéro, il y dépose la somme qu'il souhaite miser.
    La roulette est constituée de 50 cases allant naturellement de 0 à 49. Les numéros pairs sont de couleur noire, les numéros impairs sont de couleur rouge.
    Le croupier lance la roulette, lâche la bille et quand la roulette s'arrête, relève le numéro de la case dans laquelle la bille s'est arrêtée.
    Dans notre programme, nous ne reprendrons pas tous ces détails « matériels » mais ces explications sont aussi à l'intention de ceux qui ont eu la chance
    d'éviter les salles de casino jusqu'ici. Le numéro sur lequel s'est arrêtée la bille est, naturellement, le numéro gagnant.
    Si le numéro gagnant est celui sur lequel le joueur a misé (probabilité de 1/50, plutôt faible), le croupier lui remet 3 fois la somme misée.
    Sinon, le croupier regarde si le numéro misé par le joueur est de la même couleur que le numéro gagnant
    (s'ils sont tous les deux pairs ou tous les deux impairs). Si c'est le cas, le croupier lui remet 50 % de la somme misée.
    Si ce n'est pas le cas, le joueur perd sa mise""")

def menu_roulette():                                               # Affiche le menu roulette
    print("Bienvenue au jeux de la Roulette russe")
    print("--------------------------------------")
    print("1 - Voir les règles")
    print("2 - Jouez !")
    print("3 - Retour au menu principal")

def estPair(nb, nb2):                                              # Verifie si le nbJoueur est de la même couleur que le nbRoulette
    if nb % 2 == 0 and nb2 % 2 == 0:
        return 0
    elif nb % 2 != 0 and nb2 % 2 != 0:
        return 1

def jeuxRoulette():                                                  # Déroule le jeux de la roulette
    nbRoulette = random.randrange(50)
    solde = int(input("Veuillez rentrez votre solde : "))
    continu = 1
    count = 0
    while continu == 1:
        nbJoueur = int(input("Choisissez votre numéro sur lequel miser : "))
        miseJoueur = int(input("Choisissez votre mise: "))

        if nbRoulette == nbJoueur:                                    # Verifie si le nbJoueur = nbRoulette
            print("Bravo, vous avez miser sur le bon numéro : ", nbRoulette ,",vous remportez 3x votre mise !")
            solde = miseJoueur + (miseJoueur * 3)
            print("Votre solde est de : ", solde)

        elif estPair(nbJoueur, nbRoulette) == 1 or estPair(nbJoueur, nbRoulette) == 0: # Verifie si le nbJoueur est de la même couleur que nbRoulette grâce à estPair()
            solde = miseJoueur + (math.ceil(0.5 * miseJoueur))                         # Arrondie le chiffre au-dessus exem: 50% de 3€ = 1.5€, on lui rendra 2€ et non 1.5€
            print("Bravo votre numéro est de la même couleur que le nouméro gagnant : ", nbRoulette)
            print("Vous remportez 50% de votre mise, votre solde est de : ", solde)

        else:
            solde = solde - miseJoueur
            print("Perdu, vous perdez votre mise, le numéro gagnant est : ", nbRoulette)
            print("Votre solde est de : ", solde)

        count = count + 1
        print("Vous êtes à votre ", count, "partie(s)")
        continu = int(input("Voulez vous rejouez ? (oui = 1 / non = 0) "))

def menuPlusOuMoins():                                 # Affiche le menu du Plus ou Moins
    print("Bienvenue dans le jeu du Plus ou Moins")
    print("--------------------------------------")
    print("1- Un joueur")
    print("2- Deux joueur")

def jeuxPlusOuMoins():
    count = 0
    print("Plus ou Moins")
    print("-------------")
    continu = 1
    while continu == 1:
        print("Vous jouez contre l'ordinateur")
        nbPlusOuMoins = random.randrange(100)
        nbJoueur = int(input("Entrez votre estimation: "))
        while nbJoueur != nbPlusOuMoins:
            count = count + 1
            if nbJoueur > nbPlusOuMoins:
                print("C'est moins !")
                nbJoueur = int(input("Entrez votre estimation: "))

            elif nbJoueur < nbPlusOuMoins:
                print("C'est plus !")
                nbJoueur = int(input("Entrez votre estimation: "))

            
            print("Bravo, vous avez trouvé le chiffre mystère : ", nbPlusOuMoins, " en ", count, "coup(s)")
            continu = int(input("Voulez vous rejouez ? (oui = 1 / non = 0) "))

def jeuxPlusOuMoins2():
    count = 0
    print("Plus ou Moins")
    print("-------------")
    continu = 1
    while continu == 1:
        print("Vous jouez en 1v1")
        nbPlusOuMoins = int(input("Le joueur1 va choisir un chiffre en 0 et 100: "))
        nbJoueur = int(input("Joueur2 veuillez entrer votre estimation: "))
        while nbJoueur != nbPlusOuMoins:
            count = count + 1
            if nbJoueur > nbPlusOuMoins:
                print("C'est moins !")
                nbJoueur = int(input("Entrez votre estimation: "))

            elif nbJoueur < nbPlusOuMoins:
                print("C'est plus !")
                nbJoueur = int(input("Entrez votre estimation: "))
            else:
                print("Bravo, vous avez trouvé le chiffre mystère : ", nbPlusOuMoins, " en ", count, "coup(s)")
                continu = int(input("Voulez vous rejouez ? (oui = 1 / non = 0) "))
# ------------------------------------------------------------ Début du code -------------------------------------------------------------------------------#
menu()

nbJeux = int(input("Veuillez choisir votre jeu : ")) # Conversion de string en int

if nbJeux == 1:
    menu_roulette()
    nbRegles = int(input("Choisissez votre mode de jeux : ")) # Conversion de string en int

    if nbRegles == 1:
        regle_roulette()

    elif nbRegles == 2:
        jeuxRoulette()

    elif nbRegles == 3:
        menu()

elif nbJeux == 2:
    menuPlusOuMoins()
    nbRegles = int(input("Choisissez votre mode de jeux : ")) # Conversion de string en int

    if nbRegles == 1:
        jeuxPlusOuMoins()

    elif nbRegles == 2:
        jeuxPlusOuMoins2()
else:
    while nbJeux != 1 or nbJeux != 2:
        nbJeux = int(input("Veuillez choisir votre jeu : "))
        print("Veuillez entrez un numéro correspondant à un jeux")

