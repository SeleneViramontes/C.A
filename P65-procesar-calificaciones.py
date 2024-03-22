# Procesar n calificaciones producidas por el usuario

import os; os.system('cls')

print("Procesando calificaciones \n")
print("Introduce n calificaciones en el rango de 1 a 100 (99 para terminar) \n")

nums=[]
mp=[]
n=suma=prom=0


while n!=99:
    n=float(input("Numero : "))
    if n>=0 and n<=10:
        nums.append(n)
        suma +=n
    else:
        print("x")

prom=suma/ len(nums)
for n in nums:
    if n>=prom:
        mp.append(n)

print(f"\n Numeros capturados {len(nums)} : {nums}")
print("Estadisticas")
print(f"\nLa suma es: {suma} y el promedio es: {prom}, mayores al promedio: {len(mp)} y son {mp} ")
print(f"\nEl maximo es: {max(nums)} y el minimo es: {min(nums)}")

