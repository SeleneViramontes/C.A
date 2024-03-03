# Dado un numero entero entre 1 y 7, se desea mostrar con letra el día de la semana correspondiente, 
# 1 es domingo, 2 es lunes y así hasta 7 es viernes. Si el número no está en el rango especificado, 
#mostrar un mensaje de error.

import os; os.system("cls")

numero= int (input("Ingresa un numero en el rango de 1-10 ?: "))

if numero==1:
   print(f"\nDía Domingo")
elif numero== 2:
   print(f"\nDía Lunes")
elif numero== 3:
   print(f"\nDía Martes")
elif numero== 4:
   print(f"\nDía Miércoles")
elif numero== 5:
   print(f"\nDía Jueves")
elif numero== 6 :
   print(f"\nDía Viernes")
elif numero== 7 :
   print(f"\nDía Sábado")
else:
    print(f"\nEl numero ingresado esta fura del rango, vuelve a intentarlo\n")
