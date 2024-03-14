# Imprimir la tabla de multiplicar que el usuario pida hasta donde la pida

import os; os.system("cls")


while(True):
    print("Tabla de multiplicar con for:\n")
    t=int(input("Que tabla deseas ? "))
    n=int(input("Hasta donde la deseas ? "))

    for i in range(1, n+1):
        print(f"\n{t} x {i} ={t*i}")

    res=input("Deseas repetir (S/N) ? ").upper()
    if res=="N": break
