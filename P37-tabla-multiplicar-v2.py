#Imprime las tablas de 1 a n, hasta el 10

import os; os.system("cls")

n = int(input("Hasta que tabla quieres ? "))
t = 1

while t<=n:
    print(f"\nTabla del {t} \n")
    c=1

    while c<=10:
        print(f"{t} x {c} = {t*c}")
        c+=1
    t+=1
print("\nProceso terminado")