#                         Ejercicio 3 de OOP Alan Sweere

# 1- Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven
#  que deriva de la anterior.
# 1-1- Cuando se crea esta nueva clase, además del titular y la cantidad se debe 
# guardar una bonificación quemestará expresada en tanto por ciento. 

# Construye los siguientes métodos para la clase:

# 1- Un constructor.
# 2- Los setters y getters para el nuevo atributo.
# 3- En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, 
# por lo tanto hay que crear un método esTitularValido() que devuelve verdadero si el titular es
#  mayor de edad pero menor de 25 años y falso en caso contrario.
# 3-1- Además la retirada de dinero sólo se podrá hacer si el titular es válido.
# 4- El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.

# Piensa los métodos heredados de la clase madre que hay que reescribir.


# 1- Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven
#  que deriva de la anterior. 

from oop_02 import Cuenta
import os

os.system('cls')

class Cuentajoven(Cuenta):
    # 1-1-Cuando se crea esta nueva clase, además del titular y la cantidad se debe 
    # guardar una bonificación que estará expresada en tanto por ciento. 

    bonificacion = 0 # va en porcieto %
    edad = 0

    # Construye los siguientes métodos para la clase:
    # 1- Un constructor.

    def __init__(self, titular, edad, cantidad=0, bonificacion=0) -> None:
        super().__init__(titular, cantidad=cantidad)
        self.bonificacion = bonificacion
        self.edad = edad
    
    # 2- Los setters y getters para el nuevo atributo.
    # El set

    def set_bonificacion(self, bonificacion):
        self.bonificacion = bonificacion

    # El get

    def get_bonificacion(self):
        return self.bonificacion

    # 3- En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, 
    # por lo tanto hay que crear un método esTitularValido() que devuelve verdadero si el titular es
    #  mayor de edad pero menor de 25 años y falso en caso contrario.

    def esTitularValido(self):
        if self.edad < 18 or self.edad > 25: 
            return False 
        else:
            return True

    # 3-1- Además la retirada de dinero sólo se podrá hacer si el titular es válido.
    
# Cuentas de prueba
usuario_03 = Cuentajoven('Lucía', 23, 450, 10)
usuario_04 = Cuentajoven('Juanjo', 16, 2000, 5)

print('-------------------------OOP_O3------------------------------------------------')
print(usuario_03.esTitularValido())
print(usuario_04.esTitularValido())

