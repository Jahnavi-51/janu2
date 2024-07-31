import random_generator
from random_generator import random_gen
n = int(input("enter "))
a = int(input("enter the 1st number : "))
b = int(input("enter the 2nd number : "))
c = random_gen(n,a,b)
print(c)
"""
from random_generator import random_gen
def main():
    try:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))

        random_numbers = random_gen(10, start, end)

        print(f"\nGenerated 10 random numbers within [{start}, {end}]:")
        print(random_numbers)

    except ValueError:
        print("Invalid input. Please enter integers for the range.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()"""