# Procesar dos listas en un diccionario

import os; os.system('cls')

materias = ["Fisica", "Quimica", "Matematicas", "Geografia", "Estadistica"]
califs =[10,9,8,7.5,6]

print(f"Materias: {materias}, {len(materias)}")
print(f"Calificaciones: {califs}, {len(califs)}")
notas = dict(zip(materias, califs))
print(f"Las notas {notas}, {len(notas)}")
notas.update({"Ingles":10})
notas['Programacion'] = 7
print(f"Las notas {notas}, {len(notas)}")
notas.pop("Fisica")
notas.popitem()
print(f"Las notas {notas}, {len(notas)}")
notas ["Quimica"] = 10
notas.update({"Matematicas": 10, "Geografia":10})
print(f"Las notas {notas}, {len(notas)}")
print("\nLista de materias, suma y promedio:")


s=p=0
for m, c in notas.items():
    print(f"{m:<12} - {c:5>}")
    s=s+c
p=s/len(notas)

print(f"La Suma {s} el promedio {p}")

notas.clear()
print(f"Las notas {notas}, {len(notas)}")