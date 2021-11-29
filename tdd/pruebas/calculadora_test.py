import unittest
import calculadora

class CalculadoraTest(unittest.TestCase):
    def test_caracteres_no_numericos_devuelve_error(self):
        respuesta = calculadora.sumar('a,b')
        self.assertEqual(respuesta,"Error: Carácter no numérico")

    def test_cadena_vacia_devuelve_cero(self):
        respuesta = calculadora.sumar('')
        self.assertEqual(respuesta,0)


    def test_un_numero_devuelve_el_numero(self):
        respuesta = calculadora.sumar('1')
        self.assertEqual(respuesta,1)


    def test_un_caracter_devuelve_el_numero(self):
            respuesta = calculadora.sumar('a')
            self.assertEqual(respuesta,"Error: Carácter no numérico")


    def test_dos_numeros_devuelve_suma(self):
            respuesta = calculadora.sumar('2,3')
            self.assertEqual(respuesta,5)


    def test_numeros_ilimitados_devuelve_suma(self):
            respuesta = calculadora.sumar('1,2,3,4')
            self.assertEqual(respuesta,10)


    def test_numeros_separados_por_n(self):
            respuesta = calculadora.sumar('1n2n4n5,3')
            self.assertEqual(respuesta,15)

    def test_barra_barra_punto_coma_devuelve_suma(self):
            respuesta = calculadora.sumar("//;\n1;2")
            self.assertEqual(respuesta,3)

    def test_valores_negativos_producen_error(self):
            respuesta = calculadora.sumar("3,-6,15,-18,46,33")
            self.assertEqual(respuesta,'Error: No admite números negativos')
