"""
Crear una clase Calificaciones.
Tendrá un método init que admitirá como entrada una lista de forma ['Raul',9.2,5,4.5,7,9.1]
Tendra un método 'calificar' que nos devolverá ['Raul', 'Notable']

"""

class Calificaciones():
    def __init__(self,alumno_notas=[]) -> None:

        if alumno_notas:
            self.nombre = alumno_notas[0]
            self.notas = alumno_notas[1:]
            self.calificacion = self.calcula_calificacion()
        else:
            self.nombre = ''
            self.notas = []
            self.calificacion = ''
    
    def __str__(self) -> str:
        return f'Alumno: {self.nombre} tiene la calificación {self.calificacion}'

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

    def set_alumno_notas(self,new_alumno):
        if new_alumno:
            self.nombre = new_alumno[0]
            self.notas = new_alumno[1:]
        else:
            new_alumno = None

    def get_alumno_notas(self):
        return self.nombre,self.notas

    @staticmethod
    def valida_notas(lista_notas):
        validacion = True
        for x in lista_notas:
            if x != int or float:
                validacion = False
            elif 0 <= x <= 10:
                validacion = True
            else:
                validacion = True
        return validacion

cal = Calificaciones()
# cal.set_alumno_notas(['Fernando',6,5,6,7,7])
# print(cal.get_alumno_notas())
# print(cal.calcula_calificacion())
print(cal.valida_notas([6, 5, 6, 33, 7]))
print(cal.valida_notas([6, 5, 6, 7, 7]))