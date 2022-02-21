                                    # Ejercicio 1 de Alan Sweere Segovia # No Conseguido

ruta_entrada = '/home/alan/Documentos/GitHub/curso_21_22/exam_prog/palabras.txt.TXT'

def devu_lista():
    # leer el archivo
    with open(ruta_entrada) as txt_in:
        lista = txt_in.readlines()
        # buscar elementos con 'e'    
        lista_sin_e = []
        lista_con_e = []

        for l in lista:
            if 'e' in lista:
                lista_con_e.append(l)
            else:
                lista_sin_e.append(l)
        print(lista_sin_e)
        # devolver resultado



        # for l in lista:
        #     if l.find('e'):
        #           lista_con_e.append(l)

        #     else:
        #         lista_sin_e.append(l)
                

#print(devu_lista())
devu_lista()

