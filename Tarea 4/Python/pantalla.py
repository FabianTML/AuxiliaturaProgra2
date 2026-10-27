from __future__ import annotations


class Pantalla:
    def __init__(self, tipo: str, ancho: int, alto: int) -> None:
        if not tipo or not tipo.strip():
            raise ValueError("El tipo de pantalla es obligatorio")
        if ancho <= 0 or alto <= 0:
            raise ValueError("Las dimensiones de la pantalla deben ser positivas")
        self._tipo = tipo.strip()
        self._ancho = ancho
        self._alto = alto

    @property
    def tipo(self) -> str:
        return self._tipo

    @property
    def ancho(self) -> int:
        return self._ancho

    @property
    def alto(self) -> int:
        return self._alto

    def __str__(self) -> str:
        return f"{self._tipo} {self._ancho}x{self._alto}"
