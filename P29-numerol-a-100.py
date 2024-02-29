# Imprime numeros de 1 a n, en incrementos de i

import os; os.system("cls")

n = int(input("Hasta donde ? "))
i = int(input("Incremento ? "))

c=1
while c<=n:
    print(c, end=" ")
    c=c+i