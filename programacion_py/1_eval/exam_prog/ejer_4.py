# Ejercicio 4 de Alan Sweere Segovia
"""
4.	Escriba una clase que admita como parámetros en su constructor las variables 'ancho' y 'alto'.
Esta clase debe crear una matriz de tamaño 'ancho' x 'alto' llena de ceros y debe tener un método que permita imprimirla por pantalla.

"""

from pprint import pprint

# Clase que admita ancho y alto en constructor
class ejer_4():
    ancho = 0
    alto = 0

    def __init__(self, ancho, alto) -> None:
        self.ancho = ancho
        self.alto = alto

    # metodo para imprimir ancho por alto de la anterior
    def en_pantalla(self):
        pprint(self.an_x_al()) 
    
    def an_x_al(self): # matriz de tamaño ancho por alto llena de ceros
        filas = self.alto
        columnas = self.ancho
        matriz = []
        for i in range(filas):     
            fila = []
            for j in range(columnas):
                fila.append(0)
            matriz.append(fila)
        return matriz

# matriz de preuba ----------------------------
matriz_1 = ejer_4(10,10)
matriz_2 = ejer_4(20,20)
matriz_3 = ejer_4(5,5)

# Pruebas -------------------------------------
matriz_1.en_pantalla()
print('-----------------------------------------------------')
matriz_2.en_pantalla()
print('-----------------------------------------------------')
matriz_3.en_pantalla()
