""" MONO
1 - La clase csv tendría: Alumno, Boletin1,Boleton2,Boletin3... ejemplo: 'Pepe,5,7.5,6,7,8' como max 10 notas
2 - Convertir el csv en diccionario en valores nombre y boletines
    o una lista
3 - para cada alumno tasformar la recepcion de datos
"""
class NotasInvalidasError(Exception):
    pass

class Calificaciones():
    def __init__(self,alumno_notas=[]) -> None:

        if alumno_notas:
            self.__nombre = alumno_notas[0]
            self.__notas = alumno_notas[1:]
            self.__calificacion = self.calcula_calificacion()
        else:
            self.__nombre = ''
            self.__notas = []
            self.__calificacion = ''
    
    def __str__(self) -> str:
        return f'Alumno: {self.__nombre} tiene la calificación {self.__calificacion}'

    def calcula_calificacion(self):
        calificacion = ''

        if self.notas:
            nota_media = sum(self.notas)/len(self.notas)
            if nota_media < 5:
                calificacion = 'SUSPENSO'
            elif nota_media < 7:
                calificacion = 'BIEN'
            elif nota_media < 9:
                calificacion = 'NOTABLE'
            else:
                calificacion = 'SOBRESALIENTE'
            
        else:
            calificacion = None
        
        return calificacion

    def calificacion_desde_csv(Calificaciones,obj_csv):
        estudiante = dict(obj_csv) #{'nombre': 'Pepe', 'boletines': '5,7.5,6,7,8'}
        obj_estudiante = Calificaciones(estudiante['nombre'], estudiante['boletines'])
        return obj_estudiante
    
    @property
    def alumno(self):
        return self.__nombre

    @alumno.setter
    def alumno(self,nuevo_alumno):
        self.__nombre = nuevo_alumno
    
    @property
    def notas(self):
        return self.__notas

    @notas.setter
    def notas(self, nuevas_notas):
        try:
            if self.valida_notas(nuevas_notas):
                self.__notas = nuevas_notas
                self.__calificacion = self.calcula_calificacion()
        except NotasInvalidasError:
            pass        
    
    @property
    def calificacion(self):
        return self.__calificacion

    @staticmethod
    def valida_notas(lista_notas):
        valido = True
        if lista_notas == []:
            raise NotasInvalidasError('La lista de notas está vacía')

        for nota in lista_notas:
            if not type(nota) in (int,float) or not (0.0<= nota <= 10.0) :
                raise NotasInvalidasError('El tipo de dato o valores incorretos')
        
        return valido


x = Calificaciones.calificacion_desde_csv(Calificaciones,'Pepe,5,7.5,6,7,8')
print(x)


# cal = Calificaciones()
# print(cal.valida_notas([6, 5, 6, 33, 7]))
# print(cal.valida_notas([6, 5, 6, 7, 7]))





























class Estudiante():
    def __init__(self,nombre,apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self) -> str:
        return f'Estudiante: {self.nombre} {self.apellido}'

    @classmethod
    def estudiante_desde_csv(cls,obj_csv): # No necesita self al ser un método de clase
        estudiante = dict(obj_csv) #{'nombre': 'Paco', 'apellidos': 'Lopez Garcia'}
        obj_estudiante = cls(estudiante['nombre'], estudiante['apellidos'])
        return obj_estudiante


