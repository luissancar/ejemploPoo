## Ejemplo poo Python


class Padre(object):
    def __init__(self):
        print("Padre")

class Hijo1(Padre):
    def __init__(self):
        print("Hijo1")

class Hijo2(Padre):
    def __init__(self):
        super(Hijo2, self).__init__()
        print("Hijo2")


class OtroFamiliar(Hijo2,Hijo1):
    def __init__(self):
        super(OtroFamiliar, self).__init__()
        print("Otro familiar")




print("Objeto hijo1:")
print(Hijo1.__mro__)
objetoHijo1=Hijo1()

print("\n\nObjeto hijo2:")
print(Hijo2.__mro__)
objetoHijo2=Hijo2()


print("\n\nObjeto otroFamiliar:")
print(OtroFamiliar.__mro__)
objetoOtroF=OtroFamiliar()

