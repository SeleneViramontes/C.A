# Selene Vi8ramontes Ureño.
#La Academia de futbol Santos Laguna, desea llevar el control de los jugadores en cada categoría, las categorías se conforman de acuerdo con la edad y pueden tener varios
#jugadores. Diseña una aplicación en Python, usando los conceptos aprendidos sobre programación orientada a objetos.
import os; os.system("cls")
class Jugador:
    def __init__(self, nombre, año_nac, sexo, becado):
        self.nombre = nombre
        self.año_nac = año_nac
        self.sexo = sexo
        self.becado = becado

    def __str__(self):
        return f"Nombre: {self.nombre}, Año de Nacimiento: {self.año_nac}, Sexo: {self.sexo}, Becado: {'Sí' if self.becado else 'No'}"


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
        return sum(1 for jugador in self.jugadores if jugador.sexo == 'M')

    def total_mujeres(self):
        return sum(1 for jugador in self.jugadores if jugador.sexo == 'F')

    def subtotal(self):
        return sum(self.costo for jugador in self.jugadores if not jugador.becado)

    def __str__(self):
        jugadores_info = "\n".join(str(jugador) for jugador in self.jugadores)
        return f"Categoría: {self.nombre}\nRango: {self.rango}\nCosto: {self.costo}\nJugadores:\n{jugadores_info}\nSubtotal: {self.subtotal()}"


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
        return (f"Academia: {self.nombre}\nPropietario: {self.propietario}\nDomicilio: {self.domicilio}\n\n"
                f"Total de Categorías: {self.total_categorias()}\n"
                f"Total de Hombres: {self.total_hombres()}\n"
                f"Total de Mujeres: {self.total_mujeres()}\n\n"
                f"Datos de las Categorías:\n{categorias_info}\n\n"
                f"Total de Ingresos: {self.total_ingresos()}")


jugador1 = Jugador("Juan Perez", 2005, "M", False)
jugador2 = Jugador("Maria Lopez", 2006, "F", True)
jugador3 = Jugador("Carlos Gomez", 2004, "M", False)

# Crear categorías y agregar jugadores
categoria_infantil = Categoria("Infantil", "2004-2006", 500)
categoria_infantil.agregar_jugador(jugador1)
categoria_infantil.agregar_jugador(jugador2)

categoria_juvenil = Categoria("Juvenil", "2003-2004", 700)
categoria_juvenil.agregar_jugador(jugador3)

# Crear academia y agregar categorías
academia = Academia("Santos Laguna", "Pedro Martinez", "Calle Falsa 123")
academia.agregar_categoria(categoria_infantil)
academia.agregar_categoria(categoria_juvenil)

# Imprimir reporte
print(academia.reporte())