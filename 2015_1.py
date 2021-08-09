fichier = open("path", "r+")
data = fichier.read()
fichier.close()
# print(data)
etage=0
compteur=0
for i in data:
    compteur+=1
    if i == "(":
        etage+=1
    elif i == ")":
        etage-=1
    if etage==-1:
        print(compteur)
print("Il est à l'étage:",etage)
