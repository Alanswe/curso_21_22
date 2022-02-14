import unittest
from ejer_2 import CD

class Test_para_cd(unittest.TestCase):

    def test_exixtemcia_cacion(self):
        ejemplo = CD()
        self.assertNotEqual(ejemplo,None)

    def test_init_canciones(self):
        cd = CD()
        self.assertEqual(cd.canciones,['Dont go yet', 'Tacones rojos', 'Abcdefu', 'Dont be shy', 'La fama'])

    def test_init_contador(self):
        cd = CD()
        self.assertEqual(cd._contador,6)

    def test_devuelve_contador(self):
        ejemplo = CD().numeroCanciones
        self.assertEqual(ejemplo,6)

    def test_devuelve_cancion(self):
        ejemplo = CD().dameCancion(2)
        self.assertEqual(ejemplo,'Tacones rojos')

    def test_reemplaza_cancion(self):
        disco = CD()
        disco.grabaCancion(3,'Easy on me')
        comprobar = disco.canciones
        self.assertEqual(comprobar ,['Dont go yet','Tacones rojos','Easy on me',
                        'Dont be shy','La fama'])

    def test_agrega_cancion_alfinal(self):
        disco = CD()
        disco.agrega('Música ligera')
        comprobar = disco.canciones
        self.assertEqual(comprobar ,['Dont go yet','Tacones rojos','Abcdefu',
                            'Dont be shy','La fama','Música ligera'])

    def test_elemina_cancion(self):
        disco = CD()       
        disco.elimina(2)
        comprobar = disco.canciones
        self.assertEqual(comprobar ,['Dont go yet','Abcdefu',
                            'Dont be shy','La fama'])        
