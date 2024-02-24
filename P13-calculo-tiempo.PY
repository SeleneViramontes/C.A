# Dada una cantidad en horas, calcular su equivalente en días, minutos y segundos

import os; os.system("cls")

def calcular_tiempo(tiempo_en_horas):
    # Calcular los días
    dias = (tiempo_en_horas)/(24)
    # Calcular los minutos
    minutos = tiempo_en_horas*60
    # Calcular los segundos
    segundos = tiempo_en_horas*60*60

    return dias, minutos, segundos

horas = float(input("Ingrese la cantidad de horas: "))
dias, minutos, segundos = calcular_tiempo(horas)
print(f"{horas} horas equivalen a:")
print(f"{dias:.2f} días, {minutos:.2f} minutos y {segundos:.2f} segundos.")
        