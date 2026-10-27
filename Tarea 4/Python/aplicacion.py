from __future__ import annotations


class Aplicacion:
    def __init__(self, nombre: str, tamanio: int) -> None:
        if not nombre or not nombre.strip():
            raise ValueError("El nombre de la aplicación es obligatorio")
        if tamanio <= 0:
            raise ValueError("El tamaño de la aplicación debe ser positivo")
        self._nombre = nombre.strip()
        self._tamanio = tamanio

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def tamanio(self) -> int:
        return self._tamanio

    def clave_orden(self) -> tuple[int, str]:
        return (-self._tamanio, self._nombre.casefold())

    def __str__(self) -> str:
        return f"{self._nombre} - tamaño: {self._tamanio}"
