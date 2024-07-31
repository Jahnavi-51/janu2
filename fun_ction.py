"""def hello(name,place,s):
    print("Hey!!, Hello "+name)
    print("i am from "+place+"  "+s+"  "+"state")
hello("janu","Vijayawada","A.P")
"""

"""def my_number(no):
    for x in no:
        print(x)
l=[12,52,42,85,63,45,11,63]
my_number(l)"""

'''def what(*args):
    print("arbitary arugument  " +args[3])
what("janu","vasu","likki","stupid","ravi","uma")'''

x = lambda a,b : a + b
print(x(234,345))


# Defining a fucntion
# def first(firstname,lastname,sirname):
#     print("Firstname" + " " + firstname  + "lastname" +  lastname)
#
# first("Ganesh","Aditya","Marupudi")


# def my_func(cars):
#     for x in cars:
#         print(x)
# cars = ["merc","tesla","audi"]
# my_func(cars)

# def multiarg(*num):
#     print("Arbitary Argument" + num[2])
# multiarg("test1","test2","test3","test4")

##  * args which is for arbitary number of number and ** kwargs arbitary number of keywords
# def keyarg(**kwargs):
#     print("Keyword Args", kwargs["test3"])
# keyarg(test1="Ganesh", test2= "Aditya", test3= "Marupudi")


## Lambda Function

# x = lambda a,b : a * b
# print(x(5,4))

## Return Values
# def my_fucn(x):
#     return 5 * x
# print(my_fucn(5))
"""def myself(x):
    if x % 2 == 0:
        return x
print("even : " , myself(2345766))"""

