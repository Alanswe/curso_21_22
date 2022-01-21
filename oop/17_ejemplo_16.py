
class Estudiante():
    def __init__(self,nombre,apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self) -> str:
        return f'Estudiante: {self.nombre} {self.apellido}'

    @classmethod
    def estudiante_desde_json(cls,obj_json): # No necesita self al ser unmetdo de clase
        estudiante = dict(obj_json) #{'nombre': 'Paco', 'apellidos': 'Lopez Garcia'}
        obj_estudiante = cls(estudiante['nombre'], estudiante['apellidos'])
        return obj_estudiante

    @classmethod
    def estudiante_desde_lista(cls,obj_alumnos): # No necesita self al ser un metodo de clase
        estudiante = cls(obj_alumnos[0],obj_alumnos[1]) #{'nombre': 'Paco', 'apellidos': 'Lopez Garcia'}
        return estudiante

x = Estudiante.estudiante_desde_json({'nombre': 'Paco', 'apellidos': 'Lopez Garcia'})
x_2 = Estudiante.estudiante_desde_lista(['Paco','Lopez Garcia'])

print(x)
print(x_2)