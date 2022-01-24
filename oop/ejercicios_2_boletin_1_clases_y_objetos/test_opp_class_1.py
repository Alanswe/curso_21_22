import unittest
from oop_class_1 import Rectangulo

class Test_rectangulo(unittest.TestCase):
    
        def test_area(self):
                ejemplo = Rectangulo(10,15)
                self.assertEqual(ejemplo.calc_area(), 150)
                
        def test_perimetro(self):
                ejemplo = Rectangulo(10,15)
                self.assertEqual(ejemplo.calc_perimetro(), 50)