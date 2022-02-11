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
        # cuenta las canciones que no esten vacias
		return self._contador

	def dameCancion(self,int):
		return self.canciones[int-1]

	def grabaCancion(self,int,Cancion):
		self.canciones[int-1] = Cancion

	def agrega(self,cancion):
		self.canciones.append(cancion)

	def elimina(self,int):
        # para el elemina deberia cambiar el contenidpo de la indicada por ' ' (cancion en blanco)
		self.canciones[int-1] = 'vacío'
    
    def contador_def(self): # no pilla el def
        vacios = 0
        if self.canciones.index('vacío'):
            vacios += 1
        return self._contador - vacios

            
    

"""
cuando decia que 'la siguiente posición libre del array canciones'  se refiera a cualquier psocion, es decir
elimina pos 2 = ['Dont go yet',' ','Abcdefu','Dont be shy','La fama'] y es esa posición seria la 
siguiente vacia.
agrega cambia el contendio de ese por el nuevo (anque este vacio)(puede que no haga falta)
para el elemina deberia cambiar el contenidpo de la indicada por ' ' (cancion en blanco)
"""
