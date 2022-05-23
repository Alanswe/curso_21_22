class A():

    def get_class(self): 
        return self.__class__ 

    def prue(self):
        return self.__class__.__bases__

class B(A): 
    def __init__(self) -> None:
        super().__init__()

b = B() 
a = A()
print(b.get_class())
print(b.prue())


class Base(): 
    pass 

class Derived(Base):
    def print_base(self):
        for base in self.__class__.__bases__:
            print(base.__name__)

foo = Derived()
foo.print_base()
