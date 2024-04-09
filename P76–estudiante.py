# Procesa los datos de un estudiante en un diccionario

import os; os.system('cls')

estudiante= {"nombre" : "Juan Perez", "edad" : 45, "email" : "jperez@msn.com", "carrera" : "sistemas"}
estudiante2= {"nombre" : "Maria Lopez", "edad" : 22, "email" : "maria@msn.com", "carrera" : "leyes"}

print(f"\nEl estudiante: \n {estudiante}, {len(estudiante)}")

print("\nLas llaves:")
for k in estudiante.keys():
    print(k)

print("\nLos valores:")
for v in estudiante.values():
    print(v)

estudiante.update({'calificacion':9.5})
estudiante['email'] = "jperez@gmail.com"

print('\nEl diccionario modificado, llave y valor:')
for k, v in estudiante.items():
    print(f"{k:<12} - {v:>15}")
