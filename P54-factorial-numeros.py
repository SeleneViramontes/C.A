# Imprime el factorial de n numeros

import os; os.system("cls")

print("Calculando el factorial de n numeros \n")
n=int(input("De cuantos numeros deseas el factorial ? "))

for i in range(1,n+1):
    print(f"{i}!=", end=" ")
    f=1
    for j in range(1,i+1):
        f=f*j
    print(f"{f}")