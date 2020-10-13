import random

# Intro to the game
player_name = input("Hello, what's your name?")
lower = int(input("Input lower bound here:"))
upper = int(input("Input upper bound here:"))
print("Hello.", player_name, "I'm thinking of a number between", lower, "and", upper, "Guess what it is! \n" )
print("You only have 7 tries for this. Best of luck!")

# Loops for the guesses and checks the validity of the inputs
number = random.randint(lower, upper)
number_of_guesses = 0
while number_of_guesses < 7:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print("Too low! try again")
    if guess > number:
        print("Whoa that's too high! try guessing lower")
    if guess == number:
        break

# Affirmation for the number guessing
if guess == number:
    print("That's spot on! It took you", str(number_of_guesses), "tries!")
else:
    print("Awhh that's too bad. The number was", number)
