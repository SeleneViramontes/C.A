import os; os.system("cls")

def arreglo():
    arreglo = [int(x) for x in input("Ingrese una lista de números enteros separados por espacios: ").split()]
    return arreglo

def fac(n):
    f=1
    for n in range(1, n+1):
        f=f*n
    return f

def factoriales_lista(lista):
    factoriales = []
    for numero in lista:
        factorial = fac(numero)
        factoriales.append(factorial)
    return factoriales

numeros = arreglo()
print("Lista original:", numeros)
factoriales = factoriales_lista(numeros)
print("Factoriales de los números capturados:", factoriales)