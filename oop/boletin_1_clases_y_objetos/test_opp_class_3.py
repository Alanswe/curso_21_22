import unittest
from oop_class_3 import Tiempo

class Test_tiempo(unittest.TestCase):
    def test_getters(self):
        ejemplo = Tiempo(1,25,45)
        self.assertEqual(ejemplo.hora, 1)

    def test_setters(self):
        ejemplo = Tiempo(1,25,45)
        ejemplo.set_hora = 2
        ejemplo.set_minuto = 35
        ejemplo.set_segundo = 55
        self.assertEqual(ejemplo.hora, 2)
        self.assertEqual(ejemplo.minuto, 35)
        self.assertEqual(ejemplo.segundo, 55)

    # las 3 llamadas
    def test_3_instancias(self):
        ejemplo = Tiempo(6,20,15)
        # Sólo la hora
        self.assertEqual(ejemplo.hora, 6)
        # Sólo la hora y minuto
        self.assertEqual(ejemplo.get_hora_minuto, (6, 20))
        # Los tres atributos ---------------------Para otro formato más pythonic--------------------------------
        self.assertEqual(ejemplo.get_all, '6:20:15') # (6, 20, 15)