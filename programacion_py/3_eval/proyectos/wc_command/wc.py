# 1 Importamos en el que vayamos a utilizar el programa
# 2 init con ruta o ruta + archivo
# 3 cojetamos el archivo como valido
# - 3.0 mostramos error si la URL no es valida
# - 3.1 Si el archivo es binario debe devolver un error indicándolo
# - 3.2 Si el archivo está vacío debe devolver un resultado vacío
# 4 contar lineas
# 5 sumamos el archivo y su ruta a la funcion correspondiente
# 6 un input con ruta o ruta + archivo
# 7 llamamos a la clase con los imput y devolvemos el resultado 

# 1
import mimetypes

class Wc():
    
    # 2
    def __init__(self,ruta,archivo) -> None:
        self.ruta_archivo = ruta
        self.archivo = archivo
        self.contenido = ''
        self.num_frecuencias = {}
        self.num_lineas = 0
        self.num_palabras = 0
        self.basura = '",;.:!¡?¿'

    # 3 y 3.0
    def valida_archivo(self):    
        mine = mimetypes.guess_type(self.ruta_archivo+self.archivo)
        try:
            resp = mine[0].split('/')[0] == 'text'
            return resp
        except:
            raise Exception('Archivo inexistenete o inválido')

    def leer_archivo(self):
        try:
            if self.valida_archivo():
                with open(self.ruta_archivo+self.archivo,'r') as lector:
                    texto = lector.read()
                    # return texto if texto != '' else False # - 3.2 Si el archivo está vacío debe devolver un resultado vacío
                    if texto != '':
                        self.contenido = texto
                        return texto
                    else:
                        raise Exception('El archivo esá vacío')
        except:# - 3.1
            raise Exception('El archivo esá vacío')

    def cuenta_lineas(self):
        self.num_lineas = len(self.ruta_archivo+self.archivo)

    def contar_palabras(self):
        palabras = self.contenido.split()
        self.num_palabras = len(palabras)

    def limpiar_cadena(self):
        limpio = self.contenido.lower()
        for c in self.basura:
            limpio = limpio.replace(c,'')
        self.contenido = limpio

    def frecuencias(self):
        frec_palabras = {}
        contador = 0
        for x in self.contenido:
            if self.contenido:
                frec_palabras[x] += 1
                contador +1
            else:
                frec_palabras[x] = 1
                contador +1

        self.num_frecuencias = frec_palabras

    def frecuencias_2(self):
        frec_palabras = []
        contenido = self.contenido
        for x in contenido:
            frec_palabras.append(contenido.count[x])
        self.num_frecuencias = frec_palabras

    def estadisticas(self):
        self.leer_archivo()
        self.limpiar_cadena()
        self.cuenta_lineas()
        self.contar_palabras()
        self.frecuencias()

        salida = {
            'num_lineas': self.contenido,
            'num_palabras': self.num_palabras,
            'num_frecuencias': self.num_frecuencias
        }
        return salida

        # return f'Número de líneas:{self.num_lineas}\nNúmero de palabras:{self.num_palabras}\nOcurrencias de cada palabra:{self.num_frecuencias}'

    def conjunto_cuenta(self):
        unicas = list(set(self.contenido.split()))
