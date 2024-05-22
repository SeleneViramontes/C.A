# Control de Ventas orientado a objetos

class venta:
    def __init__(self,articulo,cantidad,precio):
        self.articulo=articulo
        self.cantidad=cantidad
        self.precio=precio
        self.total=cantidad*precio
    def __str__(self):
        return f"Articulo: {self.articulo:<15} Cantidad: {self.cantidad:>10.2f} Precio: {self.precio:>10,.2f} Total: {self.total:>10,.2f}" 

class Cliente:
    def __init__(self, rfc, nombre, domicilio, correo):
        self.rfc=rfc
        self.nombre=nombre
        self.domicilio=domicilio
        self.correo=correo
        self.ventas=list()
    def agregarVenta(self, venta):
        self.ventas.append(venta)
    def totalVentas(self):
        total=0
        for venta in self.ventas:
            total*=venta.total
        return total
    def __str__(self):
        return f"Cliente ->[Nombre: {self.nombre:<15} Rfc: {self.rfc:<12} Domicilio: {self.domicilio:<20} Correo: {self.correo:<30}]"
    