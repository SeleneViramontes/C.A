# Realizar un programa que pida un número entre 1 y 10 y muestre su equivalente en número romano 
#( I, II, III, IV, V, VI, VII, VIII, IX, X). Si el número no esta en el rango solicitado 
#que mande un mensaje de error.

import os; os.system("cls")

#print(f"Ingresa un numero en el rango de 1-10")
dia= int (input("Ingresa un numero en el rango de 1-10 ?: "))


if dia==1:
    n_romano = "I"
    print(f"\nEl número romano equivalente a {dia} es: {n_romano}")
elif dia== 2:
    n_romano = "II"
    print(f"\nEl número romano equivalente a {dia} es: {n_romano}")
elif dia== 3:
    n_romano = "III"
    print(f"\nEl número romano equivalente a {dia} es: {n_romano}")
elif dia== 4:
    n_romano = "IV"
    print(f"\nEl número romano equivalente a {dia} es: {n_romano}")
elif dia== 5:
    n_romano = "V"
    print(f"\nEl número romano equivalente a {dia} es: {n_romano}")
elif dia== 6:
    n_romano = "VI"
    print(f"\nEl número romano equivalente a {dia} es: {n_romano}")
elif dia== 7:
    n_romano = "VII"
    print(f"\nEl número romano equivalente a {dia} es: {n_romano}")
elif dia== 8:
    n_romano = "VIII"
    print(f"\nEl número romano equivalente a {dia} es: {n_romano}")
elif dia== 9:
    n_romano = "IX"
    print(f"\nEl número romano equivalente a {dia} es: {n_romano}")
elif dia== 10:
    n_romano = "X"
    print(f"\nEl número romano equivalente a {dia} es: {n_romano}")
else:
    print(f"\nEl numero ingresado esta fura del rango, vuelve a intentarlo\n")
