print("Welcome to a simple program to calculate in 3 options : factorial, exponentiation, and tetration.")
print("mode : fact, exp, tetr, help")
while(True):
    mode = input("Enter a mode:")
    if mode == "fact":
        test_case = int(input("Enter how many test cases:"))
        print("Please enter integers for the next", test_case, "query(-ies).")
        for i in range(test_case):
            num = int(input())
            result = num
            for j in range(1, num):
                result *= j
            if (num == 0): result = 1
            print(result)
    elif mode == "exp":
        test_case = int(input("Enter how many test cases:"))
        print("Please enter pairs of numbers with the syntax \"(base,(whitespace)exponent)\" for the next", test_case, "query(-ies).")
        for i in range(test_case):
            base, exponent = eval(input())
            print(base**exponent)
    elif mode == "tetr":
        test_case = int(input("Enter how many test cases:"))
        print("Please enter pairs of numbers with the syntax \"(base,(whitespace)height)\"")
        print("Note : height should be a positive integer." , test_case, "query(-ies).")
        for i in range(test_case):
            base, height = eval(input())
            result = base
            for j in range(height-1):
                result = base**result
            print(result)
    elif mode == "help":
        print("This is a simple program with 3 options : factorial, exponentiation, and tetration")
        print("Note : the limits of calculation on each computers may vary due to hardware and software specifications.")
        string = input("Which options would you like to learn more ?")
        if (string == "factorial"):
            print("Factorial is an unary operator that takes a number n and returns the result of n*(n-1)...1.")
            print("In mathematical notation, usually it is represented by n! (read : \"n factorial\").")
            print("To avoid errors when using this option, the input must be an integer.")
        elif (string == "exponentiation"):
            print("Exponentiation is a binary operator that takes 2 numbers, the first as the base b and the second as the exponent x.")
            print("It will return the value of b multiplied by itself x times. In mathematical notation, it is usually written b^x.")
            print("To avoid errors with this option, the exponent must be an integer.")
        elif (string == "tetration"):
            print("Tetration is a binary operator that takes 2 numbers, the first as the base b abd the second as the height h.")
            print("It will return the value of b exponentiated by itself h times, where the order of operation is from the topmost first.")
            print("For example we have base 2 and height 4. Therefore it will return 2^16 as the answer, not 2^8.")
            print("To avoid errors with this option, the height must be an integer.")
        elif (input == "exit"): break
        else: print("Command is unavailable, please try again.")
    else: print("Mode does not exists, please try again.")













