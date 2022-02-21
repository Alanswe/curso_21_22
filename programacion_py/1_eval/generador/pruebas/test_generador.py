import unittest
import generador

__esqueleto = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>"""


class test_generador(unittest.TestCase):
    def test_xx(self):
        respuesta = generador.Generador().__generar_esqueleto([])
        self.assertEqual(respuesta,__esqueleto)