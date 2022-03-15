
import unittest
import ejer_3,ejer_2

class Test_ejercicio_3(unittest.TestCase):

    def test_existencia(self):
        cj = ejer_3.Cuentajoven('Benito',11111111111111111111,19)
        self.assertIsNotNone(cj, None)

    def test_edad_valida(self):
        cj = ejer_3.Cuentajoven('Benito',11111111111111111111,18)
        validacion = cj.esTitularValido()
        self.assertEqual(validacion, True)

    def test_edad_no_valida(self):
        cj = ejer_3.Cuentajoven('Benito',11111111111111111111,19)
        validacion = cj.esTitularValido()
        self.assertEqual(validacion, False)

    def test_saldo_mayor_a_5000(self):
        cj = ejer_3.Cuentajoven('Benito',11111111111111111111,18,6000)
        cj.set_interes()
        interes = cj.interes
        self.assertEqual(interes, 5)

    def test_saldo_menor_a_5000(self):
        cj = ejer_3.Cuentajoven('Benito',11111111111111111111,18,4000)
        cj.set_interes()
        interes = cj.interes
        self.assertEqual(interes, 1)

    def test_oferta_interes_en_cuenta_mayor_de_edad(self):
        cj = ejer_3.Cuentajoven('Benito',11111111111111111111,19,6000)
        with self.assertRaises(Exception):
            cj.set_interes()

    def test_ingreso_mayor_a_1000(self):
        cj = ejer_3.Cuentajoven('Benito',11111111111111111111,18)
        cj.ingresar(1000)
        saldo = cj.get_saldo()
        self.assertEqual(saldo, 1010)

    def test_ingreso_menor_a_1000(self):
        cj = ejer_3.Cuentajoven('Benito',11111111111111111111,18)
        cj.ingresar(100)
        saldo = cj.get_saldo()
        self.assertEqual(saldo, 100)

    def test_ingreso_mayor_a_1000_cuenta_no_joven(self):
        cj = ejer_3.Cuentajoven('Benito',11111111111111111111,19)
        with self.assertRaises(Exception):
            cj.ingresar(200)

    def test_si_se_permitre_retirar_menos_de_mitad_saldo(self):
        cj = ejer_3.Cuentajoven('Benito',11111111111111111111,18)
        cj.ingresar(500)
        cj.retirar(20) # 250 seria el máximo
        saldo = cj.get_saldo()
        self.assertEqual(saldo, 480)

    def test_no_se_permitre_retirar_mas_de_mitad_saldo(self):
        cj = ejer_3.Cuentajoven('Benito',11111111111111111111,18)
        cj.ingresar(500)
        with self.assertRaises(Exception):
            cj.retirar(260) # 250 seria el máximo
