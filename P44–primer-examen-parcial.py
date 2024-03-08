# ------------------------------------SELENE VIRAMONTES UREÑO----------------------------------------------
# ---------------------------------------Examen parcial I--------------------------------------------------
# -------------------------------------Computacion Aplicada----------------------------------------------

#Universidad Patio SA de CV
#Sistema de Inscripción Congreso de Sistemas     

import os; os.system("cls")

# Definición de precios
precios_usuario = {1: 100, 2: 200, 3: 500}
precios_paquete = {1: 600, 2: 800, 3: 900}

# Variables
total_ventas = 0

# Proceso de ventas
while True:
    # Solicitar datos de la venta
    tipo_usuario = int(input("---------------INGRESE EL TIPO DE USUARIO------------------------------------------------------------- \n 1: Alumno, 2: Trabajador, 3: Docente: "))
    tipo_paquete = int(input("---------------IGRESE EL TIPO DE PAQUETE------------------------------------------------------------- \n 1: Solo conferencias, 2: Con eventos sociales, 3: Con kit de acceso: "))
    cantidad = int(input("INGRESE LA CANTIDAD DE INSCRIPCIONES: "))

    # Calcular subtotal
    subtotal = (precios_usuario[tipo_usuario] + precios_paquete[tipo_paquete]) * cantidad

    # Aplicar descuento si el subtotal es mayor a 5000
    if subtotal > 5000:
        if tipo_usuario == 1:
            descuento = subtotal * 0.20
        elif tipo_usuario == 2:
            descuento = subtotal * 0.10
        elif tipo_usuario == 3:
            descuento = subtotal * 0.05
    else:
        descuento = 0

    # Calcular total de venta
    total_venta = subtotal - descuento

    # Mostrar resumen de la venta
    print("*********************************************************************************************************************")
    print("Resumen de la venta:")
    print(f"Tipo de usuario: {tipo_usuario}")
    print(f"Tipo de paquete: {tipo_paquete}")
    print(f"Cantidad: {cantidad}")
    print(f"Subtotal: ${subtotal}")
    print(f"Descuento: ${descuento}")
    print(f"Total a pagar: ${total_venta}")
    print("*********************************************************************************************************************")
    
    # Actualizar total de ventas del día
    total_ventas += total_venta

    # Verificar si se desea procesar otra venta
    continuar = input("¿Desea procesar otra venta? (s/n): ")
    if continuar.lower() != 's':
        break

# Mostrar total de ventas del día
print(f"Total de ventas del día: ${total_ventas}")

print("Proceso terminado")