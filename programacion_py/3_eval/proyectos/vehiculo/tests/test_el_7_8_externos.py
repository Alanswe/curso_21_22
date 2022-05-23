import unittest
import el_7_8_externos, vehiculo

class Test_ejercicio_7(unittest.TestCase):

    def test_tipo_vehiculo_generico(self):
        v_b = vehiculo.Vehiculo()
        tipo = el_7_8_externos.clase(v_b)
        self.assertEqual(tipo, 'Vehiculo')

    def test_padre_de_vehiculo_generico(self):
        v_b = vehiculo.Vehiculo()
        tipo = el_7_8_externos.clase_padre(v_b)
        self.assertEqual(tipo, 'object') # si llamas al padre y es el padre

    def test_padre_del_padre_vehiculo_generico(self):
        v_b = vehiculo.Vehiculo()
        tipo = el_7_8_externos.clase_padre_del_padre(v_b)
        self.assertEqual(tipo, None) # ya que no tiene abuelo

    def test_tipo_vehiculo_buss(self):
        v_b = vehiculo.Buss()
        tipo = el_7_8_externos.clase(v_b)
        self.assertEqual(tipo, 'Buss')

    def test_tipo_vehiculo_buss_escolar(self):
        v_b = vehiculo.Buss_escolar()
        tipo = el_7_8_externos.clase(v_b)
        self.assertEqual(tipo, 'Buss_escolar')

    def test_padre_vehiculo_buss_escolar(self):
        v_b = vehiculo.Buss_escolar()
        tipo = el_7_8_externos.clase_padre(v_b)
        self.assertEqual(tipo, 'Buss')

    def test_padre_del_padre_vehiculo_buss_escolar(self):
        v_b = vehiculo.Buss_escolar()
        tipo = el_7_8_externos.clase_padre_del_padre(v_b)
        self.assertEqual(tipo, 'Vehiculo')

    def test_padre_del_padre_vehiculo_buss(self):
        v_b = vehiculo.Buss()
        tipo = el_7_8_externos.clase_padre_del_padre(v_b)
        self.assertEqual(tipo, 'object') # ya que el padre de Buss es el final

    def test_objeto_buss_escolar(self):
        buss_escola = vehiculo.Buss('Dacia',160,250000)
        clase = el_7_8_externos.clase(buss_escola)
        padre = el_7_8_externos.clase_padre(buss_escola)
        abuelo = el_7_8_externos.clase_padre_del_padre(buss_escola)
        self.assertEqual(clase, 'Buss')
        self.assertEqual(padre, 'Vehiculo')
        self.assertEqual(abuelo, 'object')
