import unittest
from vehiculo import Buss_escolar, Vehiculo,Buss

class Test_vehiculo(unittest.TestCase):

    def test_existencia(self):
        v = Vehiculo()
        self.assertIsNotNone(v)

    def test_existencia_atributos(self):
        v = Vehiculo('Dacia',160,250000)
        self.assertEqual(v.nombre,'Dacia')
        self.assertEqual(v.velocidad_max,160)
        self.assertEqual(v.kilometraje, 250000)

    def test_existencia_atributo_color(self):
        v = Vehiculo('Dacia',160,250000)
        color_v = v.color
        self.assertEqual(color_v,'Blanco')

    def test_str(self):
        v = Vehiculo('Dacia',160,250000)
        str_v = v.__str__()
        self.assertEqual(str_v,'Nombre: Dacia\nV-Max: 160\nKlm: 250000')
    
    def test_cal_tarifa_generica(self):
        v = Vehiculo('Dacia',160,250000)
        tarifa = v.cal_tarifa()
        self.assertEqual(tarifa, 100)

    def test_da_padre_siendo_padre(self):
        v = Vehiculo('Dacia',160,250000)
        padre = v.get_padre()
        self.assertEqual(padre, 'object') # al ser el objeto padre

class Test_bus(unittest.TestCase):

    def test_existencia(self):
        b = Buss()
        self.assertIsNotNone(b)

    def test_existencia_atributos(self):
        b = Buss('Dacia',160,250000)
        self.assertEqual(b.nombre,'Dacia')
        self.assertEqual(b.velocidad_max,160)
        self.assertEqual(b.kilometraje, 250000)

    def test_extsencia_atributo_capacidad(self):
        b = Buss('Dacia',160,250000)
        b.set_capacidad()
        capa_b = b.capacidad
        self.assertEqual(capa_b,50)

    def test_existencia_atributo_color(self):
        b = Buss('Dacia',160,250000)
        color_b = b.color
        self.assertEqual(color_b,'Blanco')

    def test_str(self):
        b = Buss('Dacia',160,250000)
        b.set_capacidad()
        str_b = b.__str__()
        self.assertEqual(str_b,'Nombre: Dacia\nV-Max: 160\nKlm: 250000Capacidad: 50\n color: Blanco')

    def test_cal_tarifa_bus(self):
        b = Buss('Dacia',160,250000)
        tarifa = b.cal_tarifa()
        self.assertEqual(tarifa, 5500)

    def test_da_padre(self):
        b = Buss('Dacia',160,250000)
        padre = b.get_padre()
        self.assertEqual(padre, 'Vehiculo')

class Test_para_buss_escolar(unittest.TestCase):
    
    def test_da_padre(self):
        b = Buss_escolar('Dacia',160,250000)
        padre = b.get_padre()
        self.assertEqual(padre, 'Buss')

    def test_da_padre_del_padre(self):
        b = Buss_escolar('Dacia',160,250000)
        abuelo = b.get_padre_del_padre()
        self.assertEqual(abuelo, 'Vehiculo')
