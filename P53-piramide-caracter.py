# Imprimiendo piramide de un caracter determinado

import os; os.system("cls")

print("Imprimiendo piramide del caracter deseado\n")
n=int(input("Cuantos renglones ? "))
car=input("Caracter ? ")

for i in range(1,n+1):
    for j in range(1,i+1):
        print(car, end=" ")
    print("\r")