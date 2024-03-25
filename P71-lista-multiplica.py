# Multiplicando dos listas de 5 numeros

import os;os.system("cls")

lista1=[]
lista2=[]
lista3=[]

print(" Multiplicar 2 listas de 5 numeros \n")

print(f"\nDame los elementos de la lista I:")
for i in range(5):
    n=float(input(f"Lista1[{i}]= "))
    lista1.append(n)
print(f"\nLista 1: {lista1}")

print(f"\nDame los elementos de la lista 2:")
for i in range(5):
    n=int(input(f"Lista2[{i}]= "))
    lista2.append(n)
print(f"\nLista 2: {lista2}")


print("\nCalculando la multiplicacion de las listas")
for i in range(5):
    lista3.append(lista1[i] * lista2[i])
print(f"Lista 3: {lista3}")





