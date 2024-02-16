#Calcular la paga de un trabajador

print('Calculando la paga de un trabajador :\n')

nombre = input('Nombre del trabajador: ')
horas = int (input('Dame las horas trabajadas: '))
paga = float(input('Dame la paga por hora: '))
tasa = 0.3

pagabruta = horas * paga 
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto

print('\nResumen de pagos:\n')
print(f'El trabajador {nombre} trabajo {horas} horas con una paga de {paga} pesos y una tasa de sapuesto de {tasa}%')
print(f'Paga bruta: {pagabruta:.2f}') 
print(f'Impuesto : {impuesto:.2f}')
print(f'Paga neta : {paganeta:.2f}')