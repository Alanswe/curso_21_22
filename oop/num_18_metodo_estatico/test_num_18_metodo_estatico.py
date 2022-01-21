import unittest
from num_18_metodo_estatico import Calificaciones

class TestCalificaciones(unittest.TestCase):
    def test_existencia(self):
        cal = Calificaciones()
        self.assertNotEqual(cal, None)

    def test_constructor_recibe_valores_vacios(self):
        cal = Calificaciones([])
        self.assertEqual(cal.alumno, [])
    
    def test_constructor_recibe_valores_establece_props(self):
        cal = Calificaciones(['Raul',9.2,5,4.5,7,9.1])
        self.assertEqual(cal.alumno, ['Raul',9.2,5,4.5,7,9.1])

    # def test_calificacion_vacia_devuelve_None(self) :
    #     cal = Calificaciones()
    #     self.assertEqual(cal.calificar(), None)

    def test_calificacion_devuelve_nota(self) :
        cal = Calificaciones(['Raul',9.2,5,4.5,7,9.1])
        self.assertEqual(cal.calificar(), 'APROBADO')

    def test_str(self):
        cal = Calificaciones(['Raul',9.2,5,4.5,7,9.1])
        cadena = cal.__str__()
        self.assertEqual(cadena, 'Alumno: Raul Calificación: APROBADO')