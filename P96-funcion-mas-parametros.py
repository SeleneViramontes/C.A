
def saluda (*nombres):
    print(f"Saludos a: {nombres}")

    print(f"Saludos especiales a {nombres[0]}")
    for n in nombres:
        print(f" Hola {n} bienvenido a Python, nos da gusto tenerte aqui")

saluda("Carlos", "Jose","Juan", "Pedro", "Luis", "Maria", "Teresa", "Santiago",10,20)