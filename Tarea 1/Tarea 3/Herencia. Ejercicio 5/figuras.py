from abc import ABC, abstractmethod
import math


class Figura(ABC):
    def __init__(self, color):
        self._color = color

    @abstractmethod
    def obtenerArea(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__} de color {self._color} con área {self.obtenerArea():.2f}"



class Cuadrado(Figura):
    def __init__(self, color, lado):
        super().__init__(color)
        self.__lado = lado

    def obtenerArea(self):
        return self.__lado ** 2



class Triangulo(Figura):
    
    def __init__(self, color, lado1, lado2, lado3):
        super().__init__(color)
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3

    def obtenerArea(self):
        s = (self.__lado1 + self.__lado2 + self.__lado3) / 2
        return math.sqrt(
            s * (s - self.__lado1) * (s - self.__lado2) * (s - self.__lado3)
        )




class Redondo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.__radio = radio

    def obtenerArea(self):
        return math.pi * self.__radio ** 2


def mostrarMayorArea(cuadrado, triangulo):
    if cuadrado.obtenerArea() > triangulo.obtenerArea():
        mayor = cuadrado
    else:
        mayor = triangulo
    print(f"La figura con mayor área es de color: {mayor._color}")







if __name__ == "__main__":
    cuadrado1 = Cuadrado("rojo", 4)
    cuadrado2 = Cuadrado("azul", 6)
    triangulo1 = Triangulo("verde", 3, 4, 5)
    triangulo2 = Triangulo("amarillo", 6, 8, 10)
    redondo1 = Redondo("negro", 2)
    redondo2 = Redondo("blanco", 5)

    figuras = [cuadrado1, cuadrado2, triangulo1, triangulo2, redondo1, redondo2]
    for figura in figuras:
        print(figura)

    print()
    mostrarMayorArea(cuadrado1, triangulo1)
    mostrarMayorArea(cuadrado2, triangulo2)
