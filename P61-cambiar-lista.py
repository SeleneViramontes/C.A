#Cambiar o modificar los elemntos en una lista existente

import os; os.system("cls")

nums=[10,9,8,5,6.5,9.8,7,5,6.2,9.5]
print("Modificar los elementos de una lista \n")
print(f"Todos: {nums}, {len(nums)}")
print("Modificar los elementos 0 y 1")
nums[0] = 7
nums [1] = 7
print (f"Todos: {nums}, {len(nums)}")
print("Modificar los elementos del 2 al 5")
nums [2:5]=[9,9,9]
print(f"Todos: {nums}, {len(nums)}")