from claseBaile import ClaseBaile

class NivelClase(ClaseBaile):
    def __init__(self, nombre, direccion, horario, nombre_clase, duracion, nivel):
        super().__init__(nombre, direccion, horario, nombre_clase, duracion)
        self._nivel = nivel

    # Getters y Setters
    def get_nivel(self):
        return self._nivel

    def set_nivel(self, nivel):
        self._nivel = nivel

    def info_nivel(self):
        return f"Nivel de la Clase: {self._nivel}"
