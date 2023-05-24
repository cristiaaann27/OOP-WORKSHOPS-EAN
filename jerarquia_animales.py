# Clase abstracta Animal
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def moverse(self):
        pass

    def sonido(self):
        pass


# Clase Mamífero, hereda de Animal
class Mamifero(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def moverse(self):
        return "El mamífero se mueve caminando."

    def sonido(self):
        return "El mamífero emite un sonido."


# Clase Ave, hereda de Animal
class Ave(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def moverse(self):
        return "El ave se mueve volando."

    def sonido(self):
        return "El ave emite un canto."


# Clase Reptil, hereda de Animal
class Reptil(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def moverse(self):
        return "El reptil se mueve arrastrándose."

    def sonido(self):
        return "El reptil no emite sonidos."


# Clase MamíferoAve, hereda de Mamífero y Ave
class MamiferoAve(Mamifero, Ave):
    def __init__(self, nombre):
        super().__init__(nombre)


# Crear instancias de los animales
perro = Mamifero("Perro")
pato = Ave("Pato")
serpiente = Reptil("Serpiente")
quirquincho = MamiferoAve("Quirquincho")

# Ejemplo de uso
print(perro.moverse())  # Salida: El mamífero se mueve caminando.
print(pato.moverse())  # Salida: El ave se mueve volando.
print(serpiente.sonido())  # Salida: El reptil no emite sonidos.
print(quirquincho.moverse())  # Salida: El mamífero se mueve caminando.
print(quirquincho.sonido())  # Salida: El mamífero emite un sonido.
