import math


def add(x, y):
    """Function to add two numbers"""
    return x + y

def subtract(x, y):
    """Function to subtract two numbers"""
    return x - y

def multiply(x, y):
    """Function to multiply two numbers"""
    return x * y

def divide(x, y):
    """Function to divide two numbers"""
    return x / y

def modulo(x, y):
    """Function of the modulo of two numbers"""
    return x % y

def power(x, y):
    """Function of the power of two numbers"""
    return math.pow(x,y)



print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulo")
print("6. Power")



while True:
    choice = input("Enter choice (1- Add 2- Subtract 3- Multiply 4- Divide 5- Modulo 6- Power): ")

    if choice in ('1'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))

        break


    if choice in ('2'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '2':
            print("Result:", subtract(num1, num2))

        break

    if choice in ('3'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '3':
            print("Result:", multiply(num1, num2))

        break

    if choice in ('4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '4':
            print("Result:", divide(num1, num2))

        break

    if choice in ('5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '5':
            print("Result:", modulo(num1, num2))

        break

    if choice in ('6'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '6':
            print("Result:", power(num1, num2))

        break


    else:
        print("Invalid input. Please enter a valid number (1/2/3/4/5/6).")