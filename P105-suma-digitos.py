import os; os.system("cls")
def sumadigitos(n):
    suma=0
    while n != 0:
        dig = n % 10
        suma= suma + dig
        n =n//10
    return suma

n = int(input("Dame un número entero y sumaré sus digitos? "))
print(f"El numero es {n} y la suma de sus digitos es {sumadigitos(n)}")
