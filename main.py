from director import Director
from gerente import Gerente
from jefeArea import JefeDeArea

# Crear instancias de las clases con los parámetros correctos
director = Director("Laura González", 45, 50000, "Edificio A", 10, 200000)
gerente = Gerente("José Martínez", 38, 20000, "Edificio B", 5, ["Hunter x Hunter", "One Punch Man"])
jefe_area = JefeDeArea("Ana Torres", 40, 15000, "Edificio C", 3, "Equipo de ventas")

# Mostrar la información
print(director.mostrar_informacion())
print(gerente.mostrar_informacion())
print(jefe_area.mostrar_informacion())
