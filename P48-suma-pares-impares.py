# Imprimir numeros pares y numeros impares, asi como su suma, hasta un numero n

import os; os.system("cls")

while(True):
    print("Imprimiendo numeros pares a impares de 1 a n y su suna \n")
    n=int(input("Hasta donde deseas los numeros ? "))

    s=0
    print("\nNumeros pares y su suma\n")
    for i in range(2, n+1, 2):
        print(i, end=" ")
        s=s+i
    print("\nla suma es ", s)

    s=0
    print("\nNumeros imapres y su suma\n")
    for i in range(1, n+1, 2):
        print(i, end=" ")
        s = s+i
    print("\nLa suma es", s)

    res=input("\nDeseaas Continuar (S/N) ? ").upper()
    if res=="N": break