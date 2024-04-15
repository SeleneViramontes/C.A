# Se tienen los datos de nombres y sueldos de los siguientes trabajadores, en dos listas

import os; os.system("cls")

# Listas de nombres y sueldos
nombres = ["Juan", "Pedro", "Manuel", "Elias", "Maria", "Felipe", "Julia", "Roberto"]
sueldos = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]

# Crear un diccionario con ambas listas
diccionario_sueldos = dict(zip(nombres, sueldos))

# Mostrar el diccionario resultante
print("-"*115)
print("\nDiccionario de sueldos:")
print(diccionario_sueldos)

# Iterar los elementos del diccionario usando las llaves keys()
print("\nIterar usando las llaves:")
for nombre in diccionario_sueldos.keys():
    print(nombre)

# Iterar los elementos del diccionario usando los valores values()
print("\nIterar usando los valores:")
for sueldo in diccionario_sueldos.values():
    print(sueldo)

# Iterar los elementos del diccionario usando la llave y el valor en base a la llave
print("\nIterar usando la llave y el valor en base a la llave:")
for nombre in diccionario_sueldos.keys():
    print(nombre, ":", diccionario_sueldos[nombre])

# Iterar los elementos del diccionario usando el par llave/valor items()
print("\nIterar usando el par llave/valor:")
for nombre, sueldo in diccionario_sueldos.items():
    print(nombre, ":", sueldo)

# Obtener la suma de los sueldos
suma_sueldos = sum(diccionario_sueldos.values())
print("\nSuma de los sueldos:", suma_sueldos)

# Obtener el promedio de los sueldos
promedio_sueldos = suma_sueldos / len(diccionario_sueldos)
print("Promedio de los sueldos:", promedio_sueldos)