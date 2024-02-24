# Paga de un trabajador

import os; os.system("cls")

print("Calculando la paga de horas extra de un trabajador \n")

nombre= input("Nombre del trabajador: ")
horas= int(input("Horas trabajadas: "))
paga= float(input("Paga por hora: "))

extra=pagaextra=total=0 #inicializamos las variables de resultados

if horas <= 40:
    total=horas*paga
else:
    extra=horas-40
    pagaextra=extra*paga*2
    total=(40*paga)+pagaextra

salida = (f"\nEl trabajador {nombre }\n"
f"Trabajo {horas} horas \n"
f"Con paga de {paga} \n"
f"Horas extra {extra}, paga extra {pagaextra} \n"
f"Total de pago {total} \n"
)

print(salida)