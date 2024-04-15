# Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones 
# de cada carácter en la cadena.

import os; os.system("cls")

# Pedir al usuario que ingrese una cadena
cadena = input("Ingrese una cadena: ")

# Crear un diccionario vacío para almacenar las frecuencias de los caracteres
frec_caracteres = {}

# Iterar sobre cada carácter en la cadena
for caracter in cadena:
    # Verificar si el carácter está en el diccionario
    if caracter in frec_caracteres:
        # Si yaexiste, incrementar su frecuencia en 1
        frec_caracteres[caracter] += 1
    else:
        # Si no existe, agregarlo al diccionario con frecuencia 1
        frec_caracteres[caracter] = 1

# Mostrar el diccionario con la cantidad de apariciones de cada carácter
print("Cantidad de apariciones de cada carácter:")
print(frec_caracteres)