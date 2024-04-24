import os;
def tabla(t,n):
    print(f"Imprimiendo la tabia del {t} hasta el {n}")
    for i in range(1, n+1):
        print(f"{t} x {i} = {t*i}")

#tabla(6, 10)
#tabla(3,4)

while True:
    os.system("cls")
    t=int(input("Que tabla quieres ?"))
    n=int(input("Hasta donde la quieres ?"))
    tabla(t,n)
    res = input("Deseas otra tabla (S/N)?").upper()

    if res=="N":
        break