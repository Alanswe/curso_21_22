# Ejercicio 2 de Alan Sweere Segovia
"""
2.	 Crear una clase Persona, que permita recopilar los siguientes datos referidos a una persona:

-	Nombre
-	Apellidos
-	Edad
-	DNI

Al escribir una expresión como print(pers), debe mostrar todos los datos de la persona 'pers'

"""

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

    def datos(self):
        return 'Datos de persona: ', self.nombre, self.apellidos, self.edad, self.dni

# Persona de prueba ----------------------------------------------------------------------

# Esto es para el ejercicio 3
lista_personas = [Persona('Alan', 'Sweere', 24, '2222235222H'),Persona('Pepe', 'Modesto', 29, '28645835222H')]

pers = Persona('Alan', 'Sweere', 24, '2222235222H').datos()
# pers = lista_personas[0].datos() # Esto es otra manera de crear el mismo objeto pero con la 'lista_personas'

# Pruebas -----------------------------------------------------------------------------------

print(pers)
