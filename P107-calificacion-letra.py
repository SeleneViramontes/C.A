import os;

def caletra(prom):

    if prom>=90 and prom<100:
        return "A", "Excelente"
    elif prom>=80 and prom<90:
        return "B", "Bien"
    elif prom>=70 and prom<80:
        return "C", "Suficiente"
    elif prom>=60 and prom<70:
        return "D", "Deficiente"
    elif prom>=0 and prom<60:
        return "F", "Reprobado"

os.system("cls")
prom = float(input("Dame tu promedio (1..100) ? "))
letra, mensaje=caletra(prom)
print(f"Tu promedio de {prom} se le asigna la {letra} y es {mensaje}")
