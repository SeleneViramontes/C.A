# Crear tres conjuntos, uno por cada lista de números y mostrarlos ( A, B, C)

import os; os.system("cls")

# Definición de los conjuntos
print("\n")
A = {50, 60, 70, 80, 90, 100, 200}
B = {60, 90, 100, 300, 400, 500}
C = {10, 20, 60, 90, 70, 100, 600, 700}
# Mostrar los conjuntos
print("Conjunto A:", A)
print("Conjunto B:", B)
print("Conjunto C:", C)

# Operaciones con conjuntos y mostrar los resultados de las operaciones
print("\nUnion")
print(f"union de A con B: {A | B}")
print(f"union de B con C: {B | C}")

print("\nDiferiencia")
print(f"Diferiencia de A con B: {A - C}\n")

print("\nDiferiencia simetrica")
print(f"Diferiencia simetrica de A con cB: {B ^ C}\n")

print("\nInterseccion")
print(f"Interseccion de A con B: {B & C}")

# Mostrar los resultados adicionales
print("\nProbar por subconjuntos")
print(f"A es subconjunto de B: {A.issubset(B)}")
print(f"C es subconjunto de A: {C.issubset(A)}")

print("\nVerificar la existencia de un elemento en un conjunto:")
print(f"100 esta en A: {100 in A}")
print(f"6O esta en A, B, C: {60 in A and 60 in B and 60 in C}")
print(f"900 no esta en c: {900 not in C}")