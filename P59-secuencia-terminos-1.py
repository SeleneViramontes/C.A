# Se desea imprimir la secuencia de términos armónicos el numero de renglones que el usuario desee 
# y su suma:

import os; os.system("cls")

renglones = int(input("Ingrese el número de terminos: "))
suma = 1 # Comenzamos con el primer término de la secuencia, que es 1.
secuencia = "1"

for i in range(2, renglones+1):
    termino = 1
    for j in range(1, i + 1):
        termino = termino/j
    suma += termino
    secuencia += f" + 1/{i}!"

print(f"Salida: {secuencia}, suma: {suma:.15f}")