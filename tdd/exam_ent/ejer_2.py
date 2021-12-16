class Raton():
    
    # vairavles privadasd
    __posicion_x = 0
    __posicion_y = 0
    boton_izquierdo = False
    boton_derecho = False

    def __init__(self,__posicion_x,__posicion_y) -> None:
        self.__posicion_x = __posicion_x
        self.__posicion_y = __posicion_y

    # Getters
    def get_posicion_x(self):
        return self.__posicion_x

    def get_posicion_y(self):
        return self.__posicion_y
    
    # Setters
    def set_posicion_x(self, x):
        self.__posicion_x = x

    def set_posicion_y(self, y):
        self.__posicion_y = y

    # Metodos
    def click(self):
        self.boton_izquierdo = True
        self.boton_izquierdo = False

    def doble_click(self):
        self.boton_izquierdo = True
        self.boton_izquierdo = False
        self.boton_izquierdo = True
        self.boton_izquierdo = False

    def mover(self, x, y):
        self.boton_izquierdo = True
        self.set_posicion_x(x)
        self.set_posicion_y(y)
        self.boton_izquierdo = False

# Raton de prueba   
raton_1 = Raton(0,0)

# get y set
raton_1.set_posicion_x(4)
print(raton_1.get_posicion_x())

# clik




    
