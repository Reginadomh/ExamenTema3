class Instructor:
    def __init__(self, nombre_instructor, especializacion, experiencia):
        self._nombre_instructor = nombre_instructor
        self._especializacion = especializacion
        self._experiencia = experiencia

    # Getters y Setters
    def get_nombre_instructor(self):
        return self._nombre_instructor

    def set_nombre_instructor(self, nombre_instructor):
        self._nombre_instructor = nombre_instructor

    def get_especializacion(self):
        return self._especializacion

    def set_especializacion(self, especializacion):
        self._especializacion = especializacion

    def get_experiencia(self):
        return self._experiencia

    def set_experiencia(self, experiencia):
        self._experiencia = experiencia

    def info_instructor(self):
        return f"Instructor: {self._nombre_instructor}, Especialización: {self._especializacion}, " \
               f"Experiencia: {self._experiencia} años"