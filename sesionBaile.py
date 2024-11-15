from claseBaile import ClaseBaile
from instructor import Instructor

class SesionBaile(ClaseBaile, Instructor):
    def __init__(self, nombre, direccion, horario, nombre_clase, duracion, nombre_instructor, especializacion, experiencia, fecha):
        ClaseBaile.__init__(self, nombre, direccion, horario, nombre_clase, duracion)
        Instructor.__init__(self, nombre_instructor, especializacion, experiencia)
        self._fecha = fecha

    # Getter y Setter para la fecha
    def get_fecha(self):
        return self._fecha

    def set_fecha(self, fecha):
        self._fecha = fecha

    def info_sesion(self):
        return f"Sesión de Baile el {self._fecha}, Instructor: {self._nombre_instructor}"