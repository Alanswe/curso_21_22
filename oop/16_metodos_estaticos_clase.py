# class Ejemplos():
#     #saludo = 'Hello'

#     @classmethod
#     def configurar(cls):
#         return 'Método de clase', cls

#     def suma(self,a,b):
#         return a + b

# e = Ejemplos()
# print(e.suma(1,2))

# print(Ejemplos.configurar())

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

x = Estudiante.estudiante_desde_json({'nombre': 'Paco', 'apellidos': 'Lopez Garcia'})
print(x)