
def clase(vehiculo):
    return type(vehiculo).__name__

def clase_padre(vehiculo):
    for base in vehiculo.__class__.__bases__:
        return base.__name__

# Ejer 8
def clase_padre_del_padre(vehiculo):
    for base in vehiculo.__class__.__bases__:
        for base_2 in base.__bases__:
            return base_2.__name__
