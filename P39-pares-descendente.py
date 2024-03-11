# Se desea imprimir los números pares decendentes desde 100 hasta el número que el usuario decida (n), 
# además deberá imprimirse la suma de esos números pares. El proceso debe poder repetirse hasta que 
# el usuario lo decida.

import os; os.system("cls")

while True:
        numero = int(input("Ingrese un número entero positivo (o ingrese 0 para salir): "))
        if numero < 0:
            print("Por favor, ingrese un número entero positivo.")
        elif numero == 0:
            print("Saliendo del programa...")
            break
        else:
            suma_pares = 0
            for i in range(100, numero - 1, -2):
                print(i)
                suma_pares += i
            print("La suma de los números pares desde 100 hasta", numero, "es:", suma_pares)