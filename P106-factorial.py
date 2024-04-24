
def fac(n):
    f=1
    for n in range(1, n+1):
        f=f*n
    return f

n=int(input("Dame un numero y te regreso el factorial ?"))
print(f"El factorial de {n} es {fac(n)}")
