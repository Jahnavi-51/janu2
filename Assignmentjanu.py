#1.Write a program to find the frequency of each word in a file.
'''
def word_frequency(file1,word):
    words = content.lower().split()
    count = words.count(word.lower())
    return count
word = input("enter the to find the frequency : ")
file_path = "C:\\Users\\LENOVO\\Documents\\input.txt"
with open(file_path, "r") as file:
    file1 = file.read()

f = word_frequency(file1,word)
print(f)


#2.Write a function to merge two sorted lists into one sorted list.

l1=[],l2=[]
n1 = int(input("enter the no of values for list1 : "))
n2 = int(input("enter the no of values for list2 : "))
for i in range(n1):
    x = int(input("enter the value : "))
    l1.append(x)
for i in range(n2):
    y = int(input("enter the value : "))
    l2.append(y)
l1.sort()
l2.sort()
l3 = l1+l2
l3.sort()
print("Sortedlist3: ", l3)
'''

#3.Write a program to remove all punctuation from a given string.
'''
import string
def remove_punctuation(input_string):
    translator = str.maketrans('', '', string.punctuation)
    return input_string.translate(translator)

o_string = input("Enter the string:")
c_string = remove_punctuation(o_string)
print("String without Punctuation:", c_string)'''
# second method AND ALSO REMOVING NUMBERS FROM THE STRING AND PRINT THEM
'''import string
def remove_punctuation(input_string):
    # removing punctutions( including white spaces)
    punct = ''.join([char for char in input_string if char  in string.punctuation])
    # removing numbers from a str
    numb = ''.join([char for char in input_string if char in string.digits])
    # plan string without puncations and also numbers
    pla_str = '' . join([char for char in input_string if char.isalpha()])
    #removing white_spaces
    remove_whitespaces = ''.join(char for char in input_string if char not in string.whitespaces )
    return punct,numb,pla_str,remove_whitespaces

o_string = input("Enter the string: ")
pun, num, str1 , rstr= remove_punctuation(o_string)
print(pun)
print(num)
print(str1)
print(r_str)
'''
'''
# REMOVE SPACES
str1 = input("enter the string: ")
r = str1.replace(" ", "")
print(r)
'''
#4.Write a program to read a file in reverse order.

'''file_path = "C:\\Users\\LENOVO\\Documents\\input.txt"
with open(file_path, "r") as file:
    file1 = file.read()
    print(type(file1))
    print(file1[::-1])

 # reverse the lines in a file   
def read_file_reverse(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

            lines_without_comments = [line for line in lines if not line.startswith('#')]

            reversed_lines = lines_without_comments[::-1]

            for line in reversed_lines:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except IOError:
        print(f"Error: Could not read ")
file_path ="C:\\Users\\LENOVO\\Documents\\input.txt"
read_file_reverse(file_path)'''

#5.Write a function to flatten a nested list.

def flatten_list(nested_list):
    flat_list = []#[1,2,3,4,5,6,7,8,9]
    for item in nested_list:#[1,2,[3,4],[5,6,7[8,9]]]
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

user_list = []
while True:
    user_input = input()
    if user_input.lower() == 'done':
        break
    user_list.append(eval(user_input))

flat_list = flatten_list(user_list)
print(flat_list)

#6.Write a program to split a string into words without using split()
'''def split_fun(input_str):
    w = []
    cw = []

    for char in input_str:
        if char == ' ':
            if cw:
                w.append(''.join(cw))
                cw = []
        else:
            cw.append(char)

    # Append the last word if any
    if cw:
        w.append(''.join(cw))
 

#7.Write a program to count the number of lines in a file.

'''file_path = "C:\\Users\\LENOVO\\Documents\\programming language.txt"
with open(file_path, 'r') as f:
    c = 0
    for line in f:
        c += 1
print("line_count : ", c)'''

#8.Write a function to generate the first n numbers of the Fibonacci series.

'''def fibonacci_series(n):
    f = []
    a, b = 0, 1
    while n > 0:
        f.append(a)
        a, b = b, a + b
        n -= 1
    return f
n = int(input("enter the number : "))
x = fibonacci_series(n)
print(x)'''

#9.Write a program to find the length of a string without using len()
'''
str1 = input("enter the string : ")
count=0
for i in str1:
    count += 1
print(count)
'''
#10.Write a program to reverse a given string.
'''
str1 = input("enter the string : ")
#print(str1[::-1])'''

#11.Write a program to swap the values of two variables.
"""
a = int(input("enter the a value : "))
b = int(input("enter the b value ; "))
print(a,b)
a, b = b, a
print( a,b)
"""
#non-breaking space &npsp
#12.to read n number of lines in a file
'''
def print_first_n_lines(file_path, n):
    try:
        with open(file_path, 'r') as file:
            # Read the first n lines from the file
            for i in range(n):
                line = file.readline()
                # If the file has less than n lines, break the loop
                if not line:
                    break
                else:
                    print(line.strip())  # strip() to remove newline characters
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except IOError:
        print(f"Error: Could not read the file '{file_path}'.")

# Example usage:
file_path = 'C:\\Users\\LENOVO\\Documents\\input.txt'
print_first_n_lines(file_path,2)'''
