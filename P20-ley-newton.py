#Calcula los valores de la segunda ley de newton (f = m*a)

import os; os.system("cls")

print("Calculando los valores de la segunda ley de newton \n")
print("[f]=m*a")
print("[m]=f/a")
print("[a]=f/m")
op= input("Elige una opcion ?").lower()

if op=="f":
    print("\nCalculando la fuerza..")
    m = float(input("Dame la masa ? "))
    a = float(input("Dame la aceleracion ?")) 
    f=m*a
    print("La fuerza es",f)
elif op=="m":
    print("\nCalculando la masa..")
    f = float(input("Dame la fuerza ? "))
    a = float(input("Dame la aceleracion ?")) 
    m = f/a
    print("La masa es",m)
elif op=="a":
    print("\nCalculando la aceleracion..")
    f = float(input("Dame la fuerza ? "))
    m = float(input("Dame la masa ?")) 
    a = f/m
    print("La aceleracion es",a)
else:
    print("\nOpcion incorrecta")

print("\nProceso terminado\n")