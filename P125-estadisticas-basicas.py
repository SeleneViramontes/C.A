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
    med = media(lista)
    var = sum((x - med) ** 2 for x in lista) / len(lista)
    return var

def desviacion_estandar(lista):
    var = varianza(lista)
    des_estandar = var ** 0.5
    return des_estandar


numeros = arreglos()
print("Lista original:", numeros)

may=mayor(numeros)
men=menor(numeros)
med = media(numeros)
var = varianza(numeros)
des_estandar = desviacion_estandar(numeros)

print("El mayor es", may)
#----------------------------------------------
print("El menor es", men)
#-----------------------------------------------
print(f'Media: {med:.3f}')
#-----------------------------------------------
print(f'Varianza: {var:.3f}')
#----------------------------------------------
print(f'Desviación estándar : {des_estandar:.3f}')