# Se desea imprimir los pares de 2 a n y su suma

import os; os.system("cls")

n = int(input("Ingrese un numero: "))
suma_pares = 0

print("Numeros pares: ")
for i in range(2, n+1, 2):
    print(i, end=" ")
    suma_pares += i

print("\nLa suma es: ", suma_pares)