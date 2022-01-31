ruta = '/home/alan/Descargas/'
def lee_fichero(nombre):
    try:
        a = open(ruta+nombre,'r')
    except Exception as e:
        print(f'Error abriendo el archivo\nTipo de error: {type(e).__name__} ({e})')
    else:
        datos = a.read()
        print(datos)

#lee_fichero('archivo.txt')# Llamo a un archivo que no existe

def lee_fichero_2(nombre):
    try:
        raise FileNotFoundError('Este es un error provocado')
    except FileNotFoundError as e:
        print(f'Error abriendo el archivo\nTipo de error: {type(e).__name__} ({e})')

lee_fichero_2('archivo.txt')