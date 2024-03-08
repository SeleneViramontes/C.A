# Calcula e imprime la conjetura de collatz

import os;

while(True):

    os.system("cls")

    print("Imprimiendo los números de la conjetura de collatz:\n") 
    num=int(input("Dame un número entero positivo ? "))

    while num !=1:
        print(num, end=" ")
        if num%2==0:
            num //=2
        else:
            num=num*3+1

    print(num)

    res = input("Deseas Continur (S/N) ? ")
    if res.upper()=="N": break

print("\nProceso terminado")