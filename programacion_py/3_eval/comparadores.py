from math import pi

class Circulo():
    """
    __eq__ : si uno es igual a otro es, da true
    __lt__ : si uno es menor que otro, da true
    __gt__ : si uno es mayor a otro, da true
    """
    def __init__(self,radio) -> None:
        if type(radio) in (int,float) and radio > 0:
                self.radio = radio
        else:
            raise Exception('El radio tiene que ser un número positivo \n...O simplemente un número ¡Zoquete!')

    def area(self):
        return pi * self.radio * self.radio

    def perimetro(self):
        return 2 * pi * self.radio

    def __eq__(self, __o: object) -> bool:
        return __o.radio == self.radio


# Pruebas (Solo para ejemplo)

obj = Circulo(4)

obj_2 = Circulo(3)

obj_3 = Circulo(4)
print(obj.__eq__(obj_2)) # tiene que dar false
print(obj.__eq__(obj_3)) # tiene que dar true
print(obj == obj_3) # da true
"""
Dice false si el objeto 2 es diferente al objeto 1
"""