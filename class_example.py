# class Person():
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id
#     def details(self):
#         print(f"Name : {self.name}")
#         print(f"id : {self.id}")
# class Employee(Person):
#     def __init__(self,name,id,post,sal):
#         self.post = post
#         self.sal = sal
#         Person.__init__(self,name,id)
#     def details(self):
#         print(f"Name : {self.name}")
#         print(f"Id : {self.id}")
#         print(f"Post : {self.post}")
#         print(f"Salary : {self.sal}")
# Emp = Employee("janu","12345","Intern",10000)
# Emp.details()

# class Person():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def Display(self):
#         return self.name,self.age
# class Student(Person):
#     def __init__(self,name,age,clg):
#         super().__init__(name,age)
#         self.clg=clg
#     def Display(self):
#         return self.name,self.age,self.clg
# st = Student("vamshi",22,"BEC")
# print(st.Display())

