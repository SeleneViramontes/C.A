# Diseña un programa con una función que reciba tres parámetros: dos números (un rango), una letra P o I y nos regrese la suma de números pares o impares en el rango 
# de números especificados.

import os

def suma_p_i(A,B,P_I):
    suma=0

    for i in range(A, B+1):
        if (i%2==0) and (P_I=="P") :
            suma += i
        if (i%2!=0) and (P_I=="I"):
            suma += i
        
    return suma

while True:
    os.system("cls")
    print("[P] pares ")
    print("[I] impares")
    print("[ S ] alir")
    op = input("Dame la opcion deseada ? ").upper()

    if op=="P":
        A = int(input("Desde que numero quieres iniciar ? "))
        B = int(input("Hasta donde ? "))
        print(f"La suma de los pares es {suma_p_i(A,B,op)}")
    elif op=="I":
        A = int(input("Desde que numero quieres iniciar ? "))
        B = int(input("Hasta donde ? "))
        print(f"La suma de los impares es {suma_p_i(A,B,op)}")
    elif op=="S":
        print("Acabas de salir del programa")
        break
    else:
        print("\n Opcion invalida ....")

    input("\n<<Presiona caulquier tecla para continuar>>")

print("\nGracias por utilizar este programa")

