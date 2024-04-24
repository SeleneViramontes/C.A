
def suma(n1,n2):
    s=n1+n2
    return s

print("Suma de dos numeros constantes:")
s = (100,200)
print("La suma es ",s)
print("La suma es", suma(200, 300))

print("Dame dos numeros y te devolvere la suma:")
a, b = int(input()), int(input())
res = suma(a,b)
print(f"La suma de {a} + {b} = {res}")