                                    # Ejercicio 2 de Alan Sweere Segovia
class Persona():
    nombre = None
    apellidos = None
    edad = 0
    dni = None

    def __init__(self, nombre, apellidos, edad, dni):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.dni = dni

    def pers(self):
        return 'Datos de persona: ', self.nombre, self.apellidos, self.edad, self.dni

# Persona de prueba ----------------------------------------------------------------------

# persona_1 = Persona('Alan', 'Sweere', 24, '2222235222H') # esto es de antes del ejercicio 2
lista_personas = [Persona('Alan', 'Sweere', 24, '2222235222H'),Persona('Pepe', 'modesto', 29, '28645835222H')]

# pers = persona_1.pers() # esto es de antes del ejercicio 2
pers = lista_personas[0].pers()

# Pruebas -----------------------------------------------------------------------------------

#print(persona_1.pers()) # esto es de antes del ejercicio 2
print(pers)

