instruction=[]
somlist=[]
compteur=-1
comparateur=0
somme=0
# Extract data.
with open('data.txt', 'r') as file:
    for row in file:
        instruction.append(int(row.replace('\n','')))

# print(type(instruction))

# for i in instruction:
#     i=int(i)
#     if (i>comparateur):
#         compteur+=1
        
#     comparateur=i

# print(compteur)

for i in range(0, len(instruction)-2):
    somme = instruction[i] + instruction[i+1] + instruction[i+2]
    somlist.append(somme)
    somme=0

for i in somlist:
    
    if (i>comparateur):
        compteur+=1
        
    comparateur=i

print(compteur)