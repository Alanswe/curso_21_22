import unittest
from ejer_2_1 import CD

class Test_para_cd(unittest.TestCase):

    def test_exixtemcia_cacion(self):
        ejemplo = CD()
        self.assertNotEqual(ejemplo,None)

    def test_init_canciones(self):
        cd = CD()
        self.assertEqual(cd.canciones,['Dont go yet', 'Tacones rojos', 'Abcdefu', 'Dont be shy', 'La fama'])

    def test_init_contador(self):
        cd = CD()
        self.assertEqual(cd.contador,0) # tiene que dar 0 si esta llena

    def test_init_contador_con_vacio(self):
        cd = CD()
        cd.elimina(2)
        self.assertEqual(cd.contador,2) # tiene que dar 0 si esta llena y el index del pimer vacio si no, pero el contador esta incompleto

    def test_cuenta_canciones(self):
        ejemplo = CD().numeroCanciones()
        self.assertEqual(ejemplo,5)

    def test_devuelve_contador_con_vacio(self):
        cd = CD()
        cd.elimina(2)
        ejemplo = cd.numeroCanciones()
        self.assertEqual(ejemplo,4)

    def test_devuelve_cancion(self):
        ejemplo = CD().dameCancion(2)
        self.assertEqual(ejemplo,'Tacones rojos')

    def test_devuelve_cancion_con_vacio(self):
        cd = CD()
        cd.elimina(2)
        ejemplo = cd.dameCancion(2)
        self.assertEqual(ejemplo,'vacío')

    def test_reemplaza_cancion(self):
        disco = CD()
        disco.grabaCancion(3,'Easy on me')
        comprobar = disco.canciones
        self.assertEqual(comprobar ,['Dont go yet','Tacones rojos','Easy on me',
                        'Dont be shy','La fama'])

    def test_reemplaza_cancion_con_vacio(self):
        disco = CD()
        disco.elimina(3)
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
        self.assertEqual(comprobar ,['Dont go yet','vacío','Abcdefu',
                            'Dont be shy','La fama'])        
