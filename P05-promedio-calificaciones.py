# Calcular el promedio de 3 calificaciones

import os #importa la libreria os que contiene funciones relacionadad al sistema

os.system("cls") # cls en windows

print("Calculando el proimedio de 3 calificaciones\n")

print("Dame 3 calificaciones separadas por espacio (pueden tener decimales) :")
c1, c2, c3=input().split()
c1, c2, c3= float(c1), float(c2), float(c3)

prom=(c1+c2+c3)/3

print(f"El promedio de {c1}, {c2}, {c3} es {prom:.2f}")
