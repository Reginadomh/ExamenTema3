from sesionBaile import SesionBaile

class Alumno(SesionBaile):
    def __init__(self, nombre, direccion, horario, nombre_clase, duracion, nombre_instructor, especializacion, experiencia, fecha, nombre_alumno, edad):
        super().__init__(nombre, direccion, horario, nombre_clase, duracion, nombre_instructor, especializacion, experiencia, fecha)
        self._nombre_alumno = nombre_alumno
        self._edad = edad

    # Getters y Setters
    def get_nombre_alumno(self):
        return self._nombre_alumno

    def set_nombre_alumno(self, nombre_alumno):
        self._nombre_alumno = nombre_alumno

    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        self._edad = edad

    def info_alumno(self):
        return f"Alumno: {self._nombre_alumno}, Edad: {self._edad}"