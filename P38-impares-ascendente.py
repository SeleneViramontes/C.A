# Se desea imprimir los números impares de forma ascendente desde 1 hasta el número que el usuario 
# decida (n), además deberá imprimirse la suma de esos números impares. El proceso debe poder repetirse 
# hasta que el usuario lo decida.

import os; os.system("cls")

while True:
        numero = int(input("Ingrese un número entero positivo (o ingrese 0 para salir): "))
        if numero < 0:
            print("Por favor, ingrese un número entero positivo.")
        elif numero == 0:
            print("Saliendo del programa...")
            break
        else:
            suma_impares = 0
            print("\nLos numeros impare son")
            for i in range(1, numero + 1, 2): # Genera un par de numeros de 1 hasta numero con incrementos de 2
                print(i)
                suma_impares += i
            print("\nLa suma de los números impares hasta", numero, "es:", suma_impares)