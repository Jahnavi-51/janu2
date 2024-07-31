'''class Pandu:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def janu(self):
        print(self.name,self.age)
person1 = Pandu("janu",22)
print(person1.age)
person1.janu()'''
'''
class Janu:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        print(a+b)
a = int(input("enter the a value : "))
b = int(input("enter the b value : "))
janu1 = Janu(a, b)
janu1.add() '''
''''
class Vasu:
    def __inti__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def avg(self):
        c = (a+b)/2
        print(c)
a = int(input("enter the value 1 : "))
b = int(input("enter the value 2 : "))
Vasu1 = Vasu()
Vasu1.avg()
'''
#Define a Python class BankAccount with attributes account_number and balance.
# Implement methods deposit(amount) and withdraw(amount) to modify the balance.
# Ensure appropriate validation in the withdraw method to prevent overdrafts
# class BankAccount:
#     def __init__(self, bal, wid, dep):
#         self.bal = bal
#         self.wid = wid
#         self.dep = dep
#     def deposit(self):
#         dep = int(input("enter amount to deposit : "))
#         if dep <= 0:
#             print("Invalid Amount.....")
#         else:
#             self.bal += dep
#             print("Deposit Successful!!!")
#             print("Balance : ", self.bal)
#     def withdrawl(self):
#         if self.bal <= 0:
#             print("Account balance is 0")
#         wid = int(input("enter the amount to withdrawl : "))
#         if wid <= 0:
#             print("Invalid Amount!!!")
#         elif wid > self.bal:
#             print("Insufficent funds!!!")
#         else:
#             self.bal -= wid
#             print("Withdrawl Successfully!!!!")
#             print(self.bal)
# janu = BankAccount(1000,0,0)
# i = 1
# while i > 0:
#     print("1.WITHDRAWL\n2.DEPOSIT\n3.BALANCE\n4.Exit")
#     ch = int(input("Enter the choice : "))
#     if ch == 1:
#         janu.withdrawl()
#     elif ch == 2:
#         janu.deposit()
#     elif ch == 3:
#         print("Balance : ", janu.bal)
#     elif ch == 4:
#         exit()
#     else:
#         print("Invalid Choice!!!")
