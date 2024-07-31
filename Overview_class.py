class Jahnavi(object):
    name = "hello"
    def __init__(self,a,b,c):
        self.a = a
        self._b = b
        self.__c = c
    # class method
    @classmethod
    def first_method(cls,x,y):
        return f"{x+y} is addition and class method"
    # static method
    @staticmethod
    def second_method(f,g):
        return f"{f*g} is multiplication and it is static_method"
    #instance
    def third_method(self,p,l):
        return f"{p-l} is sutraction and it is third_method"