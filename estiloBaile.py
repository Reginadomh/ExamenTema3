from claseBaile import ClaseBaile

class EstiloBaile(ClaseBaile):
    def __init__(self, nombre, direccion, horario, nombre_clase, duracion, estilo):
        super().__init__(nombre, direccion, horario, nombre_clase, duracion)
        self._estilo = estilo

    # Getters y Setters
    def get_estilo(self):
        return self._estilo

    def set_estilo(self, estilo):
        self._estilo = estilo

    def info_estilo(self):
        return f"Estilo de Baile: {self._estilo}"
