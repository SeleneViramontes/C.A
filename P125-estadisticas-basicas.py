import os; os.system("cls")

def arreglos():
    arreglo = [int(x) for x in input("Ingrese una lista de números enteros separados por espacios: ").split()]
    return arreglo

def mayor(lista): 
    m = lista[0] 
    for n in range(len(lista)): 
        if lista[n]>m:
            m=lista[n]
    return m

def menor(lista): 
    m = lista[0] 
    for n in range(len(lista)): 
        if lista[n]<m:
            m=lista[n]
    return m

def media(lista):
        suma = sum(lista)
        med = suma / len(lista)
        return med
    
def varianza(lista):
    if len(lista) == 0:
        return None
    med = media(lista)
    var = sum((x - med) ** 2 for x in lista) / len(lista)
    return var

def desviacion_estandar(lista):
    if len(lista) == 0:
        return None
    var = varianza(lista)
    des_estandar = var ** 0.5
    return des_estandar


numeros = arreglos()
print("Lista original:", numeros)

may=mayor(numeros)
men= menor(numeros)

print(f"Los numeros son: {numeros}, {len(numeros)}")
print("El mayor es", mayor)
print("El menor es", menor)
#-----------------------------------------------
med = media(numeros)
if med is not None:
    print("Media:", med)
#-----------------------------------------------
var = varianza(numeros)
if var is not None:
    print("Varianza:", var)
#----------------------------------------------
des_estandar = desviacion_estandar(numeros)
if des_estandar is not None:
    print("Desviación estándar:", des_estandar)