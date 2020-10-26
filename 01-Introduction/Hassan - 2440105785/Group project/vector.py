from math import sqrt

# User Input for the intended choice
def vec_choice():
    print("Welcome to Vector Calculator")
    print("Chose what you want to find for Vector projection, determinant, vector degrees or dot product: ")
    choice = input("Enter your Choice: ")

    if choice == "vector projection":
        vproj()

    elif choice == "determinant":
        detr()

    elif choice == "vector degrees":
        vdeg()

    elif choice == "dot product":
        dot()

    else:
        print("Invalid Input")


# Vector Projection
def vproj():
    a, a2 = input("Enter a1 and a2: ")
    b, b2 = input("Enter b1 and b2: ")
    a = int(a)
    a2 = int(a2)
    b = int(b)
    b2 = int(b2)

    def dot_product():
        return (a * b) + (a2 * b2)

    def vec_length():
        return (sqrt(b ** 2) + sqrt(b2 ** 2)) ** 2

    def result():
        ansOne = (dot_product() / vec_length()) * b
        ansTwo = (dot_product() / vec_length()) * b2

    result()


# Determinant
def detr():
    a, a2 = input("Enter a1 and a2: ")
    b, b2 = input("Enter b1 and b2: ")
    a = int(a)
    a2 = int(a2)
    b = int(b)
    b2 = int(b2)

    detCalc = (a * b2) - (a2 * b)
    print("The areal area of Parallelogram:", detCalc)
    triChoice = input("Do you want to calculate the area of the triangle?: ")

    if triChoice == "yes" or 'y':
        result = detCalc * 0.5
        print("The area of the triangle is", result)


# Vector Degrees
def vdeg():
    a, a2 = input("Enter a1 and a2: ").split()
    b, b2 = input("Enter b1 and b2: ").split()
    a = int(a)
    a2 = int(a2)
    b = int(b)
    b2 = int(b2)

    dotCalc = (a * b) + (a2 * b2)
    lengthCalc = (sqrt(a) + sqrt(a2)) * (sqrt(b) + sqrt(b2))
    degs = dotCalc / lengthCalc
    print("The result: ", degs)


# Dot Product
def dot():
    a, a2 = input("Enter a1 and a2: ").split()
    b, b2 = input("Enter b1 and b2: ").split()
    a = int(a)
    a2 = int(a2)
    b = int(b)
    b2 = int(b2)

    dotCalc = (a * b) + (a2 * b2)
    print("The result: ", dot)
