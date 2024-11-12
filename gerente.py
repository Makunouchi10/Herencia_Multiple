from area import Area
from empleado import Empleado

class Gerente(Empleado, Area):
    def __init__(self, nombre, edad, salario, ubicacion, num_empleados, proyectos):
        Empleado.__init__(self, nombre, edad, salario)  # Inicializa a través de Empleado
        Area.__init__(self, ubicacion, num_empleados)    # Inicializa a través de Area
        self._proyectos = proyectos

    def mostrar_informacion(self):
        area_info = super().mostrar_informacion()  # Llama a mostrar_informacion de Area
        return f"{area_info}, Proyectos a cargo: {self._proyectos}"
