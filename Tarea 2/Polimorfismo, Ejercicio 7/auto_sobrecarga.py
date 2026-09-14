class Auto:
    def __init__(self, *args):
        if len(args) == 2:
            self.marca, self.modelo = args
            self.color = "Sin color"
            self.gasolina = 0
        elif len(args) == 4:
            self.marca, self.modelo, self.color, self.gasolina = args
        else:
            self.marca = "Desconocido"
            self.modelo = "Desconocido"
            self.color = "Sin color"
            self.gasolina = 0

    def __pos__(self):
        self.gasolina += 5
        return self

    def __add__(self, nuevo_color):
        self.color = nuevo_color
        return self

    def __sub__(self, otro):
        return self.gasolina + otro.gasolina

    def __str__(self):
        return f"Auto(marca={self.marca}, modelo={self.modelo}, color={self.color}, gasolina={self.gasolina}L)"


if __name__ == "__main__":
    auto1 = Auto("Toyota", "Corolla")
    auto2 = Auto("Nissan", "Sentra", "Rojo", 40)

    print(auto1)
    print(auto2)

    auto1 = +auto1
    print(auto1)

    auto2 = auto2 + "Azul"
    print(auto2)

    total_gasolina = auto1 - auto2
    print("Gasolina total entre los dos autos:", total_gasolina, "L")
