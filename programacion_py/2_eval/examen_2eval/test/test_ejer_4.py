import unittest
import ejer_4

class Test_ejercicio_4(unittest.TestCase):

    def test_existencia(self):
        e = ejer_4.Estudiante('Benito',100)
        self.assertIsNotNone(e, None)

    def test_str(self):
        e = ejer_4.Estudiante('Benito',100)
        string = e.__str__()
        self.assertEqual(string, 'Nombre: Benito, Nota: 100')

    def test_aprobado(self):
        e = ejer_4.Estudiante('Antonio',52)
        nota_final = e.es_aprobado()
        self.assertEqual(nota_final, 'Aprobado')

    def test_suspenso(self):
        e = ejer_4.Estudiante('Antonio',49)
        nota_final = e.es_aprobado()
        self.assertEqual(nota_final, 'Suspenso')

    def test_suspenso_con_requisito(self):
        e = ejer_4.Estudiante('Antonio',60)
        e.min_aprobado = 70
        nota_final = e.es_aprobado()
        self.assertEqual(nota_final, 'Suspenso')
