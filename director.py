from empleado import Empleado
from area import Area

class Director(Empleado, Area):
    def __init__(self, nombre, edad, salario, ubicacion, num_empleados, presupuesto):
        Empleado.__init__(self, nombre, edad, salario)
        Area.__init__(self, ubicacion, num_empleados)
        self._presupuesto = presupuesto

    # Método específico para el Director
    def mostrar_informacion(self):
        area_info = super().mostrar_informacion()
        return f"{area_info}, Presupuesto: {self._presupuesto}"
