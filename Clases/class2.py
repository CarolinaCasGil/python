class Animal:
    def emitir_sonido(self):
        pass

class Mamifero(Animal):
    def dar_a_luz(self):
        pass

class Ave(Animal):
    def poner_huevos(self):
        pass

class León(Mamifero):
    def emitir_sonido(self):
        return "Rugido"

class Pingüino(Ave):
    def emitir_sonido(self):
        return "Honk"

