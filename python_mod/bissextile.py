#!/usr/bin/python3.7

annee = input("Saisissez une année : ")
annee = int(annee)

if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
    print("l'année saisie est bissextile.")
else:
    print("L'année saisie n'est pas bissextile.")

