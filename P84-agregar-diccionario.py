# Crear un diccionario de llave de cadena, ventas, con los siguientes elementos

import os; os.system("cls")

ventas = {"Juan" : 1550, "Jose" : 2600, "Maria" : 2220}

# Mostrar el diccionario completo
print("Diccionario de países completo:")
print(ventas)

# Agregar los elementos adicionales al diccionario
ventas["Rocio"] = 2500
ventas["Mateo"] = 1567
ventas.update({"Andrea": 9567, "Miguel": 1234})

# Mostrar el diccionario completo después de agregar los elementos adicionales
print("\nDiccionario de países después de agregar elementos adicionales:")
print(ventas)
