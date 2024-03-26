# Generar 2 listas de 10 números aleatorios

import random
import os;os.system("cls")

n=10

l1=[]
l2=[]
l3=[]

print("\nGenerando Listas con numeros aleatorios")
for i in range(n):
    l1.append(random.randint(1,10))
    l2.append(random.randint(1,10))

print(f"Lista 1: {l1}\nLista 2: {l2}")

# Sumar ambas listas si los elementos correspondientes son impares
for num1, num2 in zip(l1, l2):
    if num1 % 2 != 0 and num2 % 2 != 0:  # Verificar si ambos números son impares
        l3.append(num1 + num2)

print(f"\nLista 1: {l1}\nLista 2: {l2}\n\nLista 3 (suma_elementos impares): {l3} ")
