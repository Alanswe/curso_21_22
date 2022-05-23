import wc


ruta_ext = input('Introduce ruta del archivo:\nEjemplo(/home/user/desktop/):')
archivo_ext = input('Introduce archivo:\nEjemplo(archivo.txt):')
ejemplo_0 = wc.Wc(ruta_ext,archivo_ext)

ejemplo = wc.Wc('/home/alan/Documentos/GitHub/wc_command/','README.md')
ejemplo_2 = wc.Wc('/home/alan/Documentos/GitHub/wc_command/archivos/','pureba_sucia.txt')

ejemplo_0.leer_archivo()

