class Vehiculo:
    def __init__(self, marca, modelo, anio, kilometraje, color):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = kilometraje
        self.color = color

    def mostrar_kilometraje(self):
        km = self.kilometraje
        metros = self.kilometraje * 1000
        print(f"{self.marca} {self.modelo}: {km} km  =  {metros} m")

    def cambiar_color(self, nuevo_color):
        color_anterior = self.color
        self.color = nuevo_color
        print(f"El color del {self.marca} {self.modelo} cambió "
              f"de '{color_anterior}' a '{nuevo_color}'.")

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.anio}")
        print(f"Color: {self.color}")
        self.mostrar_kilometraje()

if __name__ == "__main__":
    auto1 = Vehiculo("Toyota", "Corolla", 2020, 45000, "Blanco")
    auto2 = Vehiculo("Chevrolet", "Spark", 2018, 32000, "Rojo")

    print("Auto 1:-----")
    auto1.cambiar_color("Negro")
    auto1.mostrar_kilometraje()

    print("\nAuto 2:-----")
    auto2.cambiar_color("Azul")
    auto2.mostrar_kilometraje()

    print("\n---Información completa---")
    auto1.mostrar_info()
    print()
    auto2.mostrar_info()