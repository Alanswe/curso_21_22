import unittest
from oop_01_punto import Punto,Rectangulo

class TestPunto(unittest.TestCase):
    def test_contructor_0_0_devuelve_0_0(self):
        p = Punto(0,0)
        self.assertEqual(p.x,0)
        self.assertEqual(p.y,0)

    def test_completos_dan_error(self):
        p = Punto((1+2j),(2+2j))
        self.assertEqual(p,1)        

class TestRectangulo(unittest.TestCase):
    def test_es_rectangulo(self):
        p1 = Punto(4,2)
        p2 = Punto(3,-1)
        r = Rectangulo()
        self.assertEqual(r.v1,Punto(4,2))
        self.assertEqual(r.v2,Punto(3,-1))
        self.assertEqual(r.v3,Punto(4,-1))
        self.assertEqual(r.v4,Punto(3,2))