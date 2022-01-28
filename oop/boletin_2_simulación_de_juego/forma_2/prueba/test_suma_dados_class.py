import unittest
from suma_dados_class import Juego

class Test_juego(unittest.TestCase):
    def test_inicial(self):
        ejemplo = Juego()
        self.assertEqual(ejemplo.play(), type(list)) #lista de elementos