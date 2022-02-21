import unittest
import ejer_1

class test_1(unittest.TestCase):
    # A - si no se pasan argumentos devuelve 0
    def test_1(self):
        respuesta = ejer_1.sumar('')
        self.assertEqual(respuesta,0)

    # B - probar que puede sumar eneros o floats
    def test_2(self):
        respuesta = ejer_1.sumar('1,3')
        self.assertEqual(respuesta,"Error: Carácter no numérico")
    
    # C - si se pasa cadenas devuelve 0
    def test_3(self):
        respuesta = ejer_1.sumar('a,c')
        self.assertEqual(respuesta,0)

    # D - datos complejos devuelve 0
    def test_4(self):
        respuesta = ejer_1.sumar('6j')
        self.assertEqual(respuesta,0)
    
    # E - caracteres no nomericos devuelve cero
    def test_5(self):
        respuesta = ejer_1.sumar('c')
        self.assertEqual(respuesta,0)
    