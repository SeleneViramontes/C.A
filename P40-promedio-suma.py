# Se desea calcular la suma y el promedio de una serie de números introducidos por el teclado hasta 
# introducir 0, además deberá contar cuantos números se introdujeron. El proceso debe poder repetirse 
# hasta que el usuario lo decida.

import os; os.system("cls")

while True:
        suma = 0
        contador = 0
        numero = None
        
        while numero != 0:
            numero = float(input("Ingrese un número (o ingrese 0 para terminar): "))
            if numero != 0:
                suma += numero
                contador += 1
        
        if contador == 0:
            print("No se ingresaron números.")
        else:
            promedio = suma / contador
            print("\nLa suma de los números es:", suma)
            print("El promedio de los números es:", promedio)
            print("Se ingresaron", contador, "números.")
        
        continuar = input("¿Desea realizar otro cálculo? (s/n): ")
        if continuar.lower() != 's':
            print("Saliendo del programa...")
            break