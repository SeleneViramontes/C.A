#Captura una lista de edades y nombres, y suestra los mayores de edad, y el de mayor edad

import os; os.system('cls')

nombres = []
edades= []

print("Capturando nombres y edades\n")

print("Introduce los nombres y edades de n estudiantes: * para terminar:")

while True:
    nombre= input("Nombre : ")
    if nombre=="*":
        break
    else:
        nombres.append(nombre)
        edad=int(input("Edad :"))
        edades.append(edad)

print(f"Nombres: {nombres} y edades {edades}")

print("\nAlumnos mayores de edad:")
for i in range(len(nombres)):
    if edades[i]>=18:
        print(f"Nombre: {nombres[i]}, edad {edades[i]}")

may=max(edades)
pos=edades.index(may)

print(f"El alumno de mayor edad es {nombres[pos]} y tiene {edades[pos]} años de edad")