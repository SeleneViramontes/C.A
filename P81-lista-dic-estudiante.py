# 

import os; os.system("cls")

grupo = [
    {"Nombre":"Carlos", "Edad":45, "Carrera": "Sistemas", "Promedio":9}, 
    {"Nombre":"Rocio", "Edad":35, "Carrera":"Psicologia", "Promedio": 10}
]
print("El grupo original", grupo)
while True:
    datos={}
    print("Datos de estudiante:")
    nombre=input("Nombre ? ")
    if nombre!="":
        datos["Nombre"]=nombre
        datos["Edad"]=int(input("Edad ? "))
        datos["Carrera"]=input("Carrera ? ")
        datos["Promedio"]=float(input("Promedio ? "))
        grupo.append(datos)
    else:
        break

print(f"Grupo completo {grupo} - {len(grupo)}")

print("Datos del grupo en forma de registros:\n")
s=0
for est in grupo:
    s=s+est["Promedio"]
    for k,v in est.items():
        print(f"{k:<10} - {v}")
    print()

print(f"Datos del grupo de estudiantes en forma de tabla:\n")
for k in grupo[0].keys():
    print(f"{k:<15}",end="")
print("\r")
print("-"*60)
for alumno in grupo:
    for v in alumno.values():
        print(f"{v:<15}",end="")
    print("\r")
print("-"*60)

print(f"\nLa suma de promedios es: {s}")
print(f"\nEl promedio de la clase es: {s/len(grupo)}")