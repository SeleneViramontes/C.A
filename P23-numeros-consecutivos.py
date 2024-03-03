# Dados tres números enteros, verificar si son consecutivos (9,10,11) y mandar mensaje confirmándolo, 
#si no lo son (1,4,6) mandar mensaje de error.

import os; os.system("cls")

print("Verificando si los numeros ingresados son consecutivos:")
print("Puedes ingresar cualquier serie de 3 numeros: \n")
print("Ingrese 3 numeros enteros, separados por espacio ? ")

n1, n2, n3=input().split()
n1, n2, n3= int(n1), int(n2), int(n3)

if (n3 - n2) == 1 and abs(n2 - n1) == 1:
    print(f"{n1} , {n2} y {n3} son consecutivos ")
else:
    print(f"{n1} , {n2} y {n3} no son consecutivos")