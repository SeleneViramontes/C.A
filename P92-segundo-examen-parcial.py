# Se desea procesar los empleados de la empresa Muebles Dico, para lo cual deberá solicitar al usuario los datos. Los datos se deben almacenar en una lista conformada 
# por diccionarios, donde cada elemento de la lista será los datos de un empleado.

import os; os.system("cls")

# Capturar los datos de un empleado
empleados = []
cantidad_empleados = int(input("Ingrese la cantidad de empleados que desea procesar: "))

for _ in range(cantidad_empleados):
    nombre = input("\nIngrese el nombre del empleado: ")
    edad = int(input("Ingrese la edad del empleado: "))
    sexo = input("Ingrese el sexo del empleado (h/m): ").lower()
    sueldo = float(input("Ingrese el sueldo del empleado: "))

    empleado = {
        'nombre': nombre,
        'edad': edad,
        'sexo': sexo,
        'sueldo': sueldo
    }
    empleados.append(empleado)

# Imprimir los datos como se guardan en la lista de diccionarios
print("\nDatos de los empleados:")
print(empleados)

# Imprimir los datos en formato tabular
print("\nTabla de datos:")
print("\n{:<9} {:<8} {:<5} {:<10}".format('NOMBRE', 'EDAD', 'SEXO', 'SUELDO'))
print("-"*35)
for empleado in empleados:
    print("{:<9} {:<8} {:<5} {:<10}".format(empleado['nombre'], empleado['edad'], empleado['sexo'], empleado['sueldo']))

# Imprimir un resumen de los datos de los empleados
total_empleados = len(empleados)
total_hombres = sum(1 for empleado in empleados if empleado['sexo'] == 'h')
total_mujeres = sum(1 for empleado in empleados if empleado['sexo'] == 'm')
suma_edad = sum(empleado['edad'] for empleado in empleados)
promedio_edad = suma_edad / total_empleados
suma_sueldo = sum(empleado['sueldo'] for empleado in empleados)
promedio_sueldo = suma_sueldo / total_empleados

print("\nResumen de los empleados:")
print("Total de empleados:", total_empleados)
print("Total de hombres:", total_hombres)
print("Total de mujeres:", total_mujeres)
print("Suma de edades:", suma_edad)
print("Promedio de edad:", promedio_edad)
print("Suma de sueldos:", suma_sueldo)
print("Promedio de sueldo:", promedio_sueldo)