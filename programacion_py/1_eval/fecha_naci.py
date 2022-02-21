# pedir fecha naciemiento xx/xx/xxxx y devolver Naciste el día xx del mes xxxxxxxxxx del año xxxx

# meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'semptiembre', 'octubre', 'nobiembre', 'diciembre']

# def mes():
#     fecha = input('Escribe tu fecha de naciemiento (dd/mm/aaaa):  ')
#     divi = fecha.split('/')
#     mess = int(divi[1]) -1
#     mesaje = 'Naciste el día ' + divi[0] + ' del mes' + meses[mess] + ' del año ' + divi[2]
#     return mesaje


# mes()

#                                                Segunda manera

def mes():
    meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'semptiembre', 10:'octubre', 11:'nobiembre', 12:'diciembre'}
    fecha = input('Escribe tu fecha de naciemiento (dd/mm/aaaa):  ')
    divi = fecha.split('/')
    mesaje = 'Naciste el día ' + divi[0] + ' del mes ' + meses[int(divi[1])] + ' del año ' + divi[2]
    return mesaje


print(mes())

