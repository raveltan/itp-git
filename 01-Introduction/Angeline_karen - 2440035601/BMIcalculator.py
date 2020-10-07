print("Welcome to BMI Calculator!")

gender = input("What is your gender(male or female): ")
height = input("Enter your height in such form 4'8: ")
weight = float(input("Enter your weight in pounds: "))
feet = int(height[0])
inches = int(height[len(height)-1])
def m(feet, inches):
    m = feet * 0.3048
    m = m + (inches * 0.0254)
    return m

# weight conversion from pounds to kg
weight1 = weight*0.453592
formula = weight1/(m(feet, inches)*m(feet, inches))

while gender == "male":
    if formula < 20:
        print("Your BMI is", formula, "in which you're categorized as underweight")
    elif 20 <= formula <= 25:
        print("Your BMI is", formula, "in which you're categorized as normal weight")
    elif 26 <= formula <= 30:
        print("Your BMI is", formula, "in which you're categorized as overweight")
    elif 31 <= formula <= 40:
        print("Your BMI is", formula, "in which you're categorized as obesity")
    elif formula > 40:
        print("Your BMI is", formula, "in which you're categorized as severe obesity")
    else:
        print("There is an error occured. Please kindly input the data as instructed. Thankyou!")
    break
while gender == "female":
    if formula < 19:
        print("Your BMI is", formula, "in which you're categorized as underweight")
    elif 19 <= formula <= 24:
        print("Your BMI is", formula, "in which you're categorized as normal weight")
    elif 25 <= formula <= 30:
        print("Your BMI is", formula, "in which you're categorized as overweight")
    elif 31 <= formula <= 40:
        print("Your BMI is", formula, "in which you're categorized as obesity")
    elif formula > 40:
        print("Your BMI is", formula, "in which you're categorized as severe obesity")
    else:
        print("There is an error occured. Please kindly input the data as instructed. Thankyou!")
    break



