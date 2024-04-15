# Crear un diccionario de llave numérica dias, con los siguientes elementos

import os; os.system("cls")

# Crear el diccionario de días
dias = {1: "Lunes", 2: "Martes", 
        3: "Miércoles", 4: "Jueves", 
        5: "Viernes", 6: "Sábado", 7: "Domingo"
        }

# Mostrar el diccionario completo
print("Diccionario de días completo:")
print(dias)
print("-"*95)

# Acceder y mostrar el primer elemento usando []
primer_elemento = dias[1]
print("Primer elemento:", primer_elemento)

# Acceder y mostrar el último elemento usando []
ultimo_elemento = dias[7]
print("Último elemento:", ultimo_elemento)

# Acceder y mostrar el quinto elemento usando get()
quinto_elemento = dias.get(5)
print("Quinto elemento:", quinto_elemento)

# Acceder y mostrar el séptimo elemento usando get()
septimo_elemento = dias.get(7)
print("Séptimo elemento:", septimo_elemento)

# Mostrar el diccionario completo nuevamente
print("-"*95)
print("Diccionario de días completo:")
print(dias)