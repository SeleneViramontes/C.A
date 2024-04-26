# Diseña un programa con una función que pida 3 números enteros y devuelva el menor de ellos, usando una función

import os;

def menor(c1, c2, c3):
    men = 0

    if c1<c2 and c1<c3 :
        men=c1
    elif c2<c1 and c2<c3:
        men=c2
    elif c3<c1 and c3<c2:
        men=c3
    return men

os.system("cls")
#print(mayor(100,100,100))
print("Dame 3 calificaciones y te dire cual es la menor de ellas")
a,b,c=float(input()), float(input()), float(input())
r=menor(a,b,c)

if r==0:
    print("Las calificaciones son iguales")
else:
    print(f"La calificacion menor es {r}")