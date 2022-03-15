
class Persona():
    
    def __init__(self,dni,nombre,apellido1,apellido2='') -> None:
        self.dni = dni
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2

    def __str__(self) -> str:
        return f'Nombre: {self.nombre}, Apellidos : {self.apellido1} {self.apellido2}, DNI: {self.dni}'