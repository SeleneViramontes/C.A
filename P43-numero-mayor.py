# Calcular el número mayor de una serie de números introducidos por el teclado, el proceso se 
# detiene al introducir 0. El proceso debe poder repetirse hasta que el usuario lo decida.

import os; os.system("cls")

while True:
    primer_num=True
    mayor=0
    while True:
            num = float(input("Introduce un número (introduce 0 para detener): "))
            if num==0:
                break
            if primer_num or num>mayor:
                mayor=num
                primer_num=False
    if primer_num:
        print("No se introdujeron números")
    else:
        print("El número mayor es:", mayor)
    
    continuar = input("¿Deseas repetir el proceso? (s/n): ")
    if continuar.lower() != 's':
        break




