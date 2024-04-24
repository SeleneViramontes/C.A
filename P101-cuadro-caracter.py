import os;

def cuadro(r,c,car):
    print(f"Tu cuadro tiene {r} x {c} dimensiones y es del catacter {car}")
    for i in range(r+1):
        for i in range(1, c+1):
            print(car, end=" ")
        print("\r")

while True:
    os.system("cls")

    #cuadro ( 2, 4,"$")

    r=int(input("Renglones ? "))
    c= int(input("Columnas ? "))
    car = input("Caracter ? ")
    cuadro(r,c,car)
    res = input("Deseas otra tabla (S/N)?").upper()
    if res=="N":
        break
    