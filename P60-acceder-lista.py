#Acceder a los elementos de una lista

import os; os.system("cls")


nums=[10,20,30,40.5,60,70.5,10,20,99]

print("Acceder a los elementos de una lista \n")
print(f"La lista tiene {len(nums)} elementos")
print(f"La lista completa: {nums}")
print(f"Primero: {nums[0]}, Ultimo: {nums [8]} ")
print(f"Primero: {nums[-9]}, Ultimo: {nums [-1]} ")
print(f"Los primero tres: {nums[:3]}")
print(f"Los ultimos tres: {nums [6:]}")