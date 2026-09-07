class Computadora:
    def __init__(self, marca="Genérica", procesador="Sin definir",
                 ram=0, almacenamiento=0):
        self.marca = marca
        self.procesador = procesador
        self.ram = ram
        self.almacenamiento = almacenamiento

    def ram_igual_a(self, x):
        return self.ram == x

    def tiene_mayor_almacenamiento(self, otra):
        return self.almacenamiento > otra.almacenamiento

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Procesador: {self.procesador}")
        print(f"RAM: {self.ram} GB")
        print(f"Almacenamiento: {self.almacenamiento} GB")


if __name__ == "__main__":
    pc1 = Computadora("HP", "Intel i5", 8, 512)

    pc2 = Computadora()
    pc2.marca = "Lenovo"
    pc2.procesador = "AMD Ryzen 7"
    pc2.ram = 16
    pc2.almacenamiento = 1024

    print("PC 1:")
    pc1.mostrar_info()
    print("\nPC 2:")
    pc2.mostrar_info()

    x = 16
    print(f"\nLa RAM de PC1 es igual a {x} GB? {pc1.ram_igual_a(x)}")
    print(f"La RAM de PC2 es igual a {x} GB? {pc2.ram_igual_a(x)}")

    print("\nComputadora con mayor almacenamiento-----------")
    if pc1.tiene_mayor_almacenamiento(pc2):
        pc1.mostrar_info()
    else:
        pc2.mostrar_info()