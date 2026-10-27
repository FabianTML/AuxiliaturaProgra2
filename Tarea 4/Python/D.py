from __future__ import annotations

import consola
from A import mostrar, obtener_laptops
from laptop import Laptop


def eliminar_apps_por_ancho(laptops: list[Laptop], ancho: int) -> int:
    afectadas = 0
    for laptop in laptops:
        if laptop.pantalla.ancho == ancho:
            laptop.eliminar_apps()
            afectadas += 1
    return afectadas


def main() -> None:
    laptops = obtener_laptops()
    print("Laptops cargadas:")
    mostrar(laptops)
    print()

    ancho = consola.leer_entero("Ancho Y de pantalla: ", minimo=1)
    afectadas = eliminar_apps_por_ancho(laptops, ancho)
    print()
    if afectadas == 0:
        print(f"No hay laptops con pantalla de ancho {ancho}.")
        return
    print(f"Se eliminaron las aplicaciones de {afectadas} laptop(s) con pantalla de ancho {ancho}.")
    print()
    print("Estado final:")
    mostrar(laptops)


if __name__ == "__main__":
    main()
