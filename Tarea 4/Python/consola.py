from __future__ import annotations


def _describir_rango(minimo: int | None, maximo: int | None) -> str:
    if minimo is not None and maximo is not None:
        return f"entre {minimo} y {maximo}"
    if minimo is not None:
        return f"mayor o igual a {minimo}"
    return f"menor o igual a {maximo}"


def leer_texto(mensaje: str) -> str:
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("El valor no puede estar vacío.")


def leer_entero(mensaje: str, minimo: int | None = None, maximo: int | None = None) -> int:
    while True:
        try:
            valor = int(input(mensaje).strip())
        except ValueError:
            print("Ingrese un número entero válido.")
            continue
        fuera_de_rango = (minimo is not None and valor < minimo) or (maximo is not None and valor > maximo)
        if not fuera_de_rango:
            return valor
        print(f"Ingrese un número {_describir_rango(minimo, maximo)}.")


def leer_si_no(mensaje: str) -> bool:
    while True:
        respuesta = input(f"{mensaje} (s/n): ").strip().lower()
        if respuesta == "s":
            return True
        if respuesta == "n":
            return False
        print("Responda 's' o 'n'.")
