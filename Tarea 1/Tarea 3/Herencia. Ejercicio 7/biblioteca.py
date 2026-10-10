class Documento:
    def __init__(self, titulo, autores, editorial, anioPublicacion):
        self._titulo = titulo
        self._autores = list(autores)
        self._editorial = editorial
        self._anioPublicacion = anioPublicacion

    def mostrarDatos(self):
        autores = ", ".join(self._autores)
        return (
            f"Título: {self._titulo}, autores: {autores}, "
            f"editorial: {self._editorial}, año: {self._anioPublicacion}"
        )

    def copiar(self):
        return Documento(self._titulo, self._autores, self._editorial, self._anioPublicacion)

    def __str__(self):
        return f"[{self.__class__.__name__}] {self.mostrarDatos()}"


class Libro(Documento):
    def copiar(self):
        return Libro(self._titulo, self._autores, self._editorial, self._anioPublicacion)


class Revista(Documento):
    def __init__(self, titulo, autores, editorial, anioPublicacion, volumen, numero, mesSalida):
        super().__init__(titulo, autores, editorial, anioPublicacion)
        self._volumen = volumen
        self._numero = numero
        self._mesSalida = mesSalida

    def mostrarDatos(self):
        return (
            f"{super().mostrarDatos()}, volumen: {self._volumen}, "
            f"número: {self._numero}, mes: {self._mesSalida}"
        )

    def copiar(self):
        return Revista(
            self._titulo, self._autores, self._editorial, self._anioPublicacion,
            self._volumen, self._numero, self._mesSalida
        )


class DocumentoCD(Documento):
    def __init__(self, titulo, autores, editorial, anioPublicacion, formatoCD, tipoLicencia):
        super().__init__(titulo, autores, editorial, anioPublicacion)
        self._formatoCD = formatoCD
        self._tipoLicencia = tipoLicencia

    def mostrarDatos(self):
        return (
            f"{super().mostrarDatos()}, formato: {self._formatoCD}, "
            f"licencia: {self._tipoLicencia}"
        )

    def copiar(self):
        return DocumentoCD(
            self._titulo, self._autores, self._editorial, self._anioPublicacion,
            self._formatoCD, self._tipoLicencia
        )


class RevistaInvestigacion(Revista):
    def __init__(self, titulo, autores, editorial, anioPublicacion, volumen, numero,
                 mesSalida, campoInvestigacion):
        super().__init__(titulo, autores, editorial, anioPublicacion, volumen, numero, mesSalida)
        self._campoInvestigacion = campoInvestigacion

    def mostrarDatos(self):
        return f"{super().mostrarDatos()}, área de investigación: {self._campoInvestigacion}"

    def copiar(self):
        return RevistaInvestigacion(
            self._titulo, self._autores, self._editorial, self._anioPublicacion,
            self._volumen, self._numero, self._mesSalida, self._campoInvestigacion
        )


class Biblioteca:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__documentos = []

    def getNombre(self):
        return self.__nombre

    def agregarDocumento(self, documento):
        self.__documentos.append(documento)

    def cantidadDocumentos(self):
        return len(self.__documentos)

    def cantidadRevistas(self):
        return sum(1 for d in self.__documentos if isinstance(d, Revista))

    def extraerRevistas(self):
        revistas = [d for d in self.__documentos if isinstance(d, Revista)]
        self.__documentos = [d for d in self.__documentos if not isinstance(d, Revista)]
        return revistas

    def extraerLibros(self):
        libros = [d for d in self.__documentos if isinstance(d, Libro)]
        self.__documentos = [d for d in self.__documentos if not isinstance(d, Libro)]
        return libros

    def recibirDocumentos(self, documentos):
        self.__documentos.extend(documentos)

    def copiaSeguridad(self):
        copia = Biblioteca(f"{self.__nombre} (copia)")
        for documento in self.__documentos:
            copia.agregarDocumento(documento.copiar())
        return copia

    def mostrar(self):
        print(f"Biblioteca: {self.__nombre}")
        if not self.__documentos:
            print("  No hay documentos")
        for documento in self.__documentos:
            print(f"  {documento}")


def comparar(b1, b2):
    if b1.cantidadRevistas() > b2.cantidadRevistas():
        print(f"Más revistas: {b1.getNombre()} ({b1.cantidadRevistas()})")
    elif b2.cantidadRevistas() > b1.cantidadRevistas():
        print(f"Más revistas: {b2.getNombre()} ({b2.cantidadRevistas()})")
    else:
        print(f"Ambas tienen {b1.cantidadRevistas()} revistas")

    if b1.cantidadDocumentos() > b2.cantidadDocumentos():
        print(f"Más documentos: {b1.getNombre()} ({b1.cantidadDocumentos()})")
    elif b2.cantidadDocumentos() > b1.cantidadDocumentos():
        print(f"Más documentos: {b2.getNombre()} ({b2.cantidadDocumentos()})")
    else:
        print(f"Ambas tienen {b1.cantidadDocumentos()} documentos")


def trasladar(b1, b2):
    revistas = b1.extraerRevistas() + b2.extraerRevistas()
    libros = b1.extraerLibros() + b2.extraerLibros()
    b1.recibirDocumentos(revistas)
    b2.recibirDocumentos(libros)


if __name__ == "__main__":
    central = Biblioteca("Biblioteca Central")
    ingenieria = Biblioteca("Biblioteca de Ingeniería")

    central.agregarDocumento(
        Libro("Cien años de soledad", ["Gabriel García Márquez"], "Sudamericana", 1967)
    )
    central.agregarDocumento(
        Revista("National Geographic", ["Varios"], "NatGeo", 2024, 245, 3, "Marzo")
    )
    central.agregarDocumento(
        DocumentoCD("Visual Studio", ["Microsoft"], "Microsoft", 2022, "DVD", "Comercial")
    )
    central.agregarDocumento(
        RevistaInvestigacion(
            "Nature", ["Varios"], "Springer", 2023, 600, 12, "Junio", "Ciencias naturales"
        )
    )

    ingenieria.agregarDocumento(
        Libro("Clean Code", ["Robert C. Martin"], "Prentice Hall", 2008)
    )
    ingenieria.agregarDocumento(
        Libro("Estructuras de datos", ["Mark Allen Weiss", "Pearson Team"], "Pearson", 2012)
    )
    ingenieria.agregarDocumento(
        Revista("IEEE Spectrum", ["Varios"], "IEEE", 2024, 61, 8, "Agosto")
    )

    print("--- Inicio ---")
    central.mostrar()
    print()
    ingenieria.mostrar()
    print()
    comparar(central, ingenieria)

    trasladar(central, ingenieria)

    print("\n--- Traslado realizado ---")
    central.mostrar()
    print()
    ingenieria.mostrar()
    print()
    comparar(central, ingenieria)

    copiaCentral = central.copiaSeguridad()
    copiaIngenieria = ingenieria.copiaSeguridad()

    print("\n--- Copias de seguridad ---")
    copiaCentral.mostrar()
    print()
    copiaIngenieria.mostrar()