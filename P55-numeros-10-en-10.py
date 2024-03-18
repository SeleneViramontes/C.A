# Se desea imprimir los números de 1 a n de 10 en 10

import os; os.system("cls")

n = int(input("Ingrese un numero: "))
print("El resultado es:")
for i in range(1, n+1, 10):
    print(f"{i}", end=" ")