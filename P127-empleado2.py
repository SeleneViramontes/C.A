import os

class Empleado:
    def __init__(self,nombre,edad,sexo,casado,sueldo):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
        self.casado=casado
        self.sueldo=sueldo
    def __str__(self):
        return f"nombre: {self.nombre}, edad: {self.edad}, sexo: {"Mujer" if self.sexo=="M" else "Hombre"}, casado: {"Casado(a)" if self.casado else "Soltero(a)"}, sueldo: {self.sueldo}"

os.system("cls")
empleado01=Empleado("Jose Diaz", 35, "H", False, 1200)
print("Nombre :", empleado01.nombre)
print("Edad :", empleado01.edad)
print("Sexo :", empleado01.sexo) 
print("Casado :", empleado01.casado)
print("Sueldo :", empleado01.sueldo)
print(empleado01)

empleado02=Empleado("Maria Lopez", 40, "M", True, 1400)
print(empleado02)

empleado03=Empleado("Rocio Soto", 45, "M", False, 2000) 
print(empleado03)

total=empleado01.sueldo + empleado02.sueldo + empleado03.sueldo
print("\nTotal del Sueldo: ", total)