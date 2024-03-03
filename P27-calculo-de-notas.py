# Se desea calcular el promedio de 5 calificaciones introducidas por el usuario, luego evaluar 
# el resultado e imprimir un mensaje de acuerdo al promedio obtenido

import os; os.system("cls")

print("Calculando el promedio de 5 calificaciones\n")
print("Dame 5 calificaciones separadas por espacio (pueden tener decimales) :")

c1, c2, c3, c4, c5=input().split()
c1, c2, c3, c4, c5= float(c1), float(c2), float(c3), float(c4), float(c5)

promedio=(c1+c2+c3+c4+c5)/5

if promedio>0 and promedio< 6:
    print(f"\nEl promedio de las calificaciones es: {promedio:.2f}. Quedas reprobado")
if promedio>6 and promedio<7:  
    print(f"\nEl promedio de las calificaciones es: {promedio:.2f}. Pasas de panzazo")
if promedio>7 and promedio<8:
    print(f"\nEl promedio de las calificaciones es: {promedio:.2f}. Muy bien, pues mejorar")
if promedio>8 and promedio<9:
    print(f"\nEl promedio de las calificaciones es: {promedio:.2f}. Excelente sigue así")
if promedio>9 and promedio<=10:
    print(f"\nEl promedio de las calificaciones es: {promedio:.2f}. Perfecto tu esfuerzo valió la pena")