from __future__ import annotations

from aplicacion import Aplicacion
from pantalla import Pantalla


class Laptop:
    MAX_APPS = 50

    def __init__(self, modelo: str, tipo_pantalla: str, ancho: int, alto: int) -> None:
        if not modelo or not modelo.strip():
            raise ValueError("El modelo de la laptop es obligatorio")
        self._modelo = modelo.strip()
        self._apps: list[Aplicacion] = []
        self._pantalla = Pantalla(tipo_pantalla, ancho, alto)

    @property
    def modelo(self) -> str:
        return self._modelo

    @property
    def cant_apps(self) -> int:
        return len(self._apps)

    @property
    def apps(self) -> tuple[Aplicacion, ...]:
        return tuple(self._apps)

    @property
    def pantalla(self) -> Pantalla:
        return self._pantalla

    def agregar_app(self, app: Aplicacion) -> bool:
        if app is None or len(self._apps) >= Laptop.MAX_APPS:
            return False
        self._apps.append(app)
        return True

    def eliminar_apps(self) -> None:
        self._apps.clear()

    def ordenar_apps(self) -> None:
        self._apps.sort(key=Aplicacion.clave_orden)

    def __str__(self) -> str:
        lineas = [f"Laptop {self._modelo} | Pantalla: {self._pantalla} | Aplicaciones: {self.cant_apps}"]
        lineas.extend(f"    {i}. {app}" for i, app in enumerate(self._apps, start=1))
        return "\n".join(lineas)
