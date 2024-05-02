import os; os.system("cls")

def suma_digitos(numero):
    suma = 0
    while numero > 0:
        suma += numero % 10
        numero //= 10
    return suma

def sumalistas(lista):
    sumas = []
    for numero in lista:
        suma = suma_digitos(numero)
        sumas.append(suma)
    return sumas

numeros = [int(x) for x in input("Ingrese una lista de números enteros separados por espacios: ").split()]
print("Lista original:", numeros)
sumas_digitos = sumalistas(numeros)
print("Sumas de los dígitos de los números capturados:", sumas_digitos)