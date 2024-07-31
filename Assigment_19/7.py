#1. What is operator overlaoding.
# Write a program to explain the same
# class First():
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def __sub__(self,other):
#         return self.a - other.a,self.b - other.b
#     def __mul__(self,other):
#         return self.a * other.a,self.b * other.b
#
#     def __str__(self,other):
#         return f"{self.a, self.b,other.a,other.b}"
# fs = First(2,3)
# ft = First(1,2)
#
# print(fs - ft)
# print(fs * ft)
import sys

#2.What are property decorators
# it is a way to manage axis to intstance attributes in
# cls by using methods like attributes
#getter , setter, deleter we use this as attribute
# class Second():
#     def __init__(self,a):
#         self._a=a
#     @property
#     def a(self):
#         return self._a
#     @a.setter
#     def a(self,b):
#        self._a = b
# sc = Second("janu")
# print(sc.a)
# sc.a = ("likki")
# print(sc.a)

#3.Method Resolution Order
# class A():
#     def Hello(self):
#         print("Hello from A")
# class B():
#     def Hello(self):
#         print("hello from B")
# class C():
#     def Hello(self):
#         print("Hello from C")
# class D(A,C):
#     def Hello(self):
#         pass
# d = D()
# d.Hello()
# print(D.__mro__)

#4. What is duck typing in python. Explain with a
# program for the same
#Duck Typing is a type system used in dynamic languages.
# For example, Python, Perl, Ruby, PHP, Javascript, etc.
# where the type or the class of an object is less
# important than the method it defines. Using Duck Typing,
# we do not check types at all. Instead, we check for the
# presence of a given method or attribute.

# class Janu():
#     def fun(self):
#         print("Janu")

# class Likki():
#     def fun2(self):
#         print("Likki")
# def funn(obj):
#     obj.fun()
# o1=Janu()
# o2=Likki()
# funn(o1)

#5. What is shallow copy and deep copy of objects in python.
# Explain with a program
# import copy
# l = [1,2,3,4,5,[6,7,8,[9,10]]]
# cp =copy.copy(l)
# print(l)
# print(cp)
# cp[5][3][0] = 95
# print(cp)
# print(l)
# dp = copy.deepcopy(l)
# print(l)
# print(dp)
# cp[5][3][0] = 123
# print(l)
# print(dp)

#6. What is type hinting and annotations in python
#Type hinting allows you to specify the expected
# type of variables and function arguments
# a: int = 17
# b: str = "janu"
# c: bool = True
# print(a,b,c)
# way to attach metadata to function
# arguments and return values
# annotations
# def greet(name: str) -> str:
#     return f"Hello, {name}"
# print(greet("vamshi"))
# -> is indicating the anntations


#7.What is a context manager in python. Write a program
# to explain the same

# class Filemanager():
#     def __init__(self,filename,mode):
#         self.filename = filename
#         self.mode = mode
#     def __enter__(self):
#         self.file = open(self.filename,self.mode)
#         return self.file
#     def __exit__(self,exc_type,exc_value,traceback):
#         self.file.close()
#         if exc_type:
#             print(F"Exception{exc_type}{exc_value}")
# with Filemanager('janu.txt','w') as file:
#     file.write("Hey vamshi 's mom was quite nice and very cool")

# from contextlib import contextmanager
#
# @contextmanager
# def open_file(filename, mode):
#     file = open(filename, mode)
#     try:
#         yield file
#     finally:
#         file.close()
#
# # Using the open_file context manager
# with open_file('example.txt', 'w') as file:
#     file.write('Hello, World!')


# class Person :
#     def __init__(self,msg):
#         self.msg = msg
#     # def __getitem__(self, i):
#     #     return self.msg[i]
#     def __setitem__(self, key, value):
#        self.msg[key] = value
# d = Person({1:2,3:4,5:6})
# d[2] = 9
# d[3] = 8
# print(d.msg)
#print(f"The Value of the first key is : {d[1]}")

# class Hello:
#     def __init__(self,a):
#         self.a = a
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index ->

# x = [1,2,3,4,5,6,7,8,9]
# y = iter(x)
# print(next(y))
# print(sys.getsizeof(y))
# print(next(y))
# print(sys.getsizeof(y))
# print(next(y))
# print(sys.getsizeof(y))
# print(next(y))
# print(sys.getsizeof(y))
# print(next(y))
# print(sys.getsizeof(y))
# print(next(y))
# print(sys.getsizeof(y))
# print(next(y))
# print(sys.getsizeof(y))
