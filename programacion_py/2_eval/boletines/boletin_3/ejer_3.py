"""								Ejercicio 3 de Alan Sweere
Cosiste en una clase libros en la que se maneja la lista de libros predefinida
Queda por terminar la función busca_libro para que:
		También incluirá un método para buscar un libro a partir de una parte de su título 
		(sin distinguir entre mayúsculas y minúsculas); 
		el método devolverá la posición en la que se encuentra el libro
"""
class Libros():
	def __init__(self) -> None:
		self.libros = ['El Hobbit', 'Fundación', 'Harry Potter', 'La Biblia', 'Yo robot']

	def get_num_libros(self):
		return len(self.libros)

	def damelibro(self,int):
		return self.libros[int-1]

	def elimina(self,int):
		self.libros.remove(self.libros[int-1])

	def inserta_libro(self,new_libro):
		self.libros.append(new_libro)
		self.libros.sort()

	def get_lista_total(self):
		return self.libros
	
	# Por terminar
	def busca_libro(self,titulo): # ¿a partir de una parte de su título?
		try:
			if self.libros.index(titulo)+1:
				return self.libros.index(titulo)+1			 
		except ValueError:
			return -1
