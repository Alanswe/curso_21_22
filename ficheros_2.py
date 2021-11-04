import os 
os.system('clear')

with open('listas.py') as arch:
    l = arch.read()
    print(l)

ruta = os.getcwd()
print(ruta)

contenido = os.scandir() # Escanea la carpeta y muestra los archivos 
for f in contenido:
    print(f)