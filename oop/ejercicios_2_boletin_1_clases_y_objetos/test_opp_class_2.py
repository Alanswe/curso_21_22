import unittest
from opp_class_2 import Coche

class Test_coches(unittest.TestCase):
    def test_getters(self):
        ejemplo = Coche('Toyota','Mirai',5,'0007ASS')
        self.assertEqual(ejemplo.marca, 'Toyota')
        self.assertEqual(ejemplo.modelo, 'Mirai')
        self.assertEqual(ejemplo.n_puertas, 5)
        self.assertEqual(ejemplo.matricula, '0007ASS')

    def test_setters(self):
        ejemplo = Coche('Dacia','StepWay',5,'86564lk')
        ejemplo.set_marca = 'Koenigsegg'
        ejemplo.set_modelo = 'Regera'
        ejemplo.set_n_puertas = 3
        ejemplo.set_martricula = '77800wr'
        self.assertEqual(ejemplo.marca, 'Koenigsegg')
        self.assertEqual(ejemplo.modelo, 'Regera')
        self.assertEqual(ejemplo.n_puertas, 3)
        self.assertEqual(ejemplo.matricula, '77800wr')