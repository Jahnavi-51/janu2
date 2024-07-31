"""def add(a,b):
    return a+b
def avg(a,b):
    return add(a,b)//2

a = int(input("enter the value 1 : "))
b = int(input("enter the value 2 : "))
print("Addition",add(a,b))
print("Average ",avg(a,b))"""

"""l=[1,2,3,4,5,6,7,8,9,20,39,45,36,76,65,45,23,98,87,76,65,54,43,32,21,10]
s=list(map(lambda x :x**2,l))# predefined higerorder functions
print(s)"""

l=[1,2,3,4,5,6,7,8,9,20,39,45,36,76,65,45,23,98,87,76,65,54,43,32,21,10]
e = list(filter(lambda x : x % 2 == 0, l))
print(e)

