class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Cliente:
    def __init__(self, nombre, correo_electronico):
        self.nombre = nombre
        self.correo_electronico = correo_electronico

class Orden:
    def __init__(self, cliente):
        self.cliente = cliente
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        return sum(producto.precio for producto in self.productos)

class CarritoDeCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        return sum(producto.precio for producto in self.productos)
