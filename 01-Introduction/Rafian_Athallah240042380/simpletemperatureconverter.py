#Name: Rafian Athallah Marchansyah
#ID: 2440042380
# Simple python program
print("Hello! Welcome to Rafian's simple temperature converter! Please choose a number: ")
print("(1) Celcius")
print("(2) Fahrenheit")
print("(3) Kelvin")

mainchoice = (int(input("Your choice: ")))
print(mainchoice)
if mainchoice > 3:
    print("Sorry! That choice is not valid.")
if mainchoice < 1:
    print("Sorry! That choice is not valid.")

if mainchoice == 1:
    print("You have chosen celcius! what would you like to convert it to?")
    print("(1) Fahrenheit")
    print("(2) Kelvin")
    choice1 = (int(input("Your choice: ")))
    
    if choice1 > 2:
        print("Sorry! That choice is not valid.")
    if choice1 < 1:
        print("Sorry! That choice is not valid.")
        
    if choice1 == 1:
        c2fv = (float(input("Insert the value you would like to convert: ")))
        print(c2fv)
        c2fa = c2fv * 1.8 + 32
        print(c2fv,"celcius is",c2fa,"fahrenheit.")
        
    if choice1 == 2: 
        c2kv = (float(input("Insert the value you would like to convert: ")))
        print(c2kv)
        c2ka = c2kv + 273.15
        print(c2kv,"celcius is",c2ka,"kelvin.")
        
if mainchoice == 2:
    print("You have chosen fahrenheit! what would you like to convert it to?")
    print("(1) Celcius")
    print("(2) Kelvin")
    choice2 = (int(input("Your choice: ")))
    
    if choice2 > 2:
        print("Sorry! That choice is not valid.")
    if choice2 < 1:
        print("Sorry! That choice is not valid.")
        
    if choice2 == 1:
        f2cv = (float(input("Insert the value you would like to convert: ")))
        print(f2cv)
        f2ca = (f2cv - 32) * (5/9)
        print(f2cv,"fahrenheit is",f2ca,"celcius.")
        
    if choice2 == 2: 
        f2kv = (float(input("Insert the value you would like to convert: ")))
        print(f2kv)
        f2ka =(f2kv - 32) * (5/9) + 273.15
        print(f2kv,"fahrenheit is",f2ka,"kelvin.")
        
if mainchoice == 3:
    print("You have chosen kelvin! What would you like to convert it to?")
    print("(1) Celcius")
    print("(2) Fahrenheit")
    choice3 = (int(input("Your choice: ")))
    
    if choice3 > 2:
        print("Sorry! That choice is not valid.")
    if choice3 < 1:
        print("Sorry! That choice is not valid.")
        
    if choice3 == 1:
        k2cv = (float(input("Insert the value you would like to convert: ")))
        print(k2cv)
        k2ca = k2cv - 273.15
        print(k2cv,"kelvin is",k2ca,"celcius.")
        
    if choice3 == 2: 
        k2fv = (float(input("Insert the value you would like to convert: ")))
        print(k2fv)
        k2fa =(k2fv - 273.15) * 1.8 + 32
        print(k2fv,"kelvin is",k2fa,"fahrenheit.")