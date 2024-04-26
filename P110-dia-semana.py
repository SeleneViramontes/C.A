# Diseña un programa con una función que pida un número entero entre 1 y 7 y devuelva el día de la semana con letra.

import os;

def dia_semana(n):
    if n==1:
        dia="Lunes"
    elif n==2:
        dia="Martes"
    elif n==3:
        dia="Miercoles"
    elif n==4:
        dia="Jueves"
    elif n==5:
        dia="Viernes"
    elif n==6:
        dia="Sabado"
    elif n==7:
        dia="Domingo"
    else:
        dia=8
    return dia

os.system("cls")

n=int(input("Dame el dia de la semana (1-7) ? "))
dia = dia_semana(n)
if dia==8:
    print("Numero de dia erroneo")
else:
    print(f"El dia de la semana que corresponde al numero {n} es {dia}")