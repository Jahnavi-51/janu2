# # single inheritance
# class Parent:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def Add(self):
#         t = self.a+self.b
#         return t
# class Child(Parent):
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def Add(self):
#         t = self.a +self.b
#         return t
# ch = Child(2,4)
# print(ch.Add())

#multiple inheritance - 1child , many parents
# class Parent():
#     @staticmethod
#     def Apple(name,age):
#         return name,age
# class Parent1():
#     @staticmethod
#     def Pineapple(name,age):
#         return name,age
# class Child(Parent,Parent1):
#     @staticmethod
#     def Orange(name,age):
#         return name,age
# print(Child.Orange("janu", 22))
# print(Child.Apple("likki", 22))
# print(Child.Pineapple("Vamsi",22))

#multilevel inhertance
# class Parent():
#     @classmethod
#     def Hello(cls,name) :
#         return f"Hello {name}"
# class Child(Parent):
#     @classmethod
#     def Hi(cls,name):
#         return f"Hi {name}"
# class Child1(Child):
#     @classmethod
#     def Hey(cls,name):
#         return f"Hey {name}"
# print(Child1.Hi("janu"))
# print(Child.Hello("vasu"))
# print(Child1.Hey("vamsi"))
# print(Child1.Hello("anil"))
# print(Parent.Hello("sai"))

# Hierarchical Inheritance


# __having one parent class and many child classes
#Polymorphism
# class Animal:
#     def speak(self):
#         print("Animal speaks")
#
# class Mammal(Animal):
#     def walk(self):
#         print("Mammal walks")
#
# class Dog(Mammal):
#     def bark(self):
#         print("Dog barks")
#
# # Create an instance of Dog
# dog = Dog()
# dog.speak()  # Inherited from Animal
# dog.walk()   # Inherited from Mammal
# dog.bark()   # Defined in Dog
#

# class Bird:
#     def fly(self):
#         print("Bird flies")
#
# class Swimmer:
#     def swim(self):
#         print("Swimmer swims")
#
# class Duck(Bird, Swimmer):
#     def quack(self):
#         print("Duck quacks")
#
# # Create an instance of Duck
# duck = Duck()
# duck.fly()   # Inherited from Bird
# duck.swim()  # Inherited from Swimmer
# duck.quack() # Defined in Duck

# Encapsulation
# wrapping data and the methods that can work on data
# within one unit
# class Hello():
#     def __init__(self):
#         self.__a = 2
#         print(self.__a)
# class Hey(Hello):
#     def __init__(self):
#         Hello.__init__(self)
#         print(self.__a)
#         self.__a = 3
#         print(self.__a)
# ob = Hey()
# ob1 = Hello()
# print(ob.__a)
# print(ob1.__a)

#Data Abstraction
# class Bankaccount():
#     def __init__(self,bal):
#         self.__bal = bal
#     def Deposit(self,amt):
#         if self.__bal <= amt :
#             return "Please Give Sufficent Amount!!!"
#         else:
#            self.__bal += amt
#            return f"Deposit Sucessfully {amt}"
#     def Withdrawl(self,amt):
#         if self.__bal <= amt:
#             return "Invalid Amount!!!"
#         else:
#             self.__bal -= amt
#             return f"Withdrawl succesfully {amt}"
#     def getbalance(self):
#         return self.__bal
# bk =Bankaccount(10000)
# print(bk.Deposit(200))
# print(bk.Withdrawl(8000))
# print(bk.getbalance())

#Abstract classes
# from abc import abstractmethod
# class Hello():
#     @abstractmethod
#     def method_1(self):
#         pass
# class Hi(Hello):
#     def method_1(self):
#         print("janu is a good girl")
# h =Hi()
# h.method_1()