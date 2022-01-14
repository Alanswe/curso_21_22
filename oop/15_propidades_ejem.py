# una clase persona que tenga nombre, fecha y apellido
from datetime import date

class Persona():

    def __init__(self,nombre, apellido,fecha_nacimiento) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
    
    def get_all(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}, fecha_nacimiento: {self.fecha_nacimiento}'

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, new_nombre):
        self.nombre = new_nombre

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self,fecha):
        self._fecha_nacimiento = fecha

p1 = Persona('Pepe','Perez','01/05/1998')

print(p1.get_all())
print(p1.fecha_nacimiento)
print('Se cambia con el setter...')
p1.fecha_nacimiento = '01/01/2020'
print(p1.fecha_nacimiento)
print(p1.get_all())
