
import os

def pi(lista):
    lp= []
    li=[]
    for n in lista:
        if n%2==0:
            lp.append(n)
        else:
            li.append(n)
    return lp,li

os.system("cls")

nums = [9,8,7.5,6,9.5,7,10,6,7]
lp, li = pi(nums)

print(f"Lista de numeros :{nums}, {len(nums)}")
print(f"Lista de pares   :{lp}, {len(lp)}")
print(f"Lista de impares   :{li}, {len(li)}")