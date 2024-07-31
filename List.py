"""x = 25
print(hex(x))
print(hex(id(x)))"""
janu = [10, 20, 30, 24, 10, 25, 45, 67, 36, 78, 97]
"""x=int(input("Enter the number of values u want to insert : "))
for i in range(x):
    ele = input("enter the value : ")
    janu.append(ele)"""
print(janu)
print("printing from index 2 ", janu[2:])
janu[5] = 'wastefellow'
print("replaceing the element : ", janu)
janu.insert(8, 'vamsi')
print("inserting new element in the index:", janu)
janu1 = janu.copy()
print("copied list :", janu1)
janu.extend(['stupid', 'vasu', 'ravi'])
print("Extended ", janu)
print("Count ", janu.count(10))
print(janu.index(10))
print(janu)
janu.pop(10)
print(janu)
janu.remove(36)
print(janu)
janu1=[1,2,4,5,9,87,5]
l = janu1.sort()
print(l)
janu.reverse()
print(janu)
janu.clear()
print(janu)
janu2 = ['a','b','e','c','janu','z','g','b','v']
janu2.sort()
print(janu2)