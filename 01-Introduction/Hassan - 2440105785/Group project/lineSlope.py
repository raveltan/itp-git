def line_slope():
    print("This is Line-Slope Calculator")
    x, y = input("Enter you first set of x and y coordinates: ").split()
    x2, y2 = input("Enter your second set of x and y coordinates: ").split()
    
    yCalc = int(y2) - int(y)
    xCalc = int(x2) - int(x)
    calc = int(yCalc) / int(xCalc)
    return  print("The line slope is ", calc)