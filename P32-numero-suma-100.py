#Imprime numeros de 1 a 200, hasta alcanzar la suma de 100

import os; os.system("cls")

c=0
s=0

while c <=200:
    c+=1
    s+=c
    print(c, end=" ")
    if s>=2350:
        break

print(f"\nHemos alcanzado la meta {s}, sumando {c} numeros")