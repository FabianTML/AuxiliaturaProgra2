class SerVivo:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Animal(SerVivo):
    def __init__(self, nombre, edad, habitat):
        super().__init__(nombre, edad)
        self.habitat = habitat


class Planta(SerVivo):
    def __init__(self, nombre, edad, necesita_sol):
        super().__init__(nombre, edad)
        self.necesita_sol = necesita_sol


class Felino(Animal):
    def __init__(self, nombre, edad, habitat, tiene_garras):
        super().__init__(nombre, edad, habitat)
        self.tiene_garras = tiene_garras


class Roedor(Animal):
    def __init__(self, nombre, edad, habitat, longitud_cola):
        super().__init__(nombre, edad, habitat)
        self.longitud_cola = longitud_cola


class Reptil(Animal):
    def __init__(self, nombre, edad, habitat, tiene_escamas):
        super().__init__(nombre, edad, habitat)
        self.tiene_escamas = tiene_escamas


class Humano(Animal):
    def __init__(self, nombre, edad, habitat, profesion):
        super().__init__(nombre, edad, habitat)
        self.profesion = profesion


class Flor(Planta):
    def __init__(self, nombre, edad, necesita_sol, color, aroma):
        super().__init__(nombre, edad, necesita_sol)
        self.color = color
        self.aroma = aroma


class Gato(Felino):
    def __init__(self, nombre, edad, habitat, tiene_garras, raza):
        super().__init__(nombre, edad, habitat, tiene_garras)
        self.raza = raza


class León(Felino):
    def __init__(self, nombre, edad, habitat, tiene_garras, tiene_melena):
        super().__init__(nombre, edad, habitat, tiene_garras)
        self.tiene_melena = tiene_melena


class Ratón(Roedor):
    def __init__(self, nombre, edad, habitat, longitud_cola, color_pelaje):
        super().__init__(nombre, edad, habitat, longitud_cola)
        self.color_pelaje = color_pelaje


class Conejo(Roedor):
    def __init__(self, nombre, edad, habitat, longitud_cola, longitud_orejas):
        super().__init__(nombre, edad, habitat, longitud_cola)
        self.longitud_orejas = longitud_orejas


class Vivora(Reptil):
    def __init__(self, nombre, edad, habitat, tiene_escamas, es_venenosa):
        super().__init__(nombre, edad, habitat, tiene_escamas)
        self.es_venenosa = es_venenosa


class Rana(Reptil):
    def __init__(self, nombre, edad, habitat, tiene_escamas, es_acuatica):
        super().__init__(nombre, edad, habitat, tiene_escamas)
        self.es_acuatica = es_acuatica


class Niño(Humano):
    def __init__(self, nombre, edad, habitat, profesion, grado_escolar):
        super().__init__(nombre, edad, habitat, profesion)
        self.grado_escolar = grado_escolar


class Adulto(Humano):
    def __init__(self, nombre, edad, habitat, profesion, estado_civil):
        super().__init__(nombre, edad, habitat, profesion)
        self.estado_civil = estado_civil


class Anciano(Humano):
    def __init__(self, nombre, edad, habitat, profesion, enfermedad_cronica):
        super().__init__(nombre, edad, habitat, profesion)
        self.enfermedad_cronica = enfermedad_cronica


if __name__ == "__main__":
    ejemplos = [
        Gato("Michi", 3, "urbano", True, "Siames"),
        León("Simba", 5, "sabana", True, True),
        Ratón("Pinky", 1, "campo", 8, "gris"),
        Conejo("Bugs", 2, "campo", 5, 10),
        Vivora("Kaa", 4, "selva", True, True),
        Rana("Rene", 1, "pantano", False, True),
        Niño("Juan", 8, "urbano", "estudiante", "3ro primaria"),
        Adulto("Maria", 30, "urbano", "ingeniera", "casada"),
        Anciano("Pedro", 75, "urbano", "jubilado", "hipertension"),
        Flor("Rosa", 1, True, "rojo", "dulce"),
    ]

    for e in ejemplos:
        print(type(e).__name__, e.__dict__)
