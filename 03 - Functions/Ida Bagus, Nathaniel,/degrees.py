def deg():
    import math
    print("This is Degrees Calculator")
    degChoice, num = input("Enter sin, cos or tan and your number: ").split()
    degChoice = degChoice.lower()

    if degChoice == "sin":
        calc = math.sin(math.radians(int(num)))
        print("The result is ", calc)
    elif degChoice == "cos":
        calc = math.cos(math.radians(int(num)))
        print("The result is ", calc)
    elif degChoice == "tan":
        calc = math.tan(math.radians(int(num)))
        print("The result is ", calc)

    else:
        print("Invalid Input") 
