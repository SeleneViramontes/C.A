# Codigo de clase
import os
class Empleado:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad= edad

    def __str__(self): 
        return f"Nombre: {self.nombre} - Edad: {self.edad}\n"

# Programa principal
os.system("cls")
empleado01=Empleado("Jose Diaz", 35)
print("Nombre:", empleado01.nombre) 
print("Edad : ", empleado01.edad)
empleado01.edad = 40
print(empleado01)

empleado02=Empleado("Sandra Lopez", 22) 
print(empleado02)

empleado03=Empleado("Lucia Ramirez", 15) 
print(empleado03)

print(f"Promedio edad de los 3",(empleado01.edad+empleado02.edad+empleado03.edad)/3)