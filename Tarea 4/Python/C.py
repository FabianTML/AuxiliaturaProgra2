from __future__ import annotations

import consola
from A import mostrar, obtener_laptops
from aplicacion import Aplicacion
from laptop import Laptop


def buscar_por_modelo(laptops: list[Laptop], modelo: str) -> list[Laptop]:
    buscado = modelo.strip().casefold()
    return [laptop for laptop in laptops if laptop.modelo.casefold() == buscado]


def agregar_app_a(destinos: list[Laptop], app: Aplicacion) -> None:
    for laptop in destinos:
        if laptop.agregar_app(app):
            print(f"Aplicación '{app.nombre}' agregada a la laptop {laptop.modelo}")
        else:
            print(f"La laptop {laptop.modelo} ya alcanzó el máximo de {Laptop.MAX_APPS} aplicaciones")


def main() -> None:
    laptops = obtener_laptops()
    print("Laptops cargadas:")
    mostrar(laptops)
    print()

    modelo = consola.leer_texto("Modelo X: ")
    coincidencias = buscar_por_modelo(laptops, modelo)
    if not coincidencias:
        print(f"No existe ninguna laptop del modelo {modelo}.")
        return

    nombre = consola.leer_texto("Nombre de la aplicación: ")
    tamanio = consola.leer_entero("Tamaño de la aplicación: ", minimo=1)
    print()
    agregar_app_a(coincidencias, Aplicacion(nombre, tamanio))

    print()
    print("Estado final:")
    mostrar(laptops)


if __name__ == "__main__":
    main()
