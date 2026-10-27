from A import mostrar, obtener_laptops
from B import mostrar_con_mas_apps


def main() -> None:
    laptops = obtener_laptops()
    print("Laptops cargadas:")
    mostrar(laptops)
    print()
    mostrar_con_mas_apps(laptops)


if __name__ == "__main__":
    main()
