import math


def add(x, y):
    """Function to add two numbers"""
    return x + y

def subtract(x, y):
    """Function to subtract two numbers"""
    return x - y



print("Select operation:")
print("1. Add")
print("2. Subtract")



while True:
    choice = input("Enter choice (1- Add 2- Subtract ): ")

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


    else:
        print("Invalid input. Please enter a valid number (1/2/3/4).")