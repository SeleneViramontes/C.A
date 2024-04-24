import os

def farnheit(temp):
    return (temp * (9/5) )+ 32

def centigrados(temp):
    return (temp - 32)*(5/9)

#programa princial
while True:
    os.system("cls")
    print("[F] arenheit ")
    print("[C] centigrados")
    print("[ S ] alir")
    op = input("Dame la opcion deseada ? ").upper()
    if op=="F":
        temp = float(input("Dame los centigrados ? "))
        print(f"Los farenheit son {farnheit(temp)}")
    elif op=="C":
        temp = float(input("Dame los farenheit ? "))
        print(f"Los centigrados son {centigrados (temp)}")
    elif op=="S":
        print("Te vas por que tu quieres irte, nadie te obliga")
        break
    else:
        print("\n Opcion invalida ....")

    input("\n<<Presiona caulquier tecla para continuar>>")

print("\nGracias por utilizar este programa")
