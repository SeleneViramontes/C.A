# Dado el año de nacimiento, la suma de sus dígitos individuales es el número de la suerte. 
# Mostrar los dígitos individuales y el número de la suerte.

import os; os.system("cls")

def numero_suerte(año):
    # Convertir el año a una cadena para poder iterar sobre sus dígitos
    año_str = str(año)
    
    # Inicializar la suma de los dígitos a 0
    suma_digitos = 0
    
    # Iterar sobre cada dígito en el año
    for digito in año_str:
        # Convertir el dígito de vuelta a entero y sumarlo
        suma_digitos += int(digito)
    
    # Imprimir los dígitos individuales
    print("Dígitos individuales:", ' '.join(año_str)) # .join concatena los elementos de la cadena
    
    # Imprimir el número de la suerte
    print("Número de la suerte:", suma_digitos)

# Pedir al usuario que ingrese su año de nacimiento
año = int(input("Ingrese su año de nacimiento: "))

# Calcular y mostrar el número de la suerte
numero_suerte(año)