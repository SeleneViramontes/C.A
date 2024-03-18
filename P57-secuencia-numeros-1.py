# Se desea imprimir la secuencia de números mostrados el numero de renglones que el usuario desee

import os; os.system("cls")

print("Imprimiendo piramide de numeros\n")
n = int(input("Ingrese el numero de renglones ? "))

for i in range(1, n+1):
    print((str(i) + ' ') * i)