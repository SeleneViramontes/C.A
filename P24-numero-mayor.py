# Dados tres números enteros, verificar cual es el mayor

import os; os.system("cls")

print("Ingrese 3 numeros enteros, separados por espacio ? ")

n1, n2, n3=input().split()
n1, n2, n3= int(n1), int(n2), int(n3)

if n1>n2 and n1>n3:
    print(f"El numero mayor es: {n1}")
elif  n2>n1 and n2>n3:
    print(f"El numero mayor es: {n2}")
elif n3>n1 and n3>n2:
    print(f"El numero mayor es: {n3}")