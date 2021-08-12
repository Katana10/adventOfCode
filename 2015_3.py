fichier = open("D:\JEU créé\IA\Réflexions\AdventOfCode\data3.txt", "r+")
data = fichier.read()
fichier.close()
x=0
y=0
listePositions=[]
compteur=0
cadeau=0
for i in data:
    positionActuelle=[x,y]
    if positionActuelle not in listePositions:
        listePositions.insert(compteur,positionActuelle)
        compteur+=1
    cadeau+=1
    if i == ">":
        x+=1
    elif i == "<":
        x-=1
    elif i == "^":
        y+=1
    elif i == "v":
        y-=1
positionActuelle=[x,y]
if positionActuelle not in listePositions:
    listePositions.insert(compteur,positionActuelle)
    compteur+=1
cadeau+=1
print(positionActuelle, compteur, cadeau)
print(listePositions)
