#3. Write a program which prints numbers in range1,100 which divisible by 5
count = 1
while count <= 100:
    if count % 5 == 0:
         print("count : ", count)
    count += 1
for i in range(1,100):
    if(i % 5 == 0):
        print(i)

#2. Create a list of length 10 including numbers and strings
l=[1,5,3,8,9,'janu','vasu','apple','bat','cat']

#a. Slice the list till the index 8
print(l[:8])

#b. Print the element which is located at index 8
print(l[8])

#c. Perofrm sort and reverse operations on the list

# Sorting
num = [item for item in l if isinstance(item, (int, float))]
str = [item for item in l if isinstance(item, str)]
num.sort()
str.sort()
l1 = num +str
print(l1)

#Reversing
l.reverse()
print(l)

#d. Write a program which takes string as input and reverses that string
str = input("Enter the String : ")
print(str)
#1
rev =''
for char in str:
    rev = char +rev
print(rev)
#2
rev = str[::-1]
print(rev)
#3
rev = ''.join(reversed(str))
print(rev)


#1.Write a python program to print only dictionary keys and values separately.Take a dictionary with 5 items (Key-Value Pairs)
d = {'name':'janu','age':'22','blood':'b+','clg':'Bec','mail':'b@gmail.com'}
print(d)
print("Keys : ", d.keys())
print("values: ", d.values())

#a. From the above dictionary pop or remove the last element
print(d.popitem())
print(d)

#b. Take dictionary from 1.a and add the following key & pair i;e "car":"Tesla" to the dictionary if the key exsists then it should update the value otherwise it should add the Key
new = {'car':'tesla'}
d.update(new)
print(d)

#c.Convert the dictionary to List
l1=list(d.keys())
print(l1)
l2 = list(d.values())
print(l2)
l=l1+l2
print(l)

