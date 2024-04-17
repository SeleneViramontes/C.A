# Crea dos conjuntos uno para cada lista de nombres y muéstralos ( A, B )

import os; os.system("cls")

# Definición de los conjuntos
print("\n")
A = {"Juan", "Maria", "Pedro", "Jose", "Rocio"}
B = {"Pedro", "Juan", "Pablo", "Mateo", "Esther"}
# Mostrar los conjuntos
print("Conjunto A:", A)
print("Conjunto B:", B)

# Operaciones con conjuntos y mostrar los resultados de las operaciones
print("\nUnion")
print(f"union de A con B: {A | B}")

print("\nInterseccion")
print(f"Interseccion de A con B: {A & B}")

print("\nDiferiencia")
print(f"Diferiencia de A con B: {A - B}\n")

print("\nDiferiencia simetrica")
print(f"Diferiencia simetrica de A con cB: {A ^ B}\n")

# Mostrar los resultados adicionales
print("\nProbar por subconjuntos")
print(f"El conjunto de nombres Pablo, Mateo, es subconjunto de B: {({"Pablo", "Mateo"}).issubset(B)}")

print("\nProbar por superconjunto")
print(f"El conjunto A es superconjunto del conjunto de nombres Reynaldo, Angelica: {A.issuperset({"Reynaldo", "Angelica"})}")

print("\nVerificar la existencia de un elemento en un conjunto:")
print(f"Pedro está en A: {"Pedro" in A}")
print(f"Lilia no está en B: {"Lilia" not in B}")
