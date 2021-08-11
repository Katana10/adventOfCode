#Initialisation des variables que l'on ne reset pas à chaque ligne
compteur=0
taille=0
ruban=0
longueur=0
largeur=0
hauteur=0
#Ouverture du fichier
fichier = open("D:\JEU créé\IA\Réflexions\AdventOfCode\data2.txt", "r+")
##Pour lire le fichier en entier
# data = fichier.read()
##Pour lire un fichier ligne par ligne
line = fichier.readline()
while line:
    #Partie 1
    petit=0
    #On enlève ce qui ne nous intéresse pas dans la ligne et on isole chaque nombre
    nombres=line.split("x")
    #On transfomre les chaine de caractère en entier pour nous faciliter les calculs
    nombres[0]=int(nombres[0])
    nombres[1]=int(nombres[1])
    nombres[2]=int(nombres[2])
    #(Facultatif) On met les valeurs correspondantes dans chaque variable
    longueur=nombres[0]
    largeur=nombres[1]
    hauteur=nombres[2]

    #Comparasion pour tourver le plus petit côté mais c'est pas le plus efficace 
    #Le plus efficace est de faire comme dans la partie 2
    cote1=longueur*largeur
    cote2=largeur*hauteur
    cote3=hauteur*longueur

    taille=2*(longueur*largeur + largeur*hauteur + hauteur*longueur)
    if((cote1<=cote2)and(cote1<=cote3)):
        petit=cote1
    elif((cote2<=cote1)and(cote2<=cote3)):
        petit=cote2
    elif((cote3<=cote1)and(cote3<=cote2)):
        petit=cote3
    taille+=petit
    compteur+=taille
    
    #Partie 2
    arc = 0
    arc = longueur*largeur*hauteur
    nombres.sort()
    
    ruban = ruban + 2*nombres[0] + 2*nombres[1] + arc

    # utilisez readline() pour lire la ligne suivante
    line = fichier.readline()
print(compteur)
print(ruban)
fichier.close()

 