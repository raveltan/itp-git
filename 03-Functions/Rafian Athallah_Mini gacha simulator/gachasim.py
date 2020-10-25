from random import randint


def rolling1x(roll_result):
    if roll_result in range(1, 601):
        print("Nice! You got a 2 star item.")
    if roll_result in range(601, 851):
        print("Congrats! You got a 3 star item.")
    if roll_result in range(851, 976):
        print("Wonderful! You got a 4 star item.")
    if roll_result in range(976, 1001):
        print("Amazing! You got a 5 star item. Nice luck!")

def rolling5x():
    for i in range(4):
        rolling1x(randint(1, 1000))
    rolling1x(696)

def rolling10x():
    for i in range(9):
        rolling1x(randint(1, 1000))
    rolling1x(869)
