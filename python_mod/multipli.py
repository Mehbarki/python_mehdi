#!/usr/bin/python3.7

"""module multipli contenant la fonction table"""

def table(nb, max=10):
    """Fonction affichant la table de multiplication par nb de
    1 * nb jusqu'à max * nb"""
    i = 0
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1

if __name__ == "__main__":
    table(4)
else:
    print("le fichier appelé n'est pas le fichier exécuté")
