# Calcular la hipotenusa de un triangulo rectangulo
import os; os.system("cls")
import math

def calcular_hipotenusa(long_lado1, long_lado2):
    # Calcular la hipotenusa utilizando la fórmula dada
    hipotenusa = math.sqrt(long_lado1 ** 2 + long_lado2 ** 2)
    return hipotenusa

# Pedir al usuario que ingrese las longitudes de los lados
long_lado1 = float(input("Ingrese la longitud del primer lado: "))
long_lado2 = float(input("Ingrese la longitud del segundo lado: "))

# Calcular la hipotenusa
hipotenusa = calcular_hipotenusa(long_lado1, long_lado2)

# Mostrar el resultado
print("La hipotenusa del triángulo rectángulo es:", hipotenusa)