# Procesando las notas entre o y 100

import os;os.system("cls")

notas = []
suma = 0
contador_notas = 0

# Leer notas hasta que se introduzca un 0
while True:
    nota = float(input("Introduce una nota (0 para terminar): "))
    
    # Validar que la nota esté entre 0 y 100
    if nota < 0 or nota > 100:
        print("Error: La nota debe estar entre 0 y 100.")
        continue
    
    # Terminar la entrada si se ingresa 0
    if nota == 0:
        break
    
    notas.append(nota)
    suma += nota
    contador_notas += 1

# Calcular promedio
promedio = suma / contador_notas if contador_notas > 0 else 0

# Encontrar la nota máxima y mínima
nota_maxima = max(notas) if notas else 0
nota_minima = min(notas) if notas else 0

# Encontrar notas menores al promedio
notas_menores_al_promedio = []
for nota in notas:
    if nota < promedio:
        notas_menores_al_promedio.append(nota)
cantidad_notas_menores = len(notas_menores_al_promedio) # cuantas notas son

# Imprimir resultados
print(f"\nCantidad de notas: {contador_notas}")
print(f"Notas: {notas}")
print(f"Suma: {suma}")
print(f"Promedio: {promedio}")
print(f"Notas menores al promedio: {notas_menores_al_promedio}, Cantidad: {cantidad_notas_menores}")
print(f"Nota máxima: {nota_maxima}")
print(f"Nota mínima: {nota_minima}")