import csv

class Generador_ul():
    __MARCADOR ='##_##'
    __lista = None
    __esqueleto = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            ##_##
        </body>
        </html>
    """
    def __generar_esqueleto(self):
        return self.__esqueleto

    def __generar_tabla(self):       
        if self.__lista:
            tabla = '<ul>'
            cabecera = list((self.__lista[0]).keys())
            for c in cabecera:
                tabla += f'<li>{c}</li>'
            tabla += '</ul>'
        return tabla

    def generar_pagina(self,lista):
        self.__lista = lista
        vacio = self.__generar_esqueleto()
        
        pag = self.__generar_tabla()
        completa= vacio.replace(self.__MARCADOR,pag)

        with open('C:\Users\Alan\Documents\GitHub\curso_21_22\generador\tabla_despegable.html','w') as arch:
            arch.write(completa)

# -----------------------

def leer_dict():
    csv_in = open('C:\Users\Alan\Documents\GitHub\curso_21_22\titanic.csv')
    lector_dict = csv.DictReader(csv_in)
    lista_dict = list(lector_dict)
    csv_in.close()
    return lista_dict

elementos = leer_dict()
g = Generador_ul()
pagina = g.generar_pagina(elementos)
