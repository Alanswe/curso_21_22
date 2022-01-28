import unittest
import suma_dados_funcional

class Tests_suma_dados_funcional_exite(unittest.TestCase):
    
    def test_inicial(self):
        self.assertEqual(suma_dados_funcional.juego(),None)