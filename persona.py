class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    # Métodos Getters y Setters
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        self._edad = edad

    # Método para mostrar información básica de la persona
    def mostrar_informacion(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}"
