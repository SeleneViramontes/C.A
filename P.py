import os; os.system("cls")
class Jugador:
    def __init__(self, nombre, año_nac, sexo, becado):
        self.nombre = nombre
        self.año_nac = año_nac
        self.sexo = sexo
        self.becado = becado

    def __str__(self):
        beca_status = "Becado" if self.becado else "Sin Beca"
        return f"Nombre: {self.nombre} AñoNac: {self.año_nac} Sexo: {self.sexo} Becado: {beca_status}"


class Categoria:
    def __init__(self, nombre, rango, costo):
        self.nombre = nombre
        self.rango = rango
        self.costo = costo
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def total_jugadores(self):
        return len(self.jugadores)

    def total_hombres(self):
        return sum(1 for jugador in self.jugadores if jugador.sexo == 'Hombre')

    def total_mujeres(self):
        return sum(1 for jugador in self.jugadores if jugador.sexo == 'Mujer')

    def subtotal(self):
        return sum(self.costo for jugador in self.jugadores if not jugador.becado)

    def __str__(self):
        jugadores_info = "\n".join(str(jugador) for jugador in self.jugadores)
        return (f"> {self.nombre} - {self.rango} - ({self.total_jugadores()})\n"
                f"{jugadores_info}\n- SubTotal : ${self.subtotal():.2f}\n")


class Academia:
    def __init__(self, nombre, propietario, domicilio):
        self.nombre = nombre
        self.propietario = propietario
        self.domicilio = domicilio
        self.categorias = []

    def agregar_categoria(self, categoria):
        self.categorias.append(categoria)

    def total_categorias(self):
        return len(self.categorias)

    def total_hombres(self):
        return sum(categoria.total_hombres() for categoria in self.categorias)

    def total_mujeres(self):
        return sum(categoria.total_mujeres() for categoria in self.categorias)

    def total_ingresos(self):
        return sum(categoria.subtotal() for categoria in self.categorias)

    def reporte(self):
        categorias_info = "\n\n".join(str(categoria) for categoria in self.categorias)
        categorias_generales = "\n".join(
            f"Nombre: {categoria.nombre} Rango: {categoria.rango} Costo: ${categoria.costo:.2f}"
            for categoria in self.categorias
        )
        return (f"REPORTE DEL CLUB DEPORTIVO\n"
                f"Nombre: {self.nombre}\n"
                f"Propietario: {self.propietario}\n"
                f"Domicilio: {self.domicilio}\n"
                f"Total de Categorias: {self.total_categorias()}\n"
                f"Total de Hombres: {self.total_hombres()}\n"
                f"Total de Mujeres: {self.total_mujeres()}\n"
                f">> Datos generales de las Categorías\n"
                f"{categorias_generales}\n\n"
                f">> Jugadores por Categoría:\n"
                f"{categorias_info}\n"
                f"-> Total : ${self.total_ingresos():.2f}")

