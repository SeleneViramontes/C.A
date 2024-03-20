#Iterar sobre los elementos de una lista

import os; os.system('cls')

nums = [2, 4, 6, 8, 10, 12, 14, 16]

print("Iterar por los elementos de una lista ") 
print(f"Los numeros {nums}, {len(nums)} ")

print("Iterar por los elementos usando for:") 
for num in nums:
    print("# :", num, num*2)

print("Interar por indice")
for i in range(len(nums)):
    print(">", nums [i], nums [i]*3)

print("Iterar por indice y elevar al cuadrado")
for i in range(len(nums)):
    nums[i] = nums[i] ** 2

print(f"Los numeros {nums}, {len(nums)} ")
