'''
#prime or not
n= int(input("enter the number ;"))
for i in range(2,x+1):
    for j in range(2,i):
        if i % j == 0:
            break;
    else:
            print("prime",i)'''

'''#Armstrong number 153=1^3+5^3+3^3
n = int((input("Enter the number : ")))
l = len(str(n))
s = 0
tn = n
while tn > 0:
    temp = tn % 10
    s = s + (temp ** l)
    tn = tn // 10
print(s)
if s == n:
    print("Armstrong")
else:
    print("Not an Armstrong")'''
'''#fibonacoi series
n = int(input("enter the number : "))
a = int(input("enter the number : "))
b = int(input("enter the number : "))
for i in range(n):
    print(a)
    a, b = b, a+b'''
'''a = int(input("enter the first number : "))
b = int(input("enter the second number : "))
c = int((a+b)/2)
print(c)'''
'''# matrix
b = int(input("enter the no of rows : "))
c = int(input("enter the no of coloumns : "))
m = []
for i in range(b):
    r = []
    for j in range(c):
        a = int(input("Enter the number : "))
        r.append(a)
    m.append(r)
for i in range(b):
    for j in range(c):
        print(m[i][j], end=' ')
    print()'''



