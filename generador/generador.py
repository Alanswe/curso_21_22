import csv

class Generador():
    __esqueleto = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>"""

    def __generar_esqueleto(self):
        return self.__esqueleto

    def __generar_tabla(self, lista):
        if self.__lista:
            tabla = '<table><tr><td>'
            cabecera = self.__lista[0]
    def generar_pagina(self,lista):
        self.__lista = lista
        if not lista:
            return self.__generar_esqueleto()
        else:
            pag = self.__generar_tabla()

#------------------------------
def leer_dict():
    csv_in = open('/home/alan/Desktop/programacion/curso_21_22/csv/titanic.csv')
    lector_dict = csv.DictReader(csv_in)
    list_dict = list(lector_dict)
    csv_in.close
    return list_dict
#------------------------------------------
       
elementos = leer_dict()
g = Generador()
pagina = g.generar_pagina(elementos)