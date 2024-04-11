# Procesa los datos de varios autos en una lista de diccionarios

import os; os.system("cls")

autos = [
{"Marca": "Ford", "Modelo": "Focus", "Año":2000}, 
{"Marca":"VW", "Modelo": "Jetta", "Año":2015}
]

print(autos, len(autos), type(autos))
autos.append({"Marca": "Ford", "Mustang":"Jetta", "Año":1964})
print(autos, len(autos), type(autos))

print("Todos los autos, uno a uno:")
for auto in autos:
    print(auto)

print("\nDatos de un auto en particular:")

for k,v in autos[0].items():
    print(k,v)

print("\nDatos de todos los autos en forma tabla:")
for auto in autos:
    for k,v in auto.items():
        print(f"{k:<12} : {v}")
    print()