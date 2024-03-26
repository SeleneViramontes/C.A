# Llenar una lista con los primeros n números impares

import os; os.system('cls')

n = int(input("Ingrese la cantidad de números impares: "))
numeros_impares = [2*i + 1 for i in range(n)]
print("Lista de números impares:", numeros_impares)

# Calcular e imprimir la suma y promedio de los números
suma_total = sum(numeros_impares)
promedio = suma_total / n
print("Suma de los números impares:", suma_total)
print("Promedio de los números impares:", promedio)

# Mostrar los números que son divisibles entre 3 y sumarlos
divisibles_por_3 = [num for num in numeros_impares if num % 3 == 0]
suma_divisibles_por_3 = sum(divisibles_por_3)
print("Números divisibles por 3:", divisibles_por_3)
print("Suma de los números divisibles por 3:", suma_divisibles_por_3)

# Buscar un elemento en la lista original y determinar si está presente y en qué posición
elemento_buscar = int(input("Ingrese un número para buscar en la lista original: "))
if elemento_buscar in numeros_impares:
    posicion = numeros_impares.index(elemento_buscar)
    print(f"El número {elemento_buscar} está en la posición {posicion} de la lista original.")
else:
    print(f"El número {elemento_buscar} no está en la lista original.")