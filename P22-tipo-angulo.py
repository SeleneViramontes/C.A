#Muestra el tipo de angulο

# <98 agudo, =90 recto, >90 y <180 obtuso, =180 llano, >180 y <360 concavo, =360 completo

import os; os.system("cls")

print("Mostrado el tipo de angulo en base a los grados\n")
angulo = int(input("Dame el angulo ?"))

if angulo>=0 and angulo<=360:

    print(f"El angulo tiene {angulo} grados por lo tanto es un angulo ", end="")
    if angulo<90:
        print("agudo")
    elif angulo==90:
        print("recto")
    elif angulo>90 and angulo<180:
        print("obtuso")
    elif angulo==180:
        print("llano")
    elif angulo>180 and angulo<360:
        print("concavo")
    else:
        print("completo")
else:
    print("\nAngulo fuera de rango")

print("\nProceso teminado")