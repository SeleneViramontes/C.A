# Calcular el volumen de un cilindro dado su radio y altura

import os; os.system("cls")
import math

def calcular_volumen(radio, altura):
    # Calcular la temperatura utilizando la fórmula dada
    volumen = math.pi * (radio ** 2) * altura
    return volumen

# Pedir al usuario que ingrese el radio y la altura del cilindro
radio= float(input("Ingrese el valor del radio del cilindro: "))
altura= float(input("Ingrese el valor de la altura del cilindro: "))

# Calcular el radio y la altura del cilindro
volumen = calcular_volumen(radio, altura)

# Mostrar el resultado
print(f"El volumen del cilindro es es {volumen:.3f}")