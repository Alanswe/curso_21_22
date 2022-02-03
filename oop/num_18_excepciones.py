# https://docs.python.org/es/3/library/exceptions.html
def dividir(a,b):
    # 1.- comprobar que b no sea 0
    # 2.- dividir y controlar el error

    # if b == 0:
    #     return None
    # else:
    #     return a/b
    
    resultado = None
    try:
        # Lista de instrucciones
        resultado = a/b
    except (ZeroDivisionError, TypeError) as e: # Ponemos la excepcion que queremos gestionar
        # Instrucciones si hay error
        print('Se ha producido un error en la división') # Manejador de la excepción
        print(F'Error específico: {e}')
        print(F'Tipo de error: {type(e).__name__}')
    # except TypeError:
    #     print('Solo se pueden dividir datos numéricos')
    else:
        print('Esta es la parte del else')
    finally:
        print('Esto es el finally')
    return resultado
        
    # return a/b

print(dividir(4,0))
print('--------------------')
print(dividir(4,'F'))