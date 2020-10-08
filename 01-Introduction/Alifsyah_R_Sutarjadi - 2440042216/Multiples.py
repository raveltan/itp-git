multiples = int(input("Put a number down and I will tell you if said number is a multiple of any single digit number or not.\n"))
division = 0
remainder = 0
number = 2
active = True

def multiplesExe():
    if multiples % number == 0:
        division = multiples//number
        print("\n" + str(multiples) + " is a multiple of " + str(number) + " because " + str(multiples) + " divided by " + str(number) +" is " + str (division) + ".")
    else:
        remainder = multiples % number
        print ("\n" + str(multiples) + " is not a multiple of " + str(number) + " as you are left with a remainder of " + str(remainder) + ".")

while active == True:
    if number >= 10:
        number = 2
        multiples = input ("You may input another number or you may terminate the program by typing stop.\n")
    else:
        multiplesExe()
        number += 1

    if multiples == 'stop':
        print ("Multiples.py has been terminated. \n")
        break
    else:
        multiples = int(multiples)