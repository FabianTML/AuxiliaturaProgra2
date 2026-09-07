class Bus:
    COSTO_PASAJE = 1.50

    def __init__(self, placa, capacidad):
        self.placa = placa
        self.capacidad = capacidad
        self.pasajeros_actuales = 0

    def subir_pasajeros(self, x):
        if x <= 0:
            print("cantidad inválida de pasajeros")
            return
        disponibles = self.capacidad - self.pasajeros_actuales
        if x > disponibles:
            print(f"No hay suficientes asientos, dispnibles: {disponibles}")
            return
        self.pasajeros_actuales += x
        print(f"Subieron {x} pasajeros, total actual: {self.pasajeros_actuales}")

    def cobrar_pasaje(self, x):
        total = x * Bus.COSTO_PASAJE
        print(f"Se cobró bs. {total:.2f} por {x} pasajero(s).")
        return total

    def mostrar_asientos_disponibles(self):
        disponibles = self.capacidad - self.pasajeros_actuales
        print(f"Asientos disponibles: {disponibles}")
        return disponibles


if __name__ == "__main__":
    bus1 = Bus("ABC-123", 40)

    bus1.subir_pasajeros(15)
    bus1.cobrar_pasaje(15)
    bus1.mostrar_asientos_disponibles()

    bus1.subir_pasajeros(10)
    bus1.cobrar_pasaje(10)
    bus1.mostrar_asientos_disponibles()