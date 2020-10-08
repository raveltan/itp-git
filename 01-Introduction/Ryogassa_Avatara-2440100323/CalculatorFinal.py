# Name    : Ida Bagus Ryogassa Avatara
# ID      : 2440100323
# Program : Basic Calculator

# Function to add two numbers
def add(num1, num2):
    return num1 + num2


# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2


# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2


# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2


print("####### CALCULATOR #######")
print("Operations (1. Add, 2. Subtract, 3. Multiply, 4. Divide) \n")

# Take inputs from the user
operation = int(input("Please select operations from 1, 2, 3, 4 : "))

num1 = eval(input("Enter first number: "))
num2 = eval(input("Enter second number: "))

if operation == 1:
    print(num1, "+", num2, "=", add(num1, num2))

elif operation == 2:
    print(num1, "-", num2, "=", subtract(num1, num2))

elif operation == 3:
    print(num1, "*", num2, "=", multiply(num1, num2))

elif operation == 4:
    print(num1, "/", num2, "=", divide(num1, num2))

else:
    print("Invalid Input")
