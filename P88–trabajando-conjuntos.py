# Operaciones sobre conjuntos

import os; os.system("cls")

municipios = {"Zacatecas", "Guadalupe","Jerez", "Fresnillo"}

print("Conjuntos y operaciones sobre ellos:")
print(f"{municipios} {len(municipios)} {type(municipios)}")
print("\nAcceder al conjunto usando un ciclo:")

for m in municipios:
    print(m.upper())

print("\nAgregar elementos al conjunto:")
municipios.add("Teul")
municipios.update({"Luis Moya", "Tepetongo"})
print(f"{municipios} {len(municipios)} {type(municipios)}")

print("\nEliminar elementos del conjunto:")
municipios.remove("Zacatecas")
municipios.discard("Ojocaliente")
municipios.pop()
print(f"{municipios} {len(municipios)} {type(municipios)}")

print("\nEliminar todos los elementos del conjunto")
municipios.clear()
print(f"{municipios} {len(municipios)} {type(municipios)}")