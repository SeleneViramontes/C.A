
#Esta funcion calcula el mayor de una lista de numeros

def mayor(lista):
    m=lista[0]
    for n in range(len(lista)):
        if lista [n] > m:
            m=lista[n]
    return m

#Esta funcion calcula el menor de una lista de numeros

def menor(lista):
    m=lista[0]
    for n in range(len(lista)):
        if lista [n] < m:
            m=lista[n]
    return m

#Esta funcion calcula el promedio de una lista de numeros

def promedio(lista):
    s=0
    for n in lista:
        s+=n
    return s/len(lista)
