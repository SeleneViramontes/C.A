# Operaciones entre conjuntos (matematicas)

import os; os.system("cls")

c1={1,2,3,4,5}
c2={5,6,7,8,9,10}
c3={9,10,11,12,13}
c4={3,4,5}

print("Union:")
print(f"union de c1 con c2: {c1.union(c2)}")
print(f"union de c1 con c3: {c1 | c3}\n")

print("Interseccion")
print(f"Interseccion de c1 con c2: {c1.intersection(c2)}")
print(f"Interseccion de c2 con c3: {c2 & c3}\n")

print("Diferiencia")
print(f"Diferiencia de c1 con c4: {c1.difference(c4)}")
print(f"Diferiencia de c2 con c3: {c2 - c3}\n")

print("Diferiencia simetrica")
print(f"Diferiencia simetrica de c1 con c2: {c1.symmetric_difference(c2)}")
print(f"Diferiencia simetrica de c2 con c3: {c2 ^ c3}\n")

print("Probar por subconjuntos")
print(f"c4 es subconjunto de c1: {c4.issubset(c1)}")
print(f"c3 es subconjunto de c2: {c3 <= c2}\n")

print("Probar por superconjunto")
print(f"c1 es superconjunto de c4 {c1.issuperset(c4)}")
print(f"c2 es superconjunto de c3: {c2 >= c3}\n")

print("Verificar la existencia de un elemento en un conjunto:")
print(f"2 esta en c1: {2 in c1}")
print(f"6 no esta en c1: {6 not in c1}")

