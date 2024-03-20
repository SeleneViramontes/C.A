# Remover elmentos de una lista de numeros 

import os; os.system("cls")

nums= [ 1, 3, 5, 7, 9, 11, 99, 15, 88 ,19,100]

print("Remover elementos de una lista de numeros \n")
print(f"Todos: {nums}, {len(nums)} ")

print("Remover la primer ocurrencia de un elemento en la lista")
nums.remove(99)
print(f"Todos: {nums}, {len(nums)} ")

print("Remover un elmento con pop en una posicion determinada y regresarlo")
numv= nums.pop(8)
print(f"Todos {nums}, {len(nums)} , eliminado: {numv}")

print("Remover el ultimo elemento de la lista usando pop")
num=nums.pop()
print(f"Todos {nums}, {len(nums)} , eliminado: {num}")

print("Borrar todos los elementos de la lista ")
nums.clear()
print(f"Todos: {nums}, {len(nums)} ")