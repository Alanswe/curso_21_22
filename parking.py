# Nos tiene que decir el importe que tenemos que pagar por el parking 
# 1 semana = 100, 1 dia = 42

#Es importante definir antes las contante para qure sea más facil lectura todo el mundo

PRECIO_SEMANA = 100
PRECIO_DIA = 42

def parking(dias):
   num_semanas = dias//7
   num_dias = dias%7
   cal_semanas = num_semanas * PRECIO_SEMANA 
   cal_dias = num_dias * PRECIO_DIA
   total = cal_semanas + cal_dias
   return total

print(parking(24))