

import os
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

def leer():
    nums=[] 
    while True: 
        d = int(input("Numero ? ")) 
        if d == -1: break 
        nums.append(d) 
    return nums

os.system("cls") 
#nums [9,8,7.5,6,30,9.5,7,10,6,7)

nums=leer()
may=mayor(nums)
men= menor(nums)

print(f"Los numeros son: {nums}, {len(nums)}")
print("El mayor es", may)
print("El menor es", men)