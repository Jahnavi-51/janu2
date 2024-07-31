import calculator
def main():
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))

    result_add = calculator.add(x, y)
    result_sub = calculator.sub(x, y)
    result_mul = calculator.mul(x, y)

    try:
        result_div = calculator.div(x, y)
        print(
            f"\nResults:\nAddition: {result_add}\nSubtraction: {result_sub}\nMultiplication: {result_mul}\nDivision: {result_div}")
    except ValueError as ve:
        print(f"\nError: {ve}")


if __name__ == "__main__":
    main()