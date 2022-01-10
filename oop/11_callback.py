# los callback notifican que la funcio termino lo que sea que hacia y avisa
class Batidora():
    
    __motor = 0

    subcriptores = []
    # guarda los callback

    def encender(self):
        self.__motor = 100
        print('Encendiendo...')

    def apagar(self):
        self.__motor = 0
        print('Apagando...')

    def acelerar(self):
        self.__motor *= 1.1
        print('Acelerando...')
        for s in self.subcriptores:
            s(self.__motor)
    
    # def acelerar(self,callback):
    #     self.__motor *= 1.1
    #     print('Acelerando...')
    #     callback(self.__motor)
    # Estamos pasando la función como parametro

    def get_estado(self):
        return self.__motor

#######################################################3

def muestre_velocidad(vel):
    print(f'La velocidad de la batidora es {vel}')

def otra_funcion(vel):
    if vel > 120:
        print(f'Velocidad excesiva {vel}')
    
b = Batidora()
b.subcriptores.append(muestre_velocidad)
b.subcriptores.append(otra_funcion)
#-------------
b.encender()
print(b.get_estado())
b.acelerar()

#b.acelerar(muestre_velocidad)
# Queremos que el callback sea la función muestre velocidad
#b.acelerar(muestre_velocidad)

b.acelerar()
b.apagar()
print(b.get_estado())
