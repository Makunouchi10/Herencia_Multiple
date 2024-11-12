from area import Area
from empleado import Empleado

class JefeDeArea(Empleado, Area):
    def __init__(self, nombre, edad, salario, ubicacion, num_empleados, equipo):
        Empleado.__init__(self, nombre, edad, salario)  # Inicializa a través de Empleado
        Area.__init__(self, ubicacion, num_empleados)    # Inicializa a través de Area
        self._equipo = equipo

    def mostrar_informacion(self):
        area_info = super().mostrar_informacion()
        return f"{area_info}, Equipo de trabajo: {self._equipo}"
