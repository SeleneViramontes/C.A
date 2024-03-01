#Cuenta los numeros introducidos por el usuario, saca la suma, positivos, negativos y ceros

import os; os.system("cls")

cuenta=suma= 0
cp=cn=cz=0

print("Conteo-de numeros :\n")

while(True):
    num = int(input(" Numero ? "))
    if num!=999:
        cuenta=cuenta+1
        suma=suma+num
        if num > 0 : 
            cp+=1
        elif num < 0:  
            cn += 1
        else: cz+=1
    else:
        break

print(f"Se introdujeron {cuenta} numeros")

print(f"La suma es {suma}")

print(f"Positivos: {cp}, Negativos: {cn}, Ceros: {cz}")