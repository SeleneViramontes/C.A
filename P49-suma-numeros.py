# Suma y promedio de numeros introducidos por el usuario

import os; os.system("cls")

print("Suma y promedio de n numeros introducidos por el usuario\n")

n=int(input("Cuantas calificaciones deseas capturar ? "))

suma=promedio=0

for i in range(1, n+1):
    print(f"Calificacion {i}: ", end=" ")
    x=float(input())
    suma=suma + x

promedio=suma/n
print(f"La suma de calificaciones es {suma}, el promedio es {promedio}")