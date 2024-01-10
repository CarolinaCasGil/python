import random
import time

class Pou:
    def __init__(self, nombre):
        self.nombre = nombre
        self.edad = 0
        self.hambre = 0
        self.energia = 100
        self.felicidad = 75
        self.salud = 100
        self.vivo = True

    def estado(self):
        print("\n=== Estado de Pou ===")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Hambre: {self.hambre}")
        print(f"Energía: {self.energia}")
        print(f"Felicidad: {self.felicidad}")
        print(f"Salud: {self.salud}")

    def __str__(self):
        return f"\n=== Estado de Pou ===\nNombre: {self.nombre}\nEdad: {self.edad}\nHambre: {self.hambre}\nEnergía: {self.energia}\nFelicidad: {self.felicidad}\nSalud: {self.salud}"

    def jugar(self):
        tiempo_juego = random.uniform(0.5, 3.0)  # Simular el tiempo que dedica a jugar

        if tiempo_juego < 1.5:
            self.mostrar_animacion(f"\033[93mJugando por poco tiempo...\033[0m")
            self.hambre += random.randint(1, 2)
            self.energia -= random.randint(1, 2)
            self.felicidad += random.randint(2, 4)
        else:
            self.mostrar_animacion(f"\033[91mJugando por mucho tiempo...\033[0m")
            self.hambre += random.randint(1, 3)
            self.energia -= random.randint(2, 4)
            self.felicidad += random.randint(4, 8)
            self.salud -= random.randint(1, 3)
            self.edad += random.randint(1, 5)

        self.verificar_estado()

    def comer(self):
        self.mostrar_animacion("\033[93mComiendo...\033[0m")
        self.hambre -= 3
        self.energia += 2
        self.felicidad += 1
        self.salud += 0.5
        self.verificar_estado()

    def dormir(self):
        self.mostrar_animacion("\033[94mDurmiendo...\033[0m")
        self.energia += 5
        self.hambre += 2
        self.felicidad += 2
        self.salud += 1
        self.verificar_estado()

    def hacer_travesura(self):
        self.mostrar_animacion("\033[91mHaciendo travesura...\033[0m")
        self.energia -= random.randint(5, 10)
        self.felicidad += random.randint(1, 5)
        self.salud -= random.randint(5, 10)
        self.verificar_estado()

    def tomar_medicina(self):
        self.mostrar_animacion("\033[95mTomando medicina...\033[0m")

        # Simular la selección de un tipo de medicina
        tipo_medicina = random.randint(1, 5)

        if tipo_medicina == 1:
            print(f"\n{self.nombre} ha tomado una medicina común. Se siente mejor.")
            self.salud += random.randint(10, 15)
            self.felicidad += random.randint(3, 7)
            self.hambre -= random.uniform(0.5, 1.5)
        elif tipo_medicina == 2:
            print(f"\n{self.nombre} ha tomado una medicina especial. ¡Recupera mucha salud y felicidad!")
            self.salud += random.randint(15, 20)
            self.felicidad += random.randint(5, 10)
            self.hambre -= random.uniform(1.0, 2.0)
        elif tipo_medicina == 3:
            print(f"\n{self.nombre} ha tomado una medicina potente. ¡Recupera salud, felicidad y energía!")
            self.salud += random.randint(20, 25)
            self.felicidad += random.randint(7, 12)
            self.hambre -= random.uniform(1.5, 3.0)
            self.energia += random.uniform(1.0, 2.5)
        else:
            print(f"\n{self.nombre} ha tomado una medicina suave. Se siente aliviado.")
            self.salud += random.randint(8, 12)
            self.felicidad += random.randint(2, 5)
            self.hambre -= random.uniform(0.3, 1.0)

        self.verificar_estado()

    def viajar(self):
        self.mostrar_animacion("\033[96mViajando...\033[0m")
        self.energia -= random.randint(10, 20)
        self.felicidad += random.randint(5, 10)
        self.salud -= random.randint(5, 15)
        self.edad += random.uniform(0.5, 2.0)

        # Simular un evento aleatorio durante el viaje
        evento_viaje = random.randint(1, 10)

        if evento_viaje <= 3:
            print(f"\n¡Oh no! {self.nombre} se ha caído del avión. ¡Se ha ido al cielo!")
            self.salud = 0
        elif 4 <= evento_viaje <= 7:
            print(f"\nEl viaje de {self.nombre} no fue muy bueno. Está muy cansado.")
            self.energia -= 10
        else:
            print(f"\n¡El viaje de {self.nombre} fue increíble! Ha subido la felicidad.")
            self.felicidad += 10

        self.verificar_estado()

    def salir_del_juego(self):
        self.mostrar_animacion("\033[1;31mSaliendo del juego...\033[0m")
        print(f"\n{self.nombre} ha decidido salir del juego. ¡Hasta pronto!")
        exit()

    def verificar_estado(self):
        if self.hambre > 10 or self.energia < 0 or self.salud <= 0:
            print(f"{self.nombre} no se siente bien...")
            self.vivo = False
            self.estado()
            print("Juego terminado.")
            exit()

    def mostrar_animacion(self, mensaje):
        for _ in range(3):  # Repetir la animación 3 veces
            print(f"\r{mensaje}", end="", flush=True)
            time.sleep(0.5)  # Pausa de 0.5 segundos entre cada iteración
            print("\r              ", end="", flush=True)  # Borrar la línea después de cada iteración
            time.sleep(0.1)  # Breve pausa antes de la siguiente iteración
        print()  # Salto de línea después de la animación

# Instancia del juego
toto = Pou("Toto")

# Bucle principal del juego
while toto.vivo:
    toto.estado()
    opcion = input("\n¿Qué quieres hacer? (jugar, comer, dormir, travesura, medicina, viajar, salir): ")

    if opcion == "jugar":
        toto.jugar()
    elif opcion == "comer":
        toto.comer()
    elif opcion == "dormir":
        toto.dormir()
    elif opcion == "travesura":
        toto.hacer_travesura()
    elif opcion == "medicina":
        toto.tomar_medicina()
    elif opcion == "viajar":
        toto.viajar()
    elif opcion == "salir":
        toto.salir_del_juego()
    else:
        print("Opción no válida. Por favor, elige de nuevo.")
