#1.Write a program which will find all such numbers which are
# divisible by 7 but are not a multiple of 5, between 2000 and 3200
# (both included). The numbers obtained should be printed in a
# comma-separated sequence on a single line.
'''l=[]
for i in range (2000,3201):
    if i % 7 == 0 and i % 5 != 0 :
        print(i,end= ",")'''


#2.Write a program which can compute the factorial of a
# given numbers. The results should be printed in a
# comma-separated sequence on a single line. Suppose the
# following input is supplied to the program: 8 Then,
# the output should be: 40320
# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n-1)
# x = int(input("enter the number : "))
# print(fact(x))


#3.With a given integral number n, write a program to generate
# a dictionary that contains (i, i*i) such that is an
# integral number between 1 and n (both included).
# and then the program should print the dictionary. Suppose
# the following input is supplied to the program: 8 Then,
# the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25,
# 6: 36, 7: 49, 8: 64}
'''
n = int(input("enter the first limit : "))
d = dict()
for i in range(1,n+1):
  d[i] =i*i
print(d)'''

'''4.Write a program which accepts a sequence of comma-separated
 numbers from console and generate a list and a tuple which 
 contains every number. Suppose the following input is 
 supplied to the program: 34,67,55,33,12,98 Then, the output 
 should be: ['34', '67', '55', '33', '12', '98'] 
 ('34', '67', '55', '33', '12', '98')'''
"""value = input()
l = value.split(",")
t = tuple(l)
print(l)
print(t)"""

#5. Define a class which has at least two methods:
# getString: to get a string from console input printString:
# to print the string in upper case. Also please include
# simple test function to test the class methods.
"""
class InputString(object):
  def __init__(self):
    self.s = ""
  def getString(self):
    self.s = input("Enter the string : ")
  def printString(self):
    print(self.s.upper())
object = InputString()
object.getString()
object.printString()
"""
#6. Write a program that calculates and prints the value
# according to the given formula: Q = Square root of
# [(2 * C * D)/H] Following are the fixed values of C and H:
# C is 50. H is 30. D is the variable whose values should
# be input to your program in a comma-separated sequence.
# Example Let us assume the following comma separated input
# sequence is given to the program: 100,150,180 The output
# of the program should be: 18,22,24
# import math
# c = 50
# h = 30
# value = []
# j = input('enter the input:')
# l = j.split(',')
# for d in l:
#     value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
# print(','.join(value))


#7.Write a program that accepts a comma separated sequence
# of words as input and prints the words in a comma-separated sequence
# after sorting them alphabetically. Suppose the following input is supplied to the program:
# without,hello,bag,world Then, the output should be: bag,hello,without,world
# str1 = input("enter the string : ")
# l = str1.split(',')
# l.sort()
# print(','.join(l))

#8.Write a program that accepts sequence of lines as input and prints the lines
# after making all characters in the sentence capitalized. Suppose the following
# input is supplied to the program: Hello world Practice makes perfect Then, the
# output should be: HELLO WORLD PRACTICE MAKES PERFECT
# str1 = input(" enter the string : ")
# str2 = str1.upper()
# print(str2)

#9.Write a program that accepts a sequence of whitespace separated words as input
# and prints the words after removing all duplicate words and sorting them
# alphanumerically. Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again Then, the output
# should be: again and hello makes perfect practice world
# x = input("enter the string")
# j = x.split(" ")
# v = set(j)
# a = list(v)
# a.sort()
# print(" ".join(a))

#10. Write a program that accepts a sentence and calculate the number of letters and
# digits. Suppose the following input is supplied to the program: hello world!
# 123 Then, the output should be: LETTERS 10 DIGITS 3
# str1 = input("entre the string : ")
# count1 = 0
# count2 = 0
# for char in str1:
#     if char.isalpha():
#         count1 += 1
#     elif char.isnumeric():
#         count2 +=1
#     else:
#         pass
# print("LETTERS ",count1)
# print("DIGITS ",count2)


#11.Write a program that accepts a sentence and calculate the
# number of upper case letters and lower case letters. Suppose
# the following input is supplied to the program: Hello world!
# Then, the output should be: UPPER CASE 1 LOWER CASE 9
# str1 = input("enter the string : ")
# count1 = 0
# count2 = 0
# for char in str1:
#     if char.isupper():
#         count1 += 1
#     elif char.islower():
#         count2 += 1
#     else:
#         pass
# print("UPPER CASE : ", count1)
# print("LOWER CASE : ", count2)

# 12.Write a program which accepts a sequence of comma separated 4 digit
# binary numbers as its input and then check whether they are divisible
# by 5 or not. The numbers that are divisible by 5 are to be printed in
# a comma separated sequence. Example: 0100,0011,1010,1001 Then the
# output should be: 1010 Notes: Assume the data is input by console.
# str1 = input("enter the numbers : ")
# v = str1.split(",")
# for i in v :
#     p = int(i,2)
#     if p % 5 == 0:
#         print(i)


#13.Write a program that computes the value of a+aa+aaa+aaaa with a given
# digit as the value of a. Suppose the following input is supplied to
# the program: 9 Then, the output should be: 11106
# x = int(input("enter the value : "))
# b = x + (11 * x) + (111 * x) +(1111 * x)
# print(b)


# 14.Use a list comprehension to square each odd number in a list. The list is
# input by a sequence of comma-separated numbers. Suppose the following
# input is supplied to the program: 1,2,3,4,5,6,7,8,9 Then, the output
# should be: 1,3,5,7,9
# x = input("enter the numbers : ")
# l = x.split(",")
# fl = [i for i in l if int(i)%2!=0]
# print(",".join(fl))

# 15.Write a program that computes the net amount of a bank account based
# a transaction log from console input. The transaction log format
# is shown as following: D 100 W 200
# D means deposit while W means withdrawal. Suppose the following
# input is supplied to the program: D 300 D 300 W 200 D 100 Then,
# the output should be: 500
# import string
# balance = 0
# while True:
#     s = input("enter the values : ")
#     if not s :
#         break
#     l = s.split(" ")
#     o = l[0]
#     a = int(l[1])
#     if o == 'D':
#         balance += a
#     elif o == 'W':
#         balance -= a
#     else:
#         pass
# print(balance)


#16. Write a method which can calculate square value of number
# def square(num):
#     return num ** 2
# n = int(input("enter the numbers :"))
# print(square(n))

#17.Define a class, which have a class parameter and have
# a same instance parameter.
# class Jahnavi :
#     def __init__(self,a):
#         self.a = a

#18.Define a function which can compute the sum of two numbers.
# def sum(a,b):
#     return a+b
# n1 = int(input("enter the a value :"))
# n2 = int(input("enter the b value : "))
# print(sum(n1,n2))


#19.Define a class with a generator which can iterate the
# numbers, which are divisible by 7, between a given
# range 0 and n.
# class Generator:
#     @staticmethod
#     def gen(n):
#         for i in range(1,n):
#             if i % 7 == 0:
#                 print(i,end=" ")
# n = int(input("Enter the value : "))
# print(Generator.gen(n))

#20.Define a function that can accept two strings as
# input and print the string with maximum length in
# console. If two strings have the same length, then the
# function should print al l strings line by line
# def String_print(str1,str2):
#     l1 = len(str1)
#     l2 = len(str2)
#     if l1 == l2 :
#         for char in str1:
#             print(char)
#         for char in str2:
#             print(char)
#     elif l1 > l2 :
#         for char in str1:
#             print(char)
#     elif l1 < l2 :
#         for char in str2:
#             print(char)
#     else :
#         pass
#
# str1 = input("enter the str1 : ")
# str2 = input("enter the str2 : ")
# String_print(str1,str2)

#21.A website requires the users to input username and password to register. Write a program to check the validity of password input by users. Following are the criteria for checking the password:

# At least 1 letter between [a-z]
# At least 1 number between [0-9]
# At least 1 letter between [A-Z]
# At least 1 character from [$#@]
# Minimum length of transaction password: 6
# Maximum length of transaction password: 12 Your
# program should accept a sequence of comma separated
# passwords and will check them according to the above
# criteria. Passwords that match the criteria are to be
# printed, each separated by a comma. Example If the
# following passwords are given as input to the program:
# ABd1234@1,a F1#2w3E*,2We3345 Then, the output of the
# program should be: ABd1234@1
# import re
# s = input("enter the passwords:").split(",")
# list = []
# pattern =r'[#@$]'
# for i in s:
#     if(i.__len__()>5 and i.__len__()<13 ):
#         if re.search("[a-z]",i ) and re.search("[A-Z]",i) and re.search("[0-9]",i) and re.search(pattern,i):
#             list.append(i)
#         else:
#             pass
#     else:
#         pass
# if list:
#     print("Valid passwords:", ",".join(list))
# else:
#     print("No valid passwords found.")

#22.You are required to write a program to sort the
# (name, age, height) tuples by ascending order where
# name is string, age and height are numbers. The tuples
# are input by console. The sort criteria is: 1: Sort
# based on name; 2: Then sort based on age; 3: Then sort
# by score. The priority is that name > age > score. If
# the following tuples are given as input to the
# program: Tom,19,80 John,20,90 Jony,17,91 Jony,17,93
# Json,21,85 Then, the output of the program should
# be: [('John', '20', '90'), ('Jony', '17', '91'),
# ('Jony', '17', '93'), ('Json', '21', '85'),
# ('Tom', '19', '80')]
# l =[]
# while True:
#     a = input("Enter the tuple:")
#     if not a :
#         break
#     else:
#       b = a.split(",")
#       l.append(tuple(b))
# print(sorted(l))


#23.Define a function that can convert a integer
# into a string and print it in console.
# def Con(n):
#     return str(n)
# n = input("enter the number : ")
# print(Con(n))

#24.Define a function that can receive two integral
# numbers in string form and compute their sum and
# then print it in console.
# def likki(a,b):
#     print(int(a)+int(b))
# likki(34,67)

#25.Define a function that can accept two strings as
# input and concatenate them and then print it in
# console.
# def jagu(a,b):
#     print(a+b)
# jagu("Best ","Friend")

#26.Define a function that can accept an integer number
# as input and print the "It is an even number" if the
# number is even, otherwise print "It is an odd number".

# def test(a):
#     if a % 2 == 0:
#         return "It is an even number"
#     else :
#         return "It is an odd number"
# print(test(3456789))

#27.Define a function which can print a dictionary where
# the keys are numbers between 1 and 3 (both included)
# and the values are square of keys.
# d = dict()
# def what():
#     for i in range(1,4):
#         d[i]=i**2
#     return d
# print(what())

#28.Define a function which can print a dictionary
# where the keys are numbers between 1 and 20 (both
# included) and the values are square of keys.
# d = dict()
# def why():
#    for i in range(1,21):
#        d[i]=i**2
#    return d
# print(why())

#29.Define a function which can generate a dictionary where
# the keys are numbers between 1 and 20 (both included)
# and the values are square of keys. The function should
# just print the keys only.
# def how():
#     d = dict()
#     for i in range(1,21):
#         d[i] = i ** 2
#     return d.keys()
# print(how())

#30.Define a function which can generate and print a
# list where the values are square of numbers between
# 1 and 20 (both included).
# def anil():
#     l=[]
#     for i in range(1,21):
#         l.append(i**2)
#     return(l)
# print(anil())

#31.Define a function which can generate a list where the
# values are square of numbers between 1 and 20
# (both included). Then the function needs to print
# the first 5 elements in the list.
# def test(n):
#     l = []
#     for i in range(1,21):
#         l.append(i**2)
#     return(l[:n])
# print(test(5))

#32.Define a function which can generate a list
# where the values are square of numbers between 1 and
# 20 (both included). Then the function needs to print
# the last 5 elements in the list.
# def test(n):
#     l = []
#     for i in range(1,21):
#         l.append(i**2)
#     return(l[-n:])
# print(test(5))

#33.Define a function which can generate a list where
# the values are square of numbers between 1 and 20
# (both included). Then the function needs to print all
# values except the first 5 elements in the list.
# def test(n):
#     l=[]
#     for i in range(1,21):
#         l.append(i**2)
#     return l[n:]
# print(test(5))

#34.Define a function which can generate and print a
# tuple where the value are square of numbers between 1
# and 20 (both included).
# def test():
#     l =[]
#     for i in range(1,21):
#         l.append(i**2)
#     return tuple(l)
# print(test()


#35.With a given tuple (1,2,3,4,5,6,7,8,9,10), write a
# program to print the first half values in one line
# and the last half values in one line.
# def test():
#     t = (1,2,3,4,5,6,7,8,9,10)
#     print(t[:5])
#     print(t[5:])
# test()

#36.Write a program to generate and print another
# tuple whose values are even numbers in the given
# tuple (1,2,3,4,5,6,7,8,9,10).
# def test():
#     t = (1,2,3,4,5,6,7,8,9,10)
#     t1 = []
#     for i in t:
#         if(i % 2 == 0):
#             t1.append(i)
#         else:
#             pass
#     return tuple(t1)
# print(test())

#37.Write a program which accepts a string as input to
# print "Yes" if the string is "yes" or "YES" or "Yes",
# otherwise print "No".
# s= input("enter the string : ")
# l=["yes","Yes","YES"]
# for i in l :
#     if s == str(l[0]):
#         print(i)
#         break
#     else:
#         print('No')

#38.Write a program which can filter even numbers in a list
# by using filter function. The list is:
# [1,2,3,4,5,6,7,8,9,10].
# def even(l):
#     return l % 2 == 0
# l =[1,2,3,4,5,6,7,8,9,10]
# fl = filter(even , l)
# f2=list(fl)
# print(f2)
# l = [1,2,3,4,5,6,7,8,9,10]
# even_numbers = filter(lambda x : x % 2 ==0 ,l)
# l=list(even_numbers)
# print(l)

#39.Write a program which can map() to make a list
# whose elements are square of
# elements in [1,2,3,4,5,6,7,8,9,10].
# l=[1,2,3,4,5,6,7,8,9,10]
# squared_numbers = map(lambda x : x ** 2,l)
# l = list(squared_numbers)
# print(l)

#40.Write a program which can map() and filter() to make a list whose elements
# are square of even number in [1,2,3,4,5,6,7,8,9,10].
# l = [ 1,2,3,4,5,6,7,8,9,10]
# numbers = filter(lambda x : x % 2 == 0,l)
# squ_numbers = map(lambda x : x ** 2,numbers)
# h1 = list(squ_numbers)
# print(h1)

#41.Define a class named American which has a static
# method called printNationality.
# class American(object):
#     @staticmethod
#     def printNationality():
#         print("America")
# america = American()
# america.printNationality()


#42.Define a class named American and its subclass NewYorker.
# class American(object):
#     @staticmethod
#     def What(a):
#         print(a)
# class NewYorker(American):
#     @staticmethod
#     def Why(b):
#         print(b)
# American.What(25)
# NewYorker.Why(10)

#43.Define a class named Circle which can be constructed
# by a radius. The Circle class has a method which can
# compute the area.
# class Circle():
#     pi = 3.14
#     def __init__(self,r):
#         self.r = r
#     def Area(self):
#         a = self.pi  * (self.r**2)
#         print(a)
# crl = Circle(2)
# crl.Area()

#44.Define a class named Rectangle which can be constructed by a length and width
# The Rectangle class has a method which can compute the
# area
# class Rectangle():
#     def __init__(self,len,bre):
#         self.l = len
#         self.b = bre
#     def Area(self):
#         a = self.l * self.b
#         print(a)
# rec = Rectangle(1,3)
# rec.Area()

#45.Define a class named Shape and its subclass Square.
# The Square class has an init function which takes a
# length as argument. Both classes have a area function
# which can print the area of the shape where Shape's
# area is 0 by default.
# class Shape():
#     def __init__(self):
#         pass
#     def Area(self):
#         return 0
# class Square(Shape):
#     def __init__(self,len):
#         Shape.__init__(self)
#         self.l = len
#     def Area(self):
#         a = self.l * self.l
#         return a
# sh = Shape()
# print(sh.Area())
# sq = Square(6)
# print(sq.Area())

#46.Please raise a RuntimeError exception.
# n = input("entre the number :")
# if type(n) == int:
#     print(n)
# else:
#     raise RuntimeError("not a int type!!!")

#47.Write a function to compute 5/0
# and use try/except to catch the exceptions.
# def What():
#     try:
#         return 5/0
#     except ZeroDivisionError:
#         print("Division  by Zero!!!")
#     finally:
#         print("exit code")
# What()

#48.Define a custom exception class which takes a
# string message as attribute
# def Why(a):
#     try:
#         if type(a) == int:
#             return a
#         else:
#             raise ValueError("Input is not an integer")
#     except Exception as e:
#         return f"{e}"
#
# print(Why(a="j"))

#49.Assuming that we have some email addresses in the
# "username@companyname.com" format, please write
# program to print the user name of a given email
# address. Both user names and company names are
# composed of letters only.
# str1 = input("enter the Username : ")
# s = str1.split('@')
# print(s[0])

#50.Assuming that we have some email addresses in the
# "username@companyname.com" format, please write
# program to print the company name of a given email
# address. Both user names and company names are
# composed of letters only.
# str1 = input("enter the Email : ")
# s = str1.split("@")
# st = s[1].split('.')
# print(st[0])


# 52.
# import re
# s = input("Enter the String : ")
# print(re.findall("\d+",s))

#53.Write a program to compute
# 1/2+2/3+3/4+...+n/n+1 with a given n input by
# console (n>0).
# Example: If the following n is given as input to the
# program:
# 5
# Then, the output of the program should be:
# 3.55
# In case of input data being supplied to the question,
# it should be assumed to be a console input.
# Hints: Use float() to convert an integer to a float
# def compute(n):
#     count = 0.0
#     for i in range(1,n+1):
#         x = float(i/(i+1))
#         count += x
#     return count
# m = int(input("Enter the No :"))
# h=compute(m)
# print(h)

#54.Write a program to compute:
# f(n)=f(n-1)+100 when n>0 and f(0)=1
# with a given n input by console (n>0).
# Example: If the following n is given
# as input to the program:
# 5
# Then, the output of the program should be:
# 500
# In case of input data being supplied to the question,
# it should be assumed to be a console input.
# Hints: We can define recursive function in Python.

# def fact(n):
#     if n == 0:
#         return 0
#     else:
#         return fact(n-1) + 100
#
# print(fact(5))

#55.The Fibonacci Sequence is computed based on the
# following formula:
# f(n)=0 if n=0 f(n)=1 if n=1 f(n)=f(n-1)+f(n-2) if n>1
# Please write a program to compute the value of f(n)
# with a given n input by console.
# Example: If the following n is given as input to the
# program:
# 7
# Then, the output of the program should be:
# 13
# In case of input data being supplied to the question,
# it should be assumed to be a console input.
# Hints: We can define recursive function in Python.

# def f(n):
#     if n == 0 :
#         return 0
#     elif n == 1 :
#         return 1
#     else:
#         return f(n-1)+f(n-2)
# m = int(input("enter the value : "))
# print(f(m))

# 56.The Fibonacci Sequence is computed based on the
# following formula:
# f(n)=0 if n=0 f(n)=1 if n=1 f(n)=f(n-1)+f(n-2) if n>1
# Please write a program to compute the value of f(n)
# with a given n input by console.
# Example: If the following n is given as input to the
# program:
# 7
# Then, the output of the program should be:
# 0,1,1,2,3,5,8,13
# In case of input data being supplied to the question,
# it should be assumed to be a console input.
# Hints: We can define recursive function in Python.

# def f(n):
#     if n == 0 :
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return (f(n-1)+f(n-2))
# m = int(input("enter the no: "))
# v = [(f(b)) for b in range(0, m+1)]
# print(v, end = ",")

# def f(n):
#     h =[]
#     def j(n):
#         if n == 0 :
#             return 0
#         elif n == 1 :
#             return 1
#         else:
#             return j(n-1)+j(n-2)
#     for i in range(0,n+1):
#         h.append(j(i))
#     return h
# m = int(input("enter the no: "))
# print(f(m))

#57.Please write a program using generator to print the
# even numbers between 0 and n in comma separated form
# while n is input by console.
# Example: If the following n is given as input to the
# program:
# 10
# Then, the output of the program should be:
# 0,2,4,6,8,10
# Hints: Use yield to produce the next value in generator.
# In case of input data being supplied to the question,
# it should be assumed to be a console input.

# def even(n):
#     l=[]
#     for i in range(0,n+1):
#         if i % 2 == 0 :
#             l.append(i)
#     return l
# n = int(input("enter the number : "))
# print(even(n))

def even(n):
        if n % 2 == 0 :
            return n
n = int(input("enter the number : "))
v = [even(n) for n in range(0,n+1)]
print(v)

