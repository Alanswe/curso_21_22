import unittest
from wc import Wc

class Test_para_wc(unittest.TestCase):
    # def setUp(self) -> None:
    #     return super().setUp()

    def test_existencia(self):
        wc = Wc('/home/alan/Documentos/GitHub/wc_command/','README.md')
        self.assertNotEqual(wc, None)

    # Validar archivo
    def test_validar_archivo(self):
        wc = Wc('/home/alan/Documentos/GitHub/wc_command/archivos/','prueba.txt')
        self.assertEqual(wc.valida_archivo(), True)

    def test_validar_archivo_nulo(self):
        wc = Wc('/home/alan/Documentos/GitHub/wc_command/archivos/','prueba_foto.png')
        self.assertEqual(wc.valida_archivo(), False)

    def test_validar_archivo_none(self):
        wc = Wc('/home/alan/Documentos/GitHub/wc_command/archivos/','Makefile')
        with self.assertRaises(Exception):
            wc.valida_archivo()

    # leer carchivo
    def test_leer_archivo_valido_lleno(self):
        wc = Wc('/home/alan/Documentos/GitHub/wc_command/archivos/','prueba.txt')
        prueba = wc.leer_archivo()
        self.assertEqual(prueba, 'hola\n')

    def test_leer_archivo_valido_vacio(self):
        wc = Wc('/home/alan/Documentos/GitHub/wc_command/archivos/','prueba_vacio.txt')
        with self.assertRaises(Exception):
            wc.leer_archivo()

    def test_leer_archivo_invalido(self):
        wc = Wc('/home/alan/Documentos/GitHub/wc_command/archivos/','Makefile')
        with self.assertRaises(Exception):
            wc.leer_archivo()

    # un def que lea un html y un md

    # leer lineas
    def test_cuenta_lineas(self):
        wc = Wc('/home/alan/Documentos/GitHub/wc_command/archivos/','prueba_sucia.txt')
        wc.leer_archivo()
        wc.limpiar_cadena()
        wc.contar_palabras()
        self.assertEqual(wc.num_palabras, 5)


    def test_limpiar_cadena(self):
        wc = Wc('/home/alan/Documentos/GitHub/wc_command/archivos/','prueba_sucia.txt')
        wc.leer_archivo()
        wc.limpiar_cadena()
        self.assertEqual(wc.contenido, 'hola esto son caractereshola dffffin')

    def test_frecuencias(self):
        wc = Wc('/home/alan/Documentos/GitHub/wc_command/archivos/','prueba_sucia.txt')
        wc.leer_archivo()
        wc.limpiar_cadena()
        wc.frecuencias()
        self.assertEqual(wc.num_frecuencias,50)
        