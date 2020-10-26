def length_vec():
    from math import sqrt
    print("This is Vector Length Calculator")
    print("Enter the Length of coordinate x and y.")
    x, y = input("x and y coordinate: ").split()

    length = sqrt(int(x) ** 2) + sqrt(int(y) ** 2)
    return print("The length of the Vector is ", length)

