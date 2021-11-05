import os
from settings import RUTA_BASE,MI_CARPETA,CODIGO      #crt+espacio para mostrar las opciones



os.system('clear')

# with open('listas.py') as arch:
#     l = arch.read()
#     print(l)

# ruta = os.getcwd()
# print(ruta)

# contenido = os.scandir() # Escanea la carpeta y muestra los archivos 
# for f in contenido:
#     print(f)

os.system('clear')

# nuevo_dir = os.chdir('/')
# actual = os.getcwd()
# print(actual)

nuevo_dir = os.chdir('/home/alan/Desktop')
actual = os.getcwd()
print(actual)

archivos = os.scandir()
print(archivos)

#nuevo_dir = os.chdir(RUTA_BASE + CODIGO)
# actual = os.getcwd()
# print(actual)
# archivos = os.scandir(actual + CODIGO) 
# for f in archivos:
#     print(f)


ruta_salida = RUTA_BASE + CODIGO + MI_CARPETA
if not os.path.exists(ruta_salida):
    os.makedirs(ruta_salida)
nuevo = open(ruta_salida + 'mi_archivo.txt', 'w')
nuevo.write('Hola Mundo')
nuevo.close()
print()
