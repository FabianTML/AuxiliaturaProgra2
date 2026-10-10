class Animal:
    
    def __init__(self, edad, peso, especie):
        self._edad = edad
        self._peso = peso
        self._especie = especie

    def respirar(self):
        print(f"El {self._especie} necesita oxígeno para vivir")

    def mover(self):
        print(f"El {self._especie} se mueve de un lugar a otro")

    def mostrarDatos(self):
        print(f"Animal: {self._especie}, edad: {self._edad} años, peso: {self._peso} kg")





class Terrestre(Animal):
    def __init__(self, edad, peso, especie, numPatas, habitat):
        super().__init__(edad, peso, especie)
        self.__numPatas = numPatas
        self.__habitat = habitat

    def correr(self):
        print(f"El {self._especie} corre con sus {self.__numPatas} patas")

    def cavar(self):
        print(f"El {self._especie} cava en su hábitat: {self.__habitat}")

    def respirar(self):
        super().respirar()
        print("Respira aire mediante sus pulmones")

    def mover(self):
        print(f"El {self._especie} camina o corre por el suelo")

    def mostrarDatos(self):
        super().mostrarDatos()
        print(f"Patas: {self.__numPatas}, hábitat: {self.__habitat}")





class Acuatico(Animal):
    def __init__(self, edad, peso, especie, tipoAgua, profundidadMax):
        super().__init__(edad, peso, especie)
        self.__tipoAgua = tipoAgua
        self.__profundidadMax = profundidadMax

    def nadar(self):
        print(f"El {self._especie} nada en agua {self.__tipoAgua}")

    def sumergirse(self):
        print(f"El {self._especie} alcanza {self.__profundidadMax} metros de profundidad")

    def respirar(self):
        super().respirar()
        print("Obtiene oxígeno del agua mediante sus branquias")

    def mover(self):
        print(f"El {self._especie} nada usando sus aletas")

    def mostrarDatos(self):
        super().mostrarDatos()
        print(f"Tipo de agua: {self.__tipoAgua}, profundidad máxima: {self.__profundidadMax} m")





class Aereo(Animal):
    def __init__(self, edad, peso, especie, envergadura, alturaVuelo):
        super().__init__(edad, peso, especie)
        self.__envergadura = envergadura
        self.__alturaVuelo = alturaVuelo

    def volar(self):
        print(f"El {self._especie} vuela con una envergadura de {self.__envergadura} m")

    def aterrizar(self):
        print(f"El {self._especie} aterriza desde {self.__alturaVuelo} metros de altura")

    def respirar(self):
        super().respirar()
        print("Respira con pulmones y sacos aeereos")

    def mover(self):
        print(f"El {self._especie} vuela batiendo sus alas")

    def mostrarDatos(self):
        super().mostrarDatos()
        print(f"Envergadura: {self.__envergadura} m, altura de vuelo: {self.__alturaVuelo} m")


if __name__ == "__main__":
    perro = Terrestre(5, 20.5, "Perro", 4, "doméstico")
    delfin = Acuatico(8, 150.0, "delfin", "salada", 300)
    aguila = Aereo(3, 4.2, "Águila", 2.1, 1500)

    animales = [perro, delfin, aguila]

    for animal in animales:
        animal.mostrarDatos()
        animal.respirar()
        animal.mover()
        print()

    perro.correr()
    perro.cavar()
    delfin.nadar()
    delfin.sumergirse()
    aguila.volar()
    aguila.aterrizar()