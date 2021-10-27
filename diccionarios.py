#Se reperesnta entre llaves {}
diccionario = {
    'nombre' : 'Fernando',
    'apellido1' : 'Lopez',
    'notas' : [1,2,3,4]

}


diccionario['apellido2'] = 'García'   #Para añadir o modificar elemntos al diccionario


print(diccionario['nombre']) #Para impirimr elementos del diccionario 
print(f"Nombre completo: {diccionario['nombre']} {diccionario['apellido1']}")