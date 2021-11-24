from pprint import pprint

print('-------------------------------------------------------------------------------')
class Coche():
    matricula = None
    num_puertas = None
    color = None
    engine_status = False
    #float(precio = 0) en otros lenguajes
    # def __init__(self,matr, puert, colo): # determina los parameteos necesarios para el coche(matr, puert, colo)
    #     self.matricula = matr
    #     self.num_puertas = puert
    #     self.color = colo
    
    def __str__(self):
        return f'Matrícula: {self.matricula} \nNúmero de puertas: {self.num_puertas}'
    def arrancar(self):
        self.engine_status = True
    def parar_motor(self):
        self.engine_status = False


bmw = Coche()
print(bmw.color)
bmw.arrancar()
print('Engine On: ', bmw.engine_status)
bmw.color = 'Verde'
bmw.matricula = '5456464-pepe'
bmw.num_puertas = '5'
bmw.marca = 'BMW'
bmw.modelo = 'A1'
bmw.precio = '20000' # Crea para el objeto
bmw.parar_motor()
print('Engine Off: ', bmw.engine_status)
print(bmw.precio)
print(bmw.color)
print('-------------------------------------------------------------------------------')
pprint(dir(bmw))
print('-------------------------------------------------------------------------------')
pprint(bmw.__class__) # pertenece al __main__
print('-------------------------------------------------------------------------------')
pprint(bmw.__dict__)
print('-------------------------------------------------------------------------------')
print(bmw) # saca lo que es, a no ser que ya devuelva algo (con return por ejemplo)