class EscuelaBaile:
    def __init__(self, nombre, direccion, horario):
        self._nombre = nombre
        self._direccion = direccion
        self._horario = horario

    # Getters y Setters
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_direccion(self):
        return self._direccion

    def set_direccion(self, direccion):
        self._direccion = direccion

    def get_horario(self):
        return self._horario

    def set_horario(self, horario):
        self._horario = horario

    def info_escuela(self):
        return f"Escuela: {self._nombre}, Dirección: {self._direccion}, Horario: {self._horario}"