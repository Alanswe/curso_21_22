"""
Partiendo del proyecto Calificaciones:
- Leer de un archivo csv los nombres de alumnos y sus calificaciones (10)
- Crear la lista de alumnos del aula
- Para cada alumno calcular e imprimir su calificación
"""
"""
Ejercicio 1 de Alan Sweere
Consiste en el anterior metodo Calificaciones, recilcado para que adminta tmabien archivo csv externos
"""
import csv

class NotasInvalidasError(Exception):
    pass

archivo_alumnos = '/home/alan/Documentos/GitHub/curso_21_22/oop/boletin_3/alumnos.csv'

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
    
    def leer_alumnos_desde_csv(self):
        csv_in = open(archivo_alumnos) 
        lector_dic = csv.DictReader(csv_in)
        lista_dict = list(lector_dic)
        csv_in.close()
        return lista_dict

    # def leer_valores_2(self,num):
    #     lista = Calificaciones().leer_alumnos_desde_csv()
    #     nombre = lista[num]
    #     notas = []
    #     for alum in lista[num]:
    #         for dato in alum[num]:
    #             notas.append[dato]
    #     return(f'{nombre}{notas}')

    # def leer_valores(leer_alumnos_desde_csv):
    #     alumno = ''
    #     notas = []
    #     for alum in leer_alumnos_desde_csv:
    #         if alum:
    #             alumno = alum[1]
    #         else:
    #             notas += 1
    #     return(f'{alumno}{notas}')

    @property
    def get_alumno(self):
        return self.__nombre,self.notas

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
    
    def alumno_sin_registro(self, nuevo_alumno):
        if self.__nombre == '':
            self.__nombre = nuevo_alumno
        return self.__nombre

    def set_alumno(self, alum):
        self.__nombre = alum[0]
        for elem in alum[1:]:
            self.__notas.append(elem)
        self.__calificacion = self.calcula_calificacion()

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def set_nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    @property
    def notas(self):
        return self.__notas

    @notas.setter
    def set_notas(self, nuevas_notas):
        try:
            if self.valida_notas(nuevas_notas):
                self.__notas = nuevas_notas
                self.__calificacion = self.calcula_calificacion()
        except NotasInvalidasError:
            raise Exception('Notas inválidas')        
    
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

# print(Calificaciones().leer_alumnos_desde_csv())