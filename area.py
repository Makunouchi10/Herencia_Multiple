from departamento import Departamento

class Area(Departamento):
    def __init__(self, ubicacion, num_empleados):
        super().__init__(ubicacion)
        self._num_empleados = num_empleados

    # Métodos Getters y Setters
    def get_num_empleados(self):
        return self._num_empleados

    def set_num_empleados(self, num_empleados):
        self._num_empleados = num_empleados

    def mostrar_informacion(self):
        departamento_info = super().mostrar_informacion()
        return f"{departamento_info}, Número de empleados: {self._num_empleados}"
