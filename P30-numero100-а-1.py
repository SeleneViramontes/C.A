# Imprime los numeros de n a 1 en incrementos de i

import os; os.system("cls")

n = int(input("Desde donde ? "))
i = int(input("Decremento ? "))

c=n
while c>=1:
    print(c, end=" ") 
    c=c-i