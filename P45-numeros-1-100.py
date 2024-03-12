# Imprimir los numeros de 1 a 100 usando for

import os; os.system("cls")


x = int(input("Hasta donde deseas imprimir? "))
y = int(input("De cuanto en cuanto ? "))
print(f"Imprimiendo numeros de 1 a {x} de {y} en {y} \n")

for n in range(1, x+1, y):
    print(n, end=" ")