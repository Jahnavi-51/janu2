#Implement a Python class FileUtility with methods for
# reading and writing files. Include methods for reading
# text files, writing to text files, and copying files.
# class FileUtility:
#     def __init__(self,file):
#         self.file = file
#     def write123(self,file):
#         with open(file, "w") as file1:
#             file2 = file1.write()
#     def read123(self,file):
#         with open(file,'r') as file1:
#             file2 = file1.read()
#     def copy123(self,file):
#         with open(file,'r') as file1:
#             file2 = file1.read()
#         with open(file2,'w') as file3:
#             file4 = file3.write()
#     FileUtility =

#Create a Python class MathOperations with static methods
# for basic mathematical operations such as addition,
# subtraction, multiplication, and division.
# class MathOperations:
#     @staticmethod
#     def add(x,y):
#         return x+y
#     @staticmethod
#     def sub(x,y):
#         return x-y
#     @staticmethod
#     def mul(x,y):
#         return x*y
#     @staticmethod
#     def div(x,y):
#         try:
#             return x//y
#         except Exception as e:
#             return e
# print("addition: ",MathOperations.add(85,25))
# print("subracation: ",MathOperations.sub(85,25))
# print("multiplication: ",MathOperations.mul(85,25))
# print("division: ",MathOperations.div(85,25))


#3.Design a Python class ConfigParser with static methods for parsing
# configuration files in different formats (e.g., JSON, YAML).
# import json
# import yaml
#
# class ConfigParser:
#
#     @staticmethod
#     def parse_json(file_path):
#         with open(file_path, 'r') as f:
#             return json.load(f)
#
#     @staticmethod
#     def parse_yaml(file_path):
#         with open(file_path, 'r') as f:
#             return yaml.safe_load(f)
#
# json_config = ConfigParser.parse_json("C:\\Users\\LENOVO\\Documents\\json.json")
# print(json_config)
#
# yaml_config = ConfigParser.parse_yaml("C:\\Users\\LENOVO\\Documents\\config.yaml")
# print(yaml_config)


# 4.Design a Python class GeometryHelper with static methods
# for calculating the area and perimeter of common geometric
# shapes such as circles, rectangles, and triangles.
import math
# class GeometryHelper:
#     pi = 3.14
#     @classmethod
#     def circles(cls,r):
#         area = cls.pi * r * r
#         perimeter =2 * cls.pi * r
#         return area,perimeter
#     def rectangles(l,w):
#         area = l*w
#         perimeter = 2 * (l+w)
#         return area, perimeter
#     def triangles(a,b,c):
#         s = (a+b+c)/2
#         area = math.sqrt(s *(s-a) * (s-b)*(s-c))
#         perimeter = a+b+c
#         return area , perimeter
# print("circle:",GeometryHelper.circles(4))
# print("rectangles:",GeometryHelper.rectangles(4,5))
# print("circle:",GeometryHelper.triangles(2,3,4))

#5.Write a python program which hits the API and checks
# the response

# import requests
#
# def check_api(url):
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         print("API request Successfull! ")
#         print("Status_code:",response.status_code)
#         print("Response JSON : ",response.json())
#     except requests.exceptions.HTTPError as http_e:
#         print(f"HTTP error occurred :{http_e}")
#     except Exception as e:
#         print(f"other error occurred :{e}")
# api_url ='https://reqres.in/api/users?page=2%27'
# check_api(api_url)

#6.Write a program which exaplins method overriding
# and overloading

# OVERLOADING
# class man:
#     @staticmethod
#     def speak():
#         print("man speaks")
#
# class baby(man):
#     @staticmethod
#     def speak():
#         print("Baby cries")
# man.speak()
# baby.speak()
# # OVERRIDING
#
# class cal:
#     @staticmethod
#     def add(a,b,c):
#         return a+b+c
#
# class calcu:
#     @staticmethod
#     def add(*args):
#         return sum(args)
#
# print(cal.add(1,2,3))
# print(calcu.add(1,2,3,4,5,6,7,8,98))

#Create a package folder with two module1.py & module2.py
# files containing 4 fucntions and import the package
# with two specific functions
# from module_1 import add, sub
# from module_2 import mul, div
# print(add(2,3))
# print(sub(2,3))
# print(mul(2,3))
# print(div(2,3))