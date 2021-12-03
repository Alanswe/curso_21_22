# Vamos a crear una clase llamada Persona. 
# Sus atributos son: nombre, edad y DNI. 
# Construye los siguientes métodos para la clase:
# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. 
# Hay que validar las entradas de datos.
# mostrar(): Muestra los datos de la persona.
# esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.


class Persona():
    # Constructor con datos vacios

    def __init__(self, edad, nombre, DNI) -> None:
        self.edad = edad
        self.nombre = nombre
        self.DNI = DNI

    # Los setters y getters para cada uno de los atributos. 
    
    def edad(self, e):
        if e < 18: 
            return 'Lo siento, no eres mayor de edad'
        else:
            return self.edad

    def nombre(self, n):
        return self.nombre

    def dni(self, d):
        return self.dni

pepe = Persona().edad(15)

juan = Persona().edad(19)

print(pepe)
print(juan)