# Convertir una temperatura de celcius a farenheit y viceversa

import os; os.system("cls")

print("Conversion de temperaturas Farenheit <--> Celcius \n")
opcion = str.upper(input("[C]elcius \n[F]arenheit \nElije? "))

if opcion == "C" :
    print("\nConvirtiendo a Celcius...")
    temp=float(input("Grados Farenheit? "))
    res=(temp-32)*5/9
    print(f"{temp} grados farenheit, equivale a {res:.2f} grados celcius")
else :
    print("\nConvirtiendo a Farenheit...")
    temp=float(input("Grados Celcius? "))
    res=(temp*9/5)+32
    print(f"{temp} grados celcius, equivale a {res:.3f} grados farenheit")

print("Proceso terminado")

