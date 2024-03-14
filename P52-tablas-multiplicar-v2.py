# Imprimir las tablas de multiplicar de la tabla 1 a la n, hasta m

import os; os.system("cls")

print("Imprimiendo las tablas de la tabla 1 a la tabla del 10 hasta el 10\n")
n=int(input("Hasta que tabla quieres ? "))
m=int(input("Hasta donde ? "))



for i in range(1,n+1):
    print(f"\nTabla del {i}")
    for j in range(1,m+1):
        print(f"{i} x {j} = {i*j}")