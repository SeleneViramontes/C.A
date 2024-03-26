# 

import os; os.system('cls')

ciudades = []

print("Capturando nombres de las ciudades\n")

print("Introduce los nombres de n ciudades: $ para terminar:")

while True:
    ciudad= input("Nombre : ")
    if ciudad=="$":
        break
    else:
        ciudades.append(ciudad)

# Imprimir el número de elementos y la lista completa
print(f"\nNombres: {ciudades} , {len(ciudades)}")

# Ordenar la lista en orden descendente
ciudades.sort(reverse=True)
print("Lista ordenada en orden descendente:", ciudades)

# Contar ciudades que comienzan con consonante y mostrar sus nombres
ciudades_consonantes = [ciudad for ciudad in ciudades if not ciudad.lower().startswith(('a', 'e', 'i', 'o', 'u'))]
print("Cantidad de ciudades que inician con consonante:", len(ciudades_consonantes))
print("Ciudades que inician con consonante:", ciudades_consonantes)