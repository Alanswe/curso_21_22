def suma(num):
    num[0] += 12
    return num

n = [8]                #la variable es mutable y acaba en 20 tal cual fué en el num[0]
print(suma(n))
print(n)

