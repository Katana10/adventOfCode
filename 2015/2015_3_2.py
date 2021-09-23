fichier = open("path", "r+")
data = fichier.read()
fichier.close()
xPN=0
xR=0
yPN=0
yR=0
listePositions=[]
compteur=0
cadeau=0
for i in data:
    cadeau+=1
    if cadeau%2==0:
        positionActuellePN=[xPN,yPN]
        if positionActuellePN not in listePositions:
            listePositions.insert(compteur,positionActuellePN)
            compteur+=1
        if i == ">":
            xPN+=1
        elif i == "<":
            xPN-=1
        elif i == "^":
            yPN+=1
        elif i == "v":
            yPN-=1
    else:
        positionActuelleR=[xR,yR]
        if positionActuelleR not in listePositions:
            listePositions.insert(compteur,positionActuelleR)
            compteur+=1
        if i == ">":
            xR+=1
        elif i == "<":
            xR-=1
        elif i == "^":
            yR+=1
        elif i == "v":
            yR-=1

cadeau+=1
if cadeau%2==0:
    x=xPN
    y=yPN
else:
    x=xR
    y=yR
positionActuelle=[x,y]
if positionActuelle not in listePositions:
    listePositions.insert(compteur,positionActuelle)
    compteur+=1

print(positionActuelle, compteur, cadeau)
print(listePositions)
