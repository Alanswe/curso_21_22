import unittest
from maquina_bolas import Maquina,MONEDA,BOLA

class TestMaquina(unittest.TestCase):
    """ Pruebas """
    def test_creacion_maquina(self):
        """ Prueba de existencia"""
        maquina = Maquina()
        self.assertIsNotNone(maquina)

    def test_estado_inicial(self):
        m = Maquina()
        monedas = m.monedero
        bolas = m.deposito
        self.assertEqual(bolas, 100)
        self.assertEqual(monedas, 0)

    def test_moneda_1E_es_valida(self):
        """ Prueba de monda de un E"""  
        maquina = Maquina()
        resp = maquina.aceptar_moneda(MONEDA)
        self.assertEqual(resp, True) 

    def test_moneda_50cent_es_valida(self):
        """ Prueba de moneda de 50cts es incorrecta"""
        maquina = Maquina()
        resp = maquina.aceptar_moneda('Cent_50')
        self.assertEqual(resp, False) 

    def test_giro_manivela_correcto(self):
        """Si gira correctamente True """
        maquina = Maquina()
        giro = 360
        resp = maquina.girar_manivela(giro)
        self.assertEqual(resp,True) 

    def test_giro_manivela_incorrecto(self):
        """Si gira menos de 360º es incorrecto"""
        maquina = Maquina()
        giro = 30
        resp = maquina.girar_manivela(giro)
        self.assertEqual(resp,False) 

    def test_moneda_y_giro_correctos_suelta_bola(self):
        # Si las condiciones son correctas suelta una bola """
        maquina = Maquina()
        dep = maquina.deposito
        mon = maquina.monedero
        resp = maquina.soltar_bola()
        self.assertEqual(resp,BOLA)
        self.assertEqual(maquina.deposito, dep-1)
        self.assertEqual(maquina.monedero, mon+1)

    def test_leer_estado_0(self):
        ejemplo = Maquina().leer_estado_csv_0()
        self.assertEqual(ejemplo, ['100,0\n']) # ['100,0\n']

    def test_leer_estado_csv_1(self):
        ejemplo = Maquina().leer_estado_csv_1()
        self.assertEqual(ejemplo, '100,0\n') # 100,0

    def test_leer_estado_csv_2(self):
        ejemplo = Maquina().leer_estado_csv_2()
        self.assertEqual(ejemplo, [['100', '0']]) # [['100', '0']]

    def test_salvar_estado_csv(self):
        m = Maquina()
        m.soltar_bola()
        m.salvar_estado_csv_1()
        monedas = m.monedero
        bolas = m.deposito
        self.assertEqual(monedas, 1) # 0 de serie
        self.assertEqual(bolas, 99) # 100 de serie

    # def test_salvar_estado_csv_2(self):  # si se ejecuta cambia la disposición del csv
    #     m = Maquina()
    #     m.soltar_bola()
    #     m.salvar_estado_csv_2()
    #     monedas = m.monedero
    #     bolas = m.deposito
    #     self.assertEqual(monedas, 1) # 0 de serie
    #     self.assertEqual(bolas, 99) # 100 de serie
