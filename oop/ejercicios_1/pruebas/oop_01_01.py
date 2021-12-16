#                        Ejercicio 1 de OOP Alan Sweere

# 1 - Vamos a crear una clase llamada Persona. 
# 1 - 0 - Sus atributos son: nombre, edad y DNI. 
# 2 - Construye los siguientes métodos para la clase:
# 2 - 0 - Un constructor, donde los datos pueden estar vacíos.
# 2 - 1 - Los setters y getters para cada uno de los atributos. 
# 2 - 2 - Hay que validar las entradas de datos.
# 2 - 3 - mostrar(): Muestra los datos de la persona.
# 2 - 4 - esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.

# 1 - Vamos a crear una clase llamada Persona. 
class Persona():                 # 1 - 0 - Sus atributos son: nombre, edad y DNI.
    nombre = None
    edad = 0
    DNI = None
                # 1* Son atributos de la clase
    
    # 2 - Construye los siguientes métodos para la clase:
    # 2 - 0 - Un constructor, donde los datos pueden estar vacíos.
    def __init__(self, nombre, edad, DNI) -> None:
        self.edad = edad
        self.nombre = nombre
        self.DNI = DNI

                # *2 Son atributos del objeto
    # 2 - 1 - Los setters y getters para cada uno de los atributos.
    # Los getters
    def get_nombre(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad

    def get_DNI(self):
        return self.DNI
    
    # Los setters (Se puede hacer en una solo def set_all(self, a, b, c) para cambiar todos a la vez)
    # 2 - 2 - Hay que validar las entradas de datos.

    def set_nombre(self, b):
        if self.nombre != str:
            return 'Error: El valor introducido es incorrecto'
        self.nombre = b

    def set_edad(self, a):
        if self.edad != int:
            return 'Error: El valor no es un entero'
        self.edad = a

    def set_DNI(self, c):
        if self.DNI != str:
            return 'Error: El valor introducido es incorrecto'
        self.DNI = c

    # 2 - 3 - mostrar(): Muestra los datos de la persona.(Se puede hacer con return)
    def mostrar(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.DNI}'

    # 2 - 4 - esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.
    def esMayorDeEdad(self):
        if self.edad < 18: 
            #print('Lo siento', self.nombre, ', no eres mayor de edad') # Opcional pero no requerido
            return False 
        else:
            return True

# Usuarios de ejemplo para las pruebas
usuario_1 = Persona('Pepe', 15, '44566633D')
usuario_2 = Persona('Raúl', 19, '20049930')
# Pruebas --------------------------------------------------------------------
def error_valor_nombre():
    return usuario_1.set_nombre(544)

def error_valor_edad():
    return usuario_1.set_edad('Hola')
#----------------------------------
print('Probamos cambiar a un valor erroneo...')
print('Ahora el tipo es', type(usuario_1.nombre), 'y esperaba str...')
print(usuario_1.set_nombre(544))
print('Ahora el tipo es', type(usuario_1.edad), 'y esperaba int...')
print(usuario_1.set_edad('Hola'))
print('Restablecemos el error...')
usuario_1.set_nombre('Pepe')
usuario_1.set_edad(15)
print('----------------------------')
print('Probamos el get: ', usuario_1.get_edad())
print('Antes de llamar al set: ', usuario_1.nombre)
usuario_1.set_nombre('Fernado')
print('Después: ', usuario_1.nombre)
print('----------------------------')
print(usuario_1.mostrar())
usuario_2.mostrar()
print('----------------------------')
print(usuario_1.esMayorDeEdad())
print(usuario_2.esMayorDeEdad())
