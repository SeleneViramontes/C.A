#Calcular el area de un circulo

import math # se importa la libreria de constantes y funciones matematicas

print('Calculando el area de un circulo \n')

radio=float(input('Dame el radio del circulo: '))

#area=3.1416*radio*radio

area=math.pi*math.pow(radio,2)

#print('El circulo del radio', radio, 'tiene un area de', area)
print(f'El circulo de radio {radio}, tiene un area de {area:.2f}')