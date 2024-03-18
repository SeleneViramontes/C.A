# Se desea imprimir la secuencia de números mostrados el numero de renglones que el usuario desee:

import os; os.system("cls")

print("Imprimiendo piramide de numeros\n")
n=int(input("Cuantos renglones ? "))


for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print("\r")