''' # prime number
x = int(input("enter the no : "))
for i in range(2, (x//2)+1):
    if x % i == 0:
        print(f"{x} is not a prime number...")
        break
else:
    print(f"{x} is a prime number...")'''
'''# biggest among three
x = int(input("enter the no1 : "))
y = int(input("enter the no2 : "))
z = int(input("enter the no3 : "))
if (x > y and x > z):
    print(f"{x} is the biggest number")
elif (y > x and y > z) :
    print(f"{y} is  the Biggest number")
else:
    print(f"{z} is the biggest number")
#divisble by 5 from 1 to 100
count = 1
while count <= 100:
    if count % 5 == 0:
         print("count : ", count)
    count += 1
for i in range(1,100):
    if(i % 5 == 0):
        print(i)'''
"""x = int(input("Enter the value 1 :"))
y = int(input("Enter the value 2 :"))
for i in range(x, y) :
    if i%2==0:
        print(f"{i} is even")"""
'''n = int(input("enter the no : "))
if n % 2 == 0:
    print("even")
else:
    print("odd")'''
