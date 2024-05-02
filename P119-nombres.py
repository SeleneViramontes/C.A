import os

def procesa(n1, n2):

    todos= []
    cuenta = []
    todos.extend(n1)
    todos.extend(n2)
    todos.sort()
    for i in range(len(todos)): 
        todos[i]= todos[i].upper()
        cuenta.append(len(todos[i]))
    return todos, cuenta

def entra():
    noms=[]
    while True:
        n=input ("Nombre ? ")
        if n=="" : break
        noms.append(n)
    return noms

os.system("cls")
noms1=["Juan", "Pedro", "Luis", "Jose", "Maria"]
#noms2 = ["Lucia", "Angelica", "Miguel", "Sandra"]
noms2=entra()

nombres, cuenta=procesa(noms1, noms2)

print(f"Nombres 1: {noms1}, {len(noms1)}") 
print (f"Nombres 2: {noms2}, {len(noms2)}") 
print(f"Nombres: {nombres}, {len(nombres)}") 
print(f"Cuenta : {cuenta}, {len(cuenta)}")