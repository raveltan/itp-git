from random import randint
import gachasim

def main():
    print("Welcome to our gacha simulator!")
    print("What would you like to roll?")
    print("(1) Roll 1x")
    print("(2) Roll 5x (Guaranteed 3 star item)")
    print("(3) Roll 10x (Guaranteed 4 star item)")

    rollchoice = (int(input("Your choice: ")))
    if rollchoice == 1:
       gachasim.rolling1x(randint(1, 1000))
    elif rollchoice == 2:
       gachasim.rolling5x()
    elif rollchoice == 3:
       gachasim.rolling10x()
    else:
        print("Sorry! That choice is not valid.")

main()