from bottle import route,run

@route('/')
def home():
    return '¡Hola Mundo!'

@route('/hola')
def home():
    return '¡Hola Caracola!'

@route('/hola/<nombre>')
def home(nombre):
    return f'¡Hola {nombre}!'

# @route('/hola/<nombre>')
# def home(nombre=None):
#     if not nombre:
#         return '¡Hola Caracola!'
#     else:
#         return f'¡Hola {nombre}!'

run(host='localhost',port=8080, debug=True)
