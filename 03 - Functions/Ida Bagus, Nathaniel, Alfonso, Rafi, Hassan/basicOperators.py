def calc():
    print("This is a calculator.")
    print(
        "Choose your first number, then a sign and then the last number, + , - , * , / , % , **")

    num1 = int(input("Enter the first Number: "))
    sign = input("Enter the Sign: ")
    num2 = int(input("Enter the number: "))

    if sign == "+":
        result = int(num1) + int(num2)
        print("The result is ", result)

    elif sign == "-":
        result = int(num1) - int(num2)
        print("The result is ", result)

    elif sign == "*":
        result = num1 * num2
        print("The result is ", result)

    elif sign == "/":
        result = num1 / num2
        print("The result is ", result)

    elif sign == "**":
        result = num1 ** num2
        print("The result is ", result)

    elif sign == "%":
        result = num1 % num2
        print("The result is ", result)

    else:
        print("Something went wrong.")
