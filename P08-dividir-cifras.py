# Dividir un numero entero de 3 cifras en sus digitos individuales

import os; os.system("cls")
print("Dividiendo en unidades, decenas, centenas, un numero entero\n")

num= int(input("Dame un numero entero de 3 cifras: "))

unidades=num%10
num//=10
decenas=num%10
num//=10
centenas=num%10
num//=10
millar=num


print(f"Millares: {millar}, Centenas: {centenas}, Decenas: {decenas}, Unidades: {unidades} ")