from num_18_metodo_estatico import Calificaciones
import unittest as ut

class TestCalificaciones(ut.TestCase):
    def test_existencia(self):
        cal = Calificaciones()
        self.assertNotEqual(cal, None)

    def test_constructor_vacio_propiedades_vacias(self):
        cal = Calificaciones()
        self.assertEqual(cal.nombre, '')
        self.assertEqual(cal.notas, [])

    def test_constructor_recibe_valores_establece_props(self):
        cal = Calificaciones(['Raul',9.2,5,4.5,7,9.1])
        self.assertEqual(cal.nombre, 'Raul')
        self.assertEqual(cal.notas, [9.2,5,4.5,7,9.1])

    def test_metodo_str_devuelve_alumno_calificacion(self):
        cal = Calificaciones(['Raul',9.2,5,4.5,7,9.1])
        cadena = cal.__str__()
        self.assertEqual(cadena,'Alumno: Raul tiene la calificación BIEN')

    def test_calcula_calificacion_vacio_devuelve_None(self):
        cal = Calificaciones()
        self.assertEqual(cal.calcula_calificacion(),None)
        
    def test_calcula_calificacion_no_vacio_devuelve_calificacion(self):
        cal = Calificaciones(['Raul',9.2,5,4.5,7,9.1])
        self.assertEqual(cal.calcula_calificacion(),'BIEN')
        self.assertEqual(cal.calificacion,'BIEN')

    def test_introducir_alumno_nulo(self):
        cal = Calificaciones()
        cal.set_alumno_notas(['Fernando',6,5,6,7,7])
        self.assertEqual(cal.get_alumno_notas(), ('Fernando', [6, 5, 6, 7, 7])) #('Fernando', [6, 5, 6, 7, 7])
        self.assertEqual(cal.nombre, 'Fernando')
        self.assertEqual(cal.notas, [6, 5, 6, 7, 7])
        self.assertEqual(cal.calcula_calificacion(), 'BIEN')

    def test_valida_nota(self):
        cal = Calificaciones()
        self.assertEqual(cal.valida_notas([6, 5, 6, 7, 7]),True)

    def test_valida_nota_incorrecta(self):
        cal = Calificaciones()
        self.assertEqual(cal.valida_notas([6, 5, 6, 33, 7]),False)

    def test_valida_nota_incorrecta_str(self):
        cal = Calificaciones()
        self.assertEqual(cal.valida_notas([6, 5, 6, 'Hola', 7]),False)