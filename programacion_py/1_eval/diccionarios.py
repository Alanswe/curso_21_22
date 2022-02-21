# #Se reperesnta entre llaves {}
# diccionario = {
#     'nombre' : 'Fernando',
#     'apellido1' : 'Lopez',
#     'notas' : [1,2,3,4]

# }


# diccionario['apellido2'] = 'García'   #Para añadir o modificar elemntos al diccionario


# print(diccionario['nombre']) #Para impirimr elementos del diccionario 
# print(f"Nombre completo: {diccionario['nombre']} {diccionario['apellido1']}")
import pprint
vscode = {
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Archivo actual",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        }
    ]
}

vscode["configurations"][0]['type'] = 'Manolito' #Para acceder a un dicionario con una lista con un diccionario dentro
tpm = vscode
pprint.pprint(tpm)