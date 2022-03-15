
import unittest
import ejer_1

class Test_ejercicio_1(unittest.TestCase):

    def test_exixtencia(self):
        p = ejer_1.Persona('55266893J','Benito','Camelo','Rápido')
        self.assertIsNotNone(p, None)

    def test_str(self):
        p = ejer_1.Persona('55266893J','Benito','Camelo','Rápido')
        string = p.__str__()
        self.assertEqual(string, 'Nombre: Benito, Apellidos : Camelo Rápido, DNI: 55266893J')
