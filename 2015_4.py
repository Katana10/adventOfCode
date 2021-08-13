import hashlib

string='iwrupvqb'
number='1'
string=string+number
# function 
result = hashlib.md5(string.encode())
while result.hexdigest()[0:6] != '000000':
    string=string[0:8]+number
    result = hashlib.md5(string.encode())
    number=int(number)+1
    number=str(number)
    
    
# printing the equivalent byte value.
print("Le hash est fini, voici le resultat pour l'entree :",string,":\n")
print(result.hexdigest())