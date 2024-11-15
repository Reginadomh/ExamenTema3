from escuelaBaile import EscuelaBaile

class ClaseBaile(EscuelaBaile):
    def __init__(self, nombre, direccion, horario, nombre_clase, duracion):
        super().__init__(nombre, direccion, horario)
        self._nombre_clase = nombre_clase
        self._duracion = duracion
        self._estudiantes = []

    # Getters y Setters
    def get_nombre_clase(self):
        return self._nombre_clase

    def set_nombre_clase(self, nombre_clase):
        self._nombre_clase = nombre_clase

    def get_duracion(self):
        return self._duracion

    def set_duracion(self, duracion):
        self._duracion = duracion

    def get_estudiantes(self):
        return self._estudiantes

    def agregar_estudiante(self, alumno):
        self._estudiantes.append(alumno)

    def info_clase(self):
        return f"Clase de Baile: {self._nombre_clase}, Duración: {self._duracion} minutos"