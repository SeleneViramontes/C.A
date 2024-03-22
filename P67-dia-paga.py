# Dado un dia de la semana imprime la paga correspondiente

import os; os.system('cls')

dias= ["lunes","martes","miercoles","jueves","viernes","sabado", "domingo"]
paga= [100,200,300,400,500,600,700]

print("Dado un dia de la semana imprimir la paga correspondiente \n")

while True:
    dia= input("Ingrese un dia de la semana con letra : ")
    if dia in dias:
        break

print("El dia que elejiste trabajar es", dia)
pos=dias.index(dia)
print("La paga que te corresponde es", paga[pos])