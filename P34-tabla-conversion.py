# Imprimir una tabla de conversion de Peso a Dollar usando while

import os;

while(True):
    os.system("cls")
    tc=17.00

    print("Tabla de conversion de peso a dolar :\n")
    pi = float(input("Valor inicial: "))
    pf = float(input("Valor final :"))

    c=pi
    print("\nPeso\tDollar")
    print ("-"*15)

    while c<=pf:
        print(f"{c}\t{c/tc:.2f}")
        c+=1
    print ("-"*15)

    res =input("Deseas Continur (S/N) ? ") 
    if res.upper()=="N": break