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
		self.canciones = ['Dont go yet','Tacones rojos','Abcdefu','vacío','La fama']
		self.contador = self.contador_def() #la siguiente posición libre del array canciones.

	def contador_def(self):# solo esta cdontando el primer elemento en ¡vez de recorrewr la cadena entera
		for x in self.canciones:
			num = 0
			if x == 'vacío':
				num = self.canciones.index('vacío')
			return num

	def prueba(self):
		return self.canciones.index('vacío')
				
	def numeroCanciones(self):
		vacios = 0
		for x in self.canciones:
			if x == 'vacío':
				vacios += 1
			else:
				pass
		return len(self.canciones) - vacios

	def dameCancion(self,int):
		return self.canciones[int-1]

	def grabaCancion(self,int,Cancion):
		self.canciones[int-1] = Cancion

	def agrega(self,cancion):
		self.canciones.append(cancion)

	def elimina(self,int):
		self.canciones[int-1] = 'vacío'

            
ejemplo = CD()
print(ejemplo.contador_def())


   

"""
cuando decia que 'la siguiente posición libre del array canciones'  se refiera a cualquier psocion, es decir
elimina pos 2 = ['Dont go yet',' ','Abcdefu','Dont be shy','La fama'] y es esa posición seria la 
siguiente vacia.
agrega cambia el contendio de ese por el nuevo (anque este vacio)(puede que no haga falta)
para el elemina deberia cambiar el contenidpo de la indicada por ' ' (cancion en blanco)
"""
