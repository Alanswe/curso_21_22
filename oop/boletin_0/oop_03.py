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

from oop_01 import Persona
from oop_02 import Cuenta
import os

os.system('cls')

class Cuentajoven(Cuenta, Persona):
    # 1-1-Cuando se crea esta nueva clase, además del titular y la cantidad se debe 
    # guardar una bonificación que estará expresada en tanto por ciento. 

    bonificacion = 0 # va en porcieto %
    # Construye los siguientes métodos para la clase:
    # 1- Un constructor.

    def __init__(self, nombre, edad, DNI) -> None:
        super().__init__(nombre, edad, DNI)


    def __init__(self, titular, edad, cantidad=0, bonificacion=0) -> None:
        super().__init__(titular, cantidad)
        self.edad = edad
        self.bonificacion = bonificacion
    
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

    def retirar(self, retiro):
        if self.esTitularValido() != True :
            return 'Titular no cumple con requisutos de cuenta joven'
        else:
            return super().retirar(retiro)

    # 4- El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
    
    def mostrar(self):
        if self.esTitularValido() != True :
            return f'{super().mostrar()}, Edad: {self.get_edad()}' # Sin mostrar bonificación al no ser cuenta joven
        else:
            return f'{super().mostrar()}, Edad: {self.get_edad()}, “Cuenta Joven” = Bonificación: {self.get_bonificacion()}%'

# Cuentas de prueba
usuario_03 = Cuentajoven('Lucía', 23, 450, 10)
usuario_04 = Cuentajoven('Juanjo', 16, 2000, 5)

print('-------------------------esTitularValido------------------------------------------------')
print(usuario_03.esTitularValido())
print(usuario_04.esTitularValido())
print('------------------------Retirada_titutlar_valido-------------------------------')
print(f'Cantidad antes: {usuario_03.get_cantidad()}')
print('(None = True, False = texto error), Reslutado: ', usuario_03.retirar(20))
print(f'Cantidad Después: {usuario_03.get_cantidad()}')
print('--------------Titular_no_valido--------------------')
print(f'Cantidad antes: {usuario_04.get_cantidad()}')
print('(None = True, False = texto error), Reslutado: ', usuario_04.retirar(20))
print(f'Cantidad Después: {usuario_04.get_cantidad()}')
print('-------------------------Mostrar-----------------------------------------------')
print(usuario_03.mostrar())
print(usuario_04.mostrar())
