# Dado el nombre del estudiante, sexo (h/m), su edad y tres calificaciones, decidir si 
#el estudiante es aceptado. La Universidad Kitty Kat SA es solo para mujeres mayores de 21 años 
#con un promedio de entre 8 y 9.5.

import os; os.system("cls")

print("La Universidad Kitty Kat SA de CV")
print("Validacion de inscripcion \n")

nombre=input("Ingresa el nombre ? ")
sexo=input("Ingresa el sexo (H/M) ? ").upper()
edad=int(input("Ingresa la edad ? "))


print("Ingresa 3 calificaciones separados por <Enter>: ")

c1,c2, c3 = float(input()), float(input()), float(input())
prom=(c1+c2+c3)/3

if prom>=8 and sexo== "M" and edad>=21:
    print(f"{nombre}, has sido aceptad@, tu edad de {edad} años y tus calificaciones {c1}, {c2}, {c3} lo permiten")
elif sexo=="H":
    print("Lo sentimos, solo aceptamos mujeres")
elif sexo=="M" and edad<21:
    print("Eres mujer, pero no tienes la edad, solo mayores a 21")
elif sexo=="M" and edad>=21 and prom<8:
    print("Eres mujer, tienes la edad, pero tu promedio no alcanza solo promedios de 8 a 9.5")
else:
    print("\nLos datos ingresado son incirrectos")

print("\nProceso terminado") 