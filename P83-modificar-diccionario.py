# Crear un diccionario de llaves de cadena países, con los siguientes elementos

import os; os.system("cls")

# Crear el diccionario de países
paises = {"Argentina": 100, "Brasil": 200, 
          "Colombia": 300, "Chile": 400, 
          "Ecuador": 500, "Bolivia": 600, "Jamaica": 700
        }

# Mostrar el diccionario completo
print("Diccionario de países completo:")
print(paises)

# Modificar Brasil por 250 usando []
paises["Brasil"] = 250

# Modificar Chile por 450 usando []
paises["Chile"] = 450

# Modificar Bolivia por 650 usando update()
paises.update({"Bolivia": 650})

# Modificar Jamaica por 750 usando update()
paises.update({"Jamaica": 750})

# Mostrar el diccionario completo después de las modificaciones
print("\nDiccionario de países después de las modificaciones:")
print(paises)