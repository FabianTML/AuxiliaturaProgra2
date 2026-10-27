from __future__ import annotations

import consola
from aplicacion import Aplicacion
from laptop import Laptop

MODELOS = ("ThinkPad", "MacBook", "Inspiron", "Aspire", "ZenBook", "Pavilion")
TIPOS_PANTALLA = ("LED", "OLED", "IPS", "LCD")
RESOLUCIONES = ((1366, 768), (1600, 900), (1920, 1080), (2560, 1440))
NOMBRES_APPS = (
    "Chrome", "Word", "Excel", "Zoom", "Spotify", "Slack",
    "Teams", "Photoshop", "VSCode", "Steam", "Discord", "Firefox",
)
TAMANIOS_APPS = (120, 450, 120, 800, 450, 200)


def instanciar_de_ejemplo(n: int) -> list[Laptop]:
    laptops = []
    for i in range(n):
        ancho, alto = RESOLUCIONES[i % len(RESOLUCIONES)]
        laptop = Laptop(
            f"{MODELOS[i % len(MODELOS)]}-{i + 1}",
            TIPOS_PANTALLA[(i // 2) % len(TIPOS_PANTALLA)],
            ancho,
            alto,
        )
        for j in range(2 + (i * 7) % 11):
            laptop.agregar_app(Aplicacion(
                NOMBRES_APPS[(i + j) % len(NOMBRES_APPS)],
                TAMANIOS_APPS[(i * 3 + j) % len(TAMANIOS_APPS)],
            ))
        laptops.append(laptop)
    return laptops


def instanciar_manual(n: int) -> list[Laptop]:
    laptops = []
    for i in range(n):
        print(f"--- Laptop {i + 1} de {n} ---")
        modelo = consola.leer_texto("Modelo: ")
        tipo = consola.leer_texto("Tipo de pantalla: ")
        ancho = consola.leer_entero("Ancho de pantalla: ", minimo=1)
        alto = consola.leer_entero("Alto de pantalla: ", minimo=1)
        laptop = Laptop(modelo, tipo, ancho, alto)
        cantidad = consola.leer_entero(
            f"Cantidad de aplicaciones (0-{Laptop.MAX_APPS}): ", minimo=0, maximo=Laptop.MAX_APPS
        )
        for j in range(1, cantidad + 1):
            nombre = consola.leer_texto(f"  Aplicación {j} - nombre: ")
            tamanio = consola.leer_entero(f"  Aplicación {j} - tamaño: ", minimo=1)
            laptop.agregar_app(Aplicacion(nombre, tamanio))
        laptops.append(laptop)
    return laptops


def obtener_laptops() -> list[Laptop]:
    n = consola.leer_entero("Cantidad de laptops (N): ", minimo=1)
    manual = consola.leer_si_no("¿Cargar los datos manualmente? Con 'n' se usan datos de ejemplo")
    print()
    return instanciar_manual(n) if manual else instanciar_de_ejemplo(n)


def mostrar(laptops: list[Laptop]) -> None:
    for i, laptop in enumerate(laptops, start=1):
        print(f"{i}) {laptop}")


def main() -> None:
    laptops = obtener_laptops()
    print(f"Se instanciaron {len(laptops)} laptops:")
    mostrar(laptops)


if __name__ == "__main__":
    main()
