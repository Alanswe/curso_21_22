import unittest
import oop_01_01

class Persona(unittest.TestCase):
    def error_valor_nombre(self):
        respuesta = oop_01_01.usuario_1.set_nombre(544)
        self.assertEqual(respuesta,"Error: El valor introducido es incorrecto")

    def error_valor_edad(self):
        respuesta = oop_01_01.usuario_1.set_edad('Hola')
        self.assertEqual(respuesta,'Error: El valor no es un entero')

if __name__ == '__main__':
    unittest.main()
