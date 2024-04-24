
def saluda(apaterno, amaterno, nombre, edad): 
    print(f"Hola {apaterno}, {amaterno}, {nombre} tu edad es {edad}")

saluda("Castaneda", "Ramirez", "Carlos", 20)

saluda(edad=20, nombre="Carlos", amaterno="Ramirez",apaterno="Castaneda")