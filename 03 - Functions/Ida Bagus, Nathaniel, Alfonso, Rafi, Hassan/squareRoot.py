from math import sqrt


def sqr():
    print("This is a Square Root calculator.")
    sqrInput = input("Enter a number you want to get the square root of:  ")

    def result():
        calc = sqrt(int(sqrInput))
        print("The Result is ", calc)

    if len(sqrInput) > 0 and sqrInput.isnumeric:
        result()

    elif sqrInput.isalpha():
        print("Only Numbers are accepted")

    elif len(sqrInput) == 0:
        print("Need Input ")

    else:
        print("Error")
