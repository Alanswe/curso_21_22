"""
Crear case Calificaciones.
Tendrá método init que admitira como entrada una lista que tenga un alumno y una serie de notas
ejemplo ['Raul',9.2,5,4.5,7,9.1]
Tendrá un método 'calificar' que nos devolvera una tupla que diga nombre y calificación
ejemplo ['Raul','Notable']
"""

"""         MONO
1 - Crear clase Calificaciones.
2 - Init que admite una lista con alumno y una serie de notas ['Raul',9.2,5,4.5,7,9.1]
3 - Método 'calificar' que nos devolvera nombre y calificación ['Raul','Notable']
3 - 1 - hacer media de segundo valor del alumno (de las notas)
3 - 2 - asigar nota a media
                # si es menor que 5 es SUSPENSO, si es de 5 a 7 es APROBADO, 
                # si es de 7 a 9 NOTABLE y si es de 9 a 10 SOBRESALIENTE
4 - STR

"""

# 1
class Calificaciones():
    # 2
    def __init__(self,alumno=[]) -> None:
        if alumno:
            self.alumno = alumno
        else:
            self.alumno = []

    # 3
    def calificar(self):
        calificacion = ''
        media_notas = sum(self.alumno[1:])/len(self.alumno)-1
        # 3 - 2 - asigar nota a media
        if self.alumno:
            if 0 > media_notas < 5:
                calificacion = 'SUSPENSO'
            elif media_notas <7:
                calificacion = 'APROBADO'
            elif media_notas <9:
                calificacion = 'NOTABLE'
            else:
                calificacion = 'SOBRESALIENTE'
            return calificacion
        else:
            return None

    #4 - STR
    def __str__(self) -> str:
        return f'Alumno: {self.alumno[0]} Calificación: {self.calificar()}'

ejemplo_1 = Calificaciones(['Raul',9.2,5,4.5,7,9.1])

print(ejemplo_1.__str__())