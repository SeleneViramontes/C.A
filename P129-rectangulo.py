import os

class Rectangulo:
    def __init__ (self, l, a):
        self.largo = l
        self.ancho = a
    def obtenerArea(self):
        return self.largo * self.ancho
    def obtenerPerimetro(self):
        return 2*self.largo + 2*self.ancho
    def __str__ (self):
        return f"Rectangulo [Largo={self.largo} - Ancho: {self.ancho}, Area: {self.obtenerArea():.2f}, Perimetro:{self.obtenerPerimetro():.2f}]\n"

#programa principal 
os.system("cls")

r1 = Rectangulo(12, 3.4)
print(r1)
r2 = Rectangulo(5.6, 7.8)
print(r2)
r3=Rectangulo (10,10)
print(r3)

rectangulos=[]
rectangulos.append(r1)
rectangulos.append(r2)
rectangulos.append(r3)
rectangulos.append(Rectangulo(60,40))
print(rectangulos)

print("Todos de una sola vez", len (rectangulos))

for rectangulo in rectangulos:
    print(rectangulo)