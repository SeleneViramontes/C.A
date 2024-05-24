# Selene Viramontes Ureño.
#La Academia de futbol Santos Laguna, desea llevar el control de los jugadores en cada categoría, las categorías se conforman de acuerdo con la edad y pueden tener varios
#jugadores. Diseña una aplicación en Python, usando los conceptos aprendidos sobre programación orientada a objetos.
import os; os.system("cls")
class Jugador:
    def __init__(self, nombre, ano_nac, sexo, becado):
        self.nombre = nombre
        self.ano_nac = ano_nac
        self.sexo = sexo
        self.becado = becado

    def __str__(self):
        beca = "Becado" if self.becado else "Sin Beca"
        return f"Nombre: {self.nombre} AñoNac: {self.ano_nac} Sexo: {self.sexo} Becado: {beca}"


class Categoria:
    def __init__(self, nombre, rango, costo):
        self.nombre = nombre
        self.rango = rango
        self.costo = costo
        self.jugadores = []
    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)
    def subtotal(self):
        return sum(self.costo for jugador in self.jugadores if not jugador.becado)
    def __str__(self):
        jugadores = "\n".join(str(jugador) for jugador in self.jugadores)
        subtotal = self.subtotal()
        return f" {self.nombre} - {self.rango} - ({len(self.jugadores)})\n{jugadores}\n- SubTotal : ${subtotal:.2f}"


class Academia:
    def __init__(self, nombre, propietario, domicilio):
        self.nombre = nombre
        self.propietario = propietario
        self.domicilio = domicilio
        self.categorias = []

    def agregar_categoria(self, categoria):
        self.categorias.append(categoria)
    def total_hombres(self):
        return sum(1 for categoria in self.categorias for jugador in categoria.jugadores if jugador.sexo == "Hombre")
    def total_mujeres(self):
        return sum(1 for categoria in self.categorias for jugador in categoria.jugadores if jugador.sexo == "Mujer")
    def total_ingresos(self):
        return sum(categoria.subtotal() for categoria in self.categorias)

    def reporte(self):
        resultado = (f"\nREPORTE DEL CLUB DEPORTIVO\nNombre: {self.nombre}\nPropietario: {self.propietario}\nDomicilio: {self.domicilio}\n"
                     f"Total de Categorias: {len(self.categorias)}\nTotal de Hombres: {self.total_hombres()}\nTotal de Mujeres: {self.total_mujeres()}\n"
                     "\nDatos generales de las Categorías\n")
        for categoria in self.categorias:
            resultado += f"Nombre: {categoria.nombre} Rango: {categoria.rango} Costo: ${categoria.costo:.2f}\n"
        resultado += "\nJugadores por Categoría:\n"
        for categoria in self.categorias:
            resultado += str(categoria) + "\n\n"
        resultado += f"Total : ${self.total_ingresos():.2f}"
        return resultado
    

academia = Academia("Academia Santos Laguna", "Francisco Nava", "Aguanaval 123, Hidráulica\n")

categoria1 = Categoria("Junior A", "2006/2007/2008", 1250.00)
categoria1.agregar_jugador(Jugador("Mario Lopez", 2006, "Hombre", False))
categoria1.agregar_jugador(Jugador("Uriel Solis", 2007, "Hombre", True))
categoria1.agregar_jugador(Jugador("Ana Escalona", 2008, "Mujer", False))

categoria2 = Categoria("Junior B", "2009/2010/2011", 850.00)
categoria2.agregar_jugador(Jugador("Asucena Santana", 2009, "Hombre", False))
categoria2.agregar_jugador(Jugador("David Mijares", 2010, "Hombre", False))
categoria2.agregar_jugador(Jugador("Antonio Herrera", 2011, "Mujer", True))

categoria3 = Categoria("Pony A", "2012/2013/2014", 700.00)
categoria3.agregar_jugador(Jugador("Andrea Saldivar", 2012, "Mujer", True))
categoria3.agregar_jugador(Jugador("Marissa Mijares", 2013, "Mujer", True))
categoria3.agregar_jugador(Jugador("Diego Soto", 2014, "Mujer", False))

academia.agregar_categoria(categoria1)
academia.agregar_categoria(categoria2)
academia.agregar_categoria(categoria3)

print(academia.reporte())