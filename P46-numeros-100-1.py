# Imprimir los numeros de 100 a 1 usando for

import os; os.system("cls")

x=int(input("Desde donde ? "))
y =int(input("De cuanto en cuanto ? "))
print(f"Imprimiendo numeros de {x} a 1 de {y} en {y}")

for c in range(x, 0, -y):
    print (c,end=" ")