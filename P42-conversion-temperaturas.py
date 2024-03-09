# Se desea calcular la temperatura convertida de grados centígrados a grados farenheit de un rango 
# de valores introducidos por el usuario, es decir el usuario introduce la temperatura inicial y la 
# temperatura final en grados centígrados y el programa realiza la conversión a farenheit incrementando 
# el valor inicial en 1, hasta llegar al valor final. El proceso debe poder repetirse hasta que el 
# usuario lo decida.

import os; os.system("cls")

while True:
        temp_inicial = float(input("Introduce la temperatura inicial en grados Celsius: "))
        temp_final = float(input("Introduce la temperatura final en grados Celsius: "))
        incremento = 1

        if temp_inicial > temp_final:
            print("La temperatura inicial no puede ser mayor que la temperatura final.")
            continue

        print("\nTemperaturas convertidas:")
        celsius = temp_inicial
        while celsius <= temp_final:
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C = {fahrenheit}°F")
            celsius += incremento

        continuar = input("\n¿Deseas realizar otra conversión? (s/n): ")
        if continuar.lower() != 's':
            break