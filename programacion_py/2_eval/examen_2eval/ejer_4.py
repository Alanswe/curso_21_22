
class Estudiante():

    def __init__(self,nombre,nota) -> None:
        self.nombre = nombre
        self.nota = nota
        self.min_aprobado = 50

    def __str__(self) -> str:
        return f'Nombre: {self.nombre}, Nota: {self.nota}'

    def es_aprobado(self):
        if self.nota >= self.min_aprobado:
            return 'Aprobado'
        else:
            return 'Suspenso'
