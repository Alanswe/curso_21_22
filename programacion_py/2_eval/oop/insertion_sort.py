
class Insort():

    def __init__(self, lista_des) -> None:
        self.lista_des = lista_des

    def ordena(self):
        for x in range(len(self.lista_des)):
            valor_1 = 0
            valor_2 = 0
            posicion_1 = 0
            posicion_2 = 1

            if self.lista_des[posicion_1] > self.lista_des[posicion_2]:
                valor_1 = self.lista_des[posicion_1]
                valor_2 = self.lista_des[posicion_2]
                self.lista_des[posicion_2] = valor_1
                self.lista_des[posicion_1] = valor_2
            else:
                pass
            
            posicion_2 += 1
            posicion_1 += 1
  
        # for x in self.lista_des:
        #     valor_1 = 0
        #     valor_2 = 0
        #     posicion_1 = 0
        #     posicion_2 = 1

        #     if x > self.lista_des[posicion_2]: # self.lista_des[posicion_1]
        #         valor_1 = self.lista_des[posicion_1]
        #         valor_2 = self.lista_des[posicion_2]
        #         self.lista_des[posicion_2] = valor_1
        #         self.lista_des[posicion_1] = valor_2
        #     else:
        #         pass
            
        #     posicion_2 += 1
        #     posicion_1 += 1
    #---------------------------------
        # for x in self.lista_des:
        #     ant = 0
        #     post = 0
        #     if self.lista_des[0] > self.lista_des[1]:
        #         ant = self.lista_des[0]
        #         post = self.lista_des[1]
        #         self.lista_des[1] = ant
        #         self.lista_des[0] = post
        #     else:
        #         pass

       # # [4, 2, 1, 10, 12, 1, 5, 6]
       # # None
       # # [2, 4, 1, 10, 12, 1, 5, 6]


prueba = Insort([4,2,1,10,1,5,6,8,3,7,9])
prueba_2 = Insort([4,3,2,10,12,1,5,6])
# print(prueba.lista_des)
# print(prueba.ordena())
# print(prueba.lista_des)
print(prueba_2.lista_des)
print(prueba_2.ordena())
print(prueba_2.lista_des)
