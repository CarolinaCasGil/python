class Forma:
    def area(self):
        pass

    def perimetro(self):
        pass

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14 * self.radio**2

    def perimetro(self):
        return 2 * 3.14 * self.radio

class Rectangulo(Forma):
    def __init__(self, ancho, altura):
        self.ancho = ancho
        self.altura = altura

    def area(self):
        return self.ancho * self.altura

    def perimetro(self):
        return 2 * (self.ancho + self.altura)

class Triangulo(Forma):
    def __init__(self, base, altura, lado1, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def area(self):
        return 0.5 * self.base * self.altura

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3
