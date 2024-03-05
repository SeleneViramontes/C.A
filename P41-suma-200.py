# Se desea calcular la suma de números introducidos por el usuario hasta que la suma sea >= 200, 
# luego mostrar cuantos números fueron introducidos y la suma de estos. El proceso debe poder repetirse 
# hasta que el usuario lo decida.

import os; os.system("cls")

while True:
        suma = 0
        contador = 0
        
        print("Ingresa los numeros que desees separados por <Enter>\n")
        while suma < 200:
            numero = float(input("Ingrese un número : "))
            suma += numero
            contador += 1
        
        print("Se alcanzó una suma mayor o igual a 200.")
        print("Se introdujeron", contador, "números.")
        print("La suma de estos números es:", suma)
        
        continuar = input("¿Desea realizar otro cálculo? (s/n): ")
        if continuar.lower() != 's':
            print("Saliendo del programa...")
            break