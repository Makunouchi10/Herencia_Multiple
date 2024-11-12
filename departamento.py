class Departamento:
    def __init__(self, ubicacion):
        self._ubicacion = ubicacion

    # Métodos Getters y Setters
    def get_ubicacion(self):
        return self._ubicacion

    def set_ubicacion(self, ubicacion):
        self._ubicacion = ubicacion

    # Método para mostrar información del departamento
    def mostrar_informacion(self):
        return f"Ubicación: {self._ubicacion}"