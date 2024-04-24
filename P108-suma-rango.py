import os;

def suma_rango(ini, fin) :
    s=0
    for i in range(ini, fin+1):
        s=s+i
    return s

os.system("cls")
while True:
    i = int(input("Dame inicio ? "))
    f = int(input("Dame fin    ? "))
    if i<f:
        break

print(f"La suma del rango de {i}..{f} = {suma_rango(i,f)}")
