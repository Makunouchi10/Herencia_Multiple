from persona import Persona

class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self._salario = salario

    # Métodos Getters y Setters
    def get_salario(self):
        return self._salario

    def set_salario(self, salario):
        self._salario = salario

    def mostrar_informacion(self):
        persona_info = super().mostrar_informacion()
        return f"{persona_info}, Salario: {self._salario}"
