import unittest
from ejer_3 import Libros

class Test_libros(unittest.TestCase):

    def test_numero_libros(self):
        ejemplo = Libros().get_num_libros()
        self.assertEqual(ejemplo,5)

    def test_insertar_libro(self):
        libro = Libros()
        libro.inserta_libro('Reina Roja')
        ejemplo = libro.get_lista_total()
        self.assertEqual(ejemplo, ['El Hobbit', 'Fundación', 'Harry Potter', 'La Biblia', 'Reina Roja', 'Yo robot'])

    def test_elimina_libro(self):
        libro = Libros()
        libro.elimina(4)
        ejemplo = libro.get_lista_total()
        self.assertEqual(ejemplo, ['El Hobbit', 'Fundación', 'Harry Potter', 'Yo robot'])

    def test_dar_libro(self):
        ejemplo = Libros().damelibro(4)
        self.assertEqual(ejemplo, 'La Biblia')

    def test_dar_libro_0(self):
        ejemplo = Libros().damelibro(1)
        self.assertEqual(ejemplo, 'El Hobbit')

    def test_busca_libro_titulo_entero(self):
        ejemplo = Libros().busca_libro('Fundación')
        self.assertEqual(ejemplo, 2)

    def test_busca_libro_titulo_entero_posicion_0(self):
        ejemplo = Libros().busca_libro('El Hobbit')
        self.assertEqual(ejemplo, 1)
        
    def test_busca_libro_titulo_parcial(self):
        ejemplo = Libros().busca_libro('Harry') # ¿tiene que buscarse letra a letra?
        self.assertEqual(ejemplo, 3) # ValueError: 'Harry' is not in list, es decir -1

    def test_busca_libro_no_existe(self):
        ejemplo = Libros().busca_libro('Reina Roja')
        self.assertEqual(ejemplo, -1)
