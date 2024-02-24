# Dada una temperatura en grados celcius, obtener su equivalente en grados farenheit

import os; os.system("cls")

def calcular_temperatura(celcius):
    # Calcular la temperatura utilizando la fórmula dada
    farenheit = (celcius * 9/5) + 32
    return farenheit

# Pedir al usuario que ingrese la temperatura en grados celcius
celcius= float(input("Ingrese el valor de la temperatura en grados celcius: "))

# Calcular la temperatura en grados farenheit
farenheit = calcular_temperatura(celcius)

# Mostrar el resultado
print("La temperatura en grados farenheit es:", farenheit)