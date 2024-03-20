#Agregar elementos a una Lista de numeros

import os; os.system("cls")

nums= [80.3, 12.5, 60.2, 30.4]
print("Agregar elementos a una lista de numeros existente \n")
print(f"Todos {nums}, {len(nums)}")

print("Agregar elmentos al final :")
nums.append(90)
nums.append(100)
print(f"Todos {nums}, {len(nums)}")

print("Insertar elemento en una posicion determinada:")
nums.insert(4,80)
print(f"Todos {nums}, {len(nums)}")

print("Agregar varios elementos al final")
nums.extend([110,120,130])
print(f"Todos {nums}, {len(nums)}")