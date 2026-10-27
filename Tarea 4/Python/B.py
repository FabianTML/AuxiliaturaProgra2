from __future__ import annotations

from A import mostrar, obtener_laptops
from laptop import Laptop


def con_mas_apps(laptops: list[Laptop]) -> list[Laptop]:
    if not laptops:
        return []
    maximo = max(laptop.cant_apps for laptop in laptops)
    return [laptop for laptop in laptops if laptop.cant_apps == maximo]


def mostrar_con_mas_apps(laptops: list[Laptop]) -> None:
    ganadoras = con_mas_apps(laptops)
    if not ganadoras:
        print("No hay laptops cargadas.")
        return
    if ganadoras[0].cant_apps == 0:
        print("Ninguna laptop tiene aplicaciones instaladas.")
        return
    print("Laptop con más aplicaciones:" if len(ganadoras) == 1 else "Laptops empatadas con más aplicaciones:")
    for laptop in ganadoras:
        print(laptop)


def main() -> None:
    laptops = obtener_laptops()
    print("Laptops cargadas:")
    mostrar(laptops)
    print()
    mostrar_con_mas_apps(laptops)


if __name__ == "__main__":
    main()
