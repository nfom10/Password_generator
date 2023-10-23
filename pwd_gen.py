from random import choice
from string import ascii_letters , digits
rango = [6,7,8,9,10,11,12]
print("#"*49)
print("# ")
print("# Se han generado 5 contraseñas: ")
print("# ")
for a in range(5):
    password = ''.join([choice (ascii_letters + digits) for i in range(choice(rango))])
    print("# "+str(a+1)+"> ", password)
print("# ")
print("#"*49)
