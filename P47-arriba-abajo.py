#Imprime numeros de 1 a n o de n a 1 segun lo decida el usuario

import os; os.system("cls")

while(True):
    print("\nImprimir los numeros de 1 a n o de n a 1..\n")
    print("[1] Numeros de 1 a n ")
    print("[2] Numeros de n a l ")
    print("[3] Salir ")
    op = int(input("Elige ? "))

    if op==1:
        n=int(input("Hasta donde ? "))
        for c in range(1, n+1):
            print(c, end=" ")
    elif op==2:
        n=int(input("Desde donde ? "))
        for c in range(n, 0, -1):
            print(c, end=" ")
    elif op==3:
        print("Decidiste salir, adios")
        break
    else:
        print("\n0pcion Incorrecta ")

print("\nProceso terminado, gracias por utilizar este programa")