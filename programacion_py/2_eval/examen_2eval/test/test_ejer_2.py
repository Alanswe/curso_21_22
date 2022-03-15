
import unittest
import ejer_2,ejer_1

class Test_ejercicio_2(unittest.TestCase):

    def test_exixtencia(self):
        c = ejer_2.Cuenta('Benito',11111111111111111111)
        self.assertIsNotNone(c, None)

    def test_saldo_inicial(self):
        c = ejer_2.Cuenta('Benito',11111111111111111111)
        saldo = c.get_saldo()
        self.assertEqual(saldo, 0)

    def test_numero_cuenta(self):
        c = ejer_2.Cuenta('Benito',11111111111111111111)
        numero = c.numero
        self.assertEqual(numero, 11111111111111111111)

    def test_sin_numero_cuenta(self):
        with self.assertRaises(TypeError):
            ejer_2.Cuenta('Benito')

    def test_numero_cuenta_no_valido(self):
        with self.assertRaises(Exception):
            ejer_2.Cuenta('Benito',11111)

    def test_existencia_titulares_2(self):
        c = ejer_2.Cuenta('Benito',11111111111111111111)
        titu = c.get_titulares()
        self.assertEqual(titu,[])

    def test_titulares(self):
        c = ejer_2.Cuenta('Benito',11111111111111111111)
        p1 = ejer_1.Persona('55266893J','Benito','Camelo','Rápido')
        p2 = ejer_1.Persona('45266453Y','Pepe','Rodrigez')
        p3 = ejer_1.Persona('69266893F','Menganito','Segovia','Fernandez')
        c.set_titulares([p1,p2,p3])
        titu = c.get_titulares()
        self.assertEqual(titu,['Benito Camelo Rápido', 'Pepe Rodrigez ', 'Menganito Segovia Fernandez'])

    def test_ingresar(self):
        c = ejer_2.Cuenta('Benito',11111111111111111111)
        c.ingresar(100)
        saldo_new = c.get_saldo()
        self.assertEqual(saldo_new, 100)

    def test_ingresar_negativo(self):
        c = ejer_2.Cuenta('Benito',11111111111111111111)
        with self.assertRaises(Exception):
            c.ingresar(-100)

    def test_retirar(self):
        c = ejer_2.Cuenta('Benito',11111111111111111111)
        c.ingresar(100)
        c.retirar(50)
        saldo_new = c.get_saldo()
        self.assertEqual(saldo_new, 50)    

    def test_retirar_negativo(self):
        c = ejer_2.Cuenta('Benito',11111111111111111111)
        # saldo = 0
        with self.assertRaises(Exception):
            c.retirar(-100)

    def test_retirar_mayor_saldo(self):
        c = ejer_2.Cuenta('Benito',11111111111111111111)
        c.ingresar(100)
        # saldo = 100
        with self.assertRaises(Exception):
            c.retirar(200)
    
    def test_str(self):
        c = ejer_2.Cuenta('Benito',11111111111111111111)
        string = c.__str__()
        self.assertEqual(string, 'Titular: Benito, Número de cuenta: 11111111111111111111, Saldo: 0, Interés: 0')
