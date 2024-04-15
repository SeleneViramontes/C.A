# Cree un diccionario de llave de cadena municipios con los siguientes elementos

import os; os.system("cls")

Municipios={"Apozol" : 1863, "Calera" : 1868, 
            "Fresnillo" : 1554, "Guadalupe" : 1821, 
            "Jalpa" : 1824, "Jerez" : 1824, 
            "Loreto" : 1931, "Mazapil" : 1824, "Momax" : 1857
            }

# Mostrar el diccionario completo
print("Diccionario de países completo:")
print(Municipios)

# Eliminar Apozol usando del
del Municipios["Apozol"]
print("\nDiccionario después de eliminar 'Apozol' con del:")
print(Municipios)

# Eliminar Fresnillo usando pop()
Municipios.pop("Fresnillo")
print("\nDiccionario después de eliminar 'Fresnillo' con pop:")
print(Municipios)

# Eliminar Momax usando popitem()
Municipios.popitem()
print("\nDiccionario después de eliminar Momax con popitem:")
print(Municipios)

# Borrar todos los elementos del diccionario con clear()
Municipios.clear()

# Mostrar el diccionario completo después de borrar los elementos
print("\nDiccionario después de borrar todos los elementos con clear():")
print(Municipios)
