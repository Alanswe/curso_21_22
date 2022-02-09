"""							Ejercicio 2 de Alan Sweere
Consiste en una clase cd en la que están los objetos 'canción', 
a la que añadimos,eliminamos y otras funciones de CD

El contador dice la siguiente posicion libre del array de canciones,
siendo siempre una más que la lista de canciones actual.

list_40 = ['Dont go yet','Tacones rojos','Abcdefu','Dont be shy','La fama']
ejemplos para test = 'Easy on me','Música ligera'
"""
class CD():

	def __init__(self) -> None:
		self.canciones = ['Dont go yet','Tacones rojos','Abcdefu','Dont be shy','La fama']
		self._contador = len(self.canciones)+1 #la siguiente posición libre del array canciones.

	def numeroCanciones(self):
		return self._contador

	def dameCancion(self,int):
		return self.canciones[int-1]

	def grabaCancion(self,int,Cancion):
		self.canciones[int-1] = Cancion

	def agrega(self,cancion):
		self.canciones.append(cancion)

	def elimina(self,int):
		self.canciones.remove(self.canciones[int-1])
