# Leer datos y enviar un saludo

print('Leyendo datos y enviando un saludo: \n')

nombre = input('Dame tu nombre:')
edad=input('Dame tu edad:')
peso= float(input('Dame tu peso:'))

print('Tu nombre es ' + nombre + " Tu edad es " + str(edad) + " Tu peso es " + str(peso))
print('Tu nombre es ' , nombre, ' Tu edad es' , edad, ' Tu peso es' , peso)
print(f'Tu nombre es {nombre}, Tu edad es {edad}, Tu peso es {peso}')

alerta = peso > 65

print(alerta)

print(type(nombre))
print(type(edad))
print(type(peso))
