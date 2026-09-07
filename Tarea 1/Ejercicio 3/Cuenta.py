class CuentaBancaria:

    def __init__(self, titular, nro_cuenta, saldo=0):
        self.titular = titular
        self.nro_cuenta = nro_cuenta
        self.saldo = saldo

    def depositar(self, monto):
        if monto <= 0:
            print(f"Error: no se puede depositar un monto negativo o 0 "
                  f"(intentaste depositar {monto}).")
            return
        self.saldo += monto
        print(f"Depósito exitoso de {monto}, saaldo actual: {self.saldo}")

    def retirar(self, monto):
        if monto <= 0:
            print(f"Error: no se puede retirar un monto negativo o 0 "
                  f"(intentaste retirar {monto}).")
            return
        if monto > self.saldo:
            print(f"Error: fondos insuficientes, saldo disponible: "
                  f"{self.saldo}, intentaste retirar {monto}.")
            return
        self.saldo -= monto
        print(f"Retiro exitoso de {monto}, saldo actual: {self.saldo}")

    def mostrar_datos(self):
        print(f"Titular: {self.titular}")
        print(f"N° de cuenta: {self.nro_cuenta}")
        print(f"Saldo: {self.saldo}")


if __name__ == "__main__":
    cuenta = CuentaBancaria("Juan Pérez", "001-234567", 500)

    print("Datos iniciales:")
    cuenta.mostrar_datos()

    print("\nPruebas de depósito:")
    cuenta.depositar(200)
    cuenta.depositar(-50)
    cuenta.depositar(0)

    print("\nPruebas de retiro:")
    cuenta.retirar(100)
    cuenta.retirar(10000)
    cuenta.retirar(-20)

    print("\nDatos finales:")
    cuenta.mostrar_datos()