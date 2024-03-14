#Calcula el factorial de un numero

import os; os.system("cls")

print("Imprimiendo el factorial de un numero \n")
n=int(input("Dame un numero entero ? "))

f=1
for i in range(1, n+1):
    f=f*i
print(f"\nEl factorial es {f}")