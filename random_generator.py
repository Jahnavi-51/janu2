#1.Create a Python module named
# random_generator.py that
# contains a function to generate a list of random numbers.
# Write a program to import this module and generate a list
# of 10 random
# numbers within a specified range entered by the user.
import random
def random_gen(n,a,b):
    r=[]
    for i in range(n):
        ran = random.randint(a,b)
        r.append(ran)
    return r
'''import random

def generate_random_numbers(n, start, end):
    random_numbers = []
    for _ in range(n):
        rand_num = random.randint(start, end)
        random_numbers.append(rand_num)
    return random_numbers'''