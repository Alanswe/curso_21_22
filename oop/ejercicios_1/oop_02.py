#                         Ejercicio 2 de OOP Alan Sweere

# 1 - Crea una clase llamada **Cuenta** que tendrá los siguientes atributos: 
# 1-1- titular (que es una persona) y cantidad (puede tener decimales). 
#   El titular será obligatorio y la cantidad es opcional. 

# Construye los siguientes métodos para la clase:

# 2 Un constructor, donde los datos pueden estar vacíos.
# 3 Los setters y getters para cada uno de los atributos. 
# El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
# 4 mostrar(): Muestra los datos de la cuenta.
# 5 ingresar(cantidad): se ingresa una cantidad a la cuenta, 
#   si la cantidad introducida es negativa, no se hará nada.
# 6 retirar(cantidad): se retira una cantidad a la cuenta. 
# La cuenta puede estar en números rojos.


# 1 - Crea una clase llamada **Cuenta** que tendrá los siguientes atributos: 
class Cuenta():

    # 1-1- titular (que es una persona) y cantidad (puede tener decimales). 
    titular = None
    cantidad = 0

    # Construye los siguientes métodos para la clase:
    # 2 Un constructor, donde los datos pueden estar vacíos.
    #   El titular será obligatorio y la cantidad es opcional. 

    def __init__(self, titular, cantidad=0) -> None:
        self.titular = titular
        self.cantidad = cantidad

    # 3 Los setters y getters para cada uno de los atributos. 

    # Los getters

    def get_titular(self):
        return self.titular

    def get_cantidad(self):
        return self.cantidad

    # Los setters

    def set_titular(self, a):
        self.titular = a

    # El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
    
    # 5 ingresar(cantidad): se ingresa una cantidad a la cuenta, 
    # si la cantidad introducida es negativa, no se hará nada.

    def ingresar(self, ingreso):
        if ingreso <0:
            print('Error: Valor introducido negativo')
            pass
        else:
            self.cantidad = self.cantidad + ingreso

    # 6 retirar(cantidad): se retira una cantidad a la cuenta. 
    # si la cantidad introducida es negativa, no se hará nada.
    # La cuenta puede estar en números rojos.  

    def retirar(self, retiro):
        if retiro <0:
            print('Error: Valor introducido negativo')
            pass
        else:
            self.cantidad = self.cantidad - retiro
    
    # 4 mostrar(): Muestra los datos de la cuenta.

    def mostrar(self):
        print('Titular: ', self.titular, ', Cantidad: ', self.cantidad)
        #return ('Titular: ', self.titular, ', Cantidad: ', self.cantidad)

# Cuentas de prueba

cuenta_01 = Cuenta('Pepe', 500)

cuenta_02 = Cuenta('Manolo')

# Pruebas-----------------------
print('Prueba opcional:', cuenta_02.mostrar())
print('Llamar a get: ', cuenta_01.get_titular())
print('----------Prueba Set--------------------')
print('Antes de llamar al set: ', cuenta_01.titular)
cuenta_01.set_titular('Jose')
print('Después: ', cuenta_01.titular)
print('--------------ingreso--------------------------')
cuenta_01.ingresar(-100)
print('Comprobación: ', cuenta_01.cantidad)
print('----------------retiro------------------------')
cuenta_01.retirar(100)
print('Después de retirar 100: ', cuenta_01.cantidad)
cuenta_01.retirar(-100)
print('Comprobación: ', cuenta_01.cantidad)
print('-------------------numero rojos---------------------')
cuenta_01.retirar(600)
print('Después de retirar 600 en rojo: ', cuenta_01.cantidad)
print('-------------------mostrar---------------------')
cuenta_01.mostrar()
#print(cuenta_01.mostrar())
