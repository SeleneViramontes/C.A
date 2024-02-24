# Dados dos ángulos de un triángulo, calcular el 3er ángulo

import os; os.system("cls")

def calcular_3erangulo(angulo1, angulo2):
    # Calcular el 3er anguolo utilizando la fórmula dada
    angulo3 = 180-(angulo1 + angulo2)
    return angulo3

# Pedir al usuario que ingrese los dos angulos
angulo1 = float(input("Ingrese el valor del angulo1: "))
angulo2 = float(input("Ingrese el valor del angulo2: "))

# Calcular el angulo 3
angulo3 = calcular_3erangulo(angulo1, angulo2)

# Mostrar el resultado
print("El angulo3 del triángulo rectángulo es:", angulo3)