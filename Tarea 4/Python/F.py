from __future__ import annotations

from A import mostrar, obtener_laptops
from laptop import Laptop


def ordenar_apps_de_cada_laptop(laptops: list[Laptop]) -> None:
    for laptop in laptops:
        laptop.ordenar_apps()


def main() -> None:
    laptops = obtener_laptops()
    print("Antes de ordenar:")
    mostrar(laptops)
    print()

    ordenar_apps_de_cada_laptop(laptops)

    print("Después de ordenar (tamaño decreciente, empate por nombre):")
    mostrar(laptops)


if __name__ == "__main__":
    main()
