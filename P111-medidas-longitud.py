# Diseña un programa con dos funciones que convierta: pulgadas a centímetros y metros a pies. Deberá́ mostrar un menú con las opciones correspondientes.

import os

def centimetros(medida):
    return (medida * 2.54 )

def pies(medida):
    return (medida * 3.281)

#programa princial
while True:
    os.system("cls")
    print("[PC] pulgadas a centimetros ")
    print("[MP] metros a pies")
    print("[ S ] alir")
    op = input("Dame la opcion deseada ? ").upper()
    if op=="PC":
        medida = float(input("Dame las pulgadas ? "))
        print(f"Los centimetros son {centimetros(medida)}")
    elif op=="MP":
        medida = float(input("Dame los metros ? "))
        print(f"Los pies son {pies(medida)}")
    elif op=="S":
        print("Acabas de salir del programa")
        break
    else:
        print("\n Opcion invalida ....")

    input("\n<<Presiona caulquier tecla para continuar>>")

print("\nGracias por utilizar este programa")