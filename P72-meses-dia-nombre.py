# Nombres de meses y su dia 

import os;os.system("cls")

# Definir listas con nombres de meses y días correspondientes
meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Leer el número de mes del usuario
num_mes = int(input("Ingresa el número de mes (1-12): "))

# Validar que el número de mes esté dentro del rango
if num_mes < 1 or num_mes > 12:
    print("Número de mes inválido.")
else:
    # Obtener el nombre del mes y la cantidad de días correspondientes
    mes = meses[num_mes - 1]
    dia = dias[num_mes - 1]

    # Imprimir el resultado
    print("Mes:", mes.capitalize())  # Usar capitalize() para capitalizar la primera letra del mes
    print("Días:", dia)