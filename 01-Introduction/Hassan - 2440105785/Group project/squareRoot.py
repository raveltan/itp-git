def sqr():
    from math import sqrt
    print("This is a Square Root calculator.")
    sqrInput = input("Enter a number you want to get the square root of:  ")

    def numeric():
        calc = sqrt(int(sqrInput))
        print("The Result is ", calc)

    if len(sqrInput) > 0 and sqrInput.isnumeric:
        numeric()

    elif sqrInput.isalpha():
        print("You need to use Numbers")

    elif len(sqrInput) == 0:
        print("You must type something ")

    else:
        print("Something went wrong")
