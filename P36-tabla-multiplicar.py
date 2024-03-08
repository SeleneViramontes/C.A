# Imprime la tabla de multiplicar deseada de 1 a n

import os

while(True):
    os.system("cls")

    print("Imprimiendo la tabla de multiplicar deseada:\n")
    t=int(input("Que tabla quieres ? "))
    n=int(input("Hasta donde       ?"))
    c=1

    while c<=n:
        print(f"{t} x {c} = {t*c}")
        c+=1

    res=input("Deseas Continuar (S/N) ? ")
    if res.upper()=="N": break

print("\nProceso terminado")