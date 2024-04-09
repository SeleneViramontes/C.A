# Procesar los nombres y edades en un diccionario

import os; os.system("cls")

datos={}

print(f"Datos {datos}, {len(datos)}")

print("Introduce nombres y edades (nombre vacio para terminar):")
while True:
    nombre= input("Dame el nombre ? ")
    if nombre!='':
        datos[nombre] = int(input("Dame la Edad ? "))
        #datos ['Peso'] = float(input("Peso ?"))
    else:
        break

print(f"Datos {datos}, {len(datos)}")

print("\nListado de nombres y edades, con suma y promedio")
s=p=0

for n, e in datos.items():
    print(f"{n:<20} - {e:3}")
    s=s+e

p=s/len(datos)
print(f"\nLa suma es {s} y El promedio es {p}")