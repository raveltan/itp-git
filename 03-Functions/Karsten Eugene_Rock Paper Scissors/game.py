import random


def start(n_time):
    count = 0
    score = 0
    wins = 0
    loss = 0
    draw = 0
    rps = ["Rock", "Paper", "Scissors"]
    while count < n_time:
        user_input = input("Choose Rock, Paper, or Scissors: ")
        computer_input = rps[random.randint(0, 2)]
        print("")
        print("Player chose:", user_input)
        print("Computer chose:", computer_input)
        print("")
        if user_input == rps[0] and computer_input == rps[2]:
            print("Player smashed Computer with Rock!")
            print("")
            score += 1
            wins += 1
            count += 1
        elif user_input == rps[1] and computer_input == rps[0]:
            print("Player wrapped Computer with Paper!")
            print("")
            score += 1
            wins += 1
            count += 1
        elif user_input == rps[2] and computer_input == rps[1]:
            print("Player cut Computer with Scissors!")
            print("")
            score += 1
            wins += 1
            count += 1
        elif user_input == rps[2] and computer_input == rps[0]:
            print("Computer smashed Player with Rock!")
            print("")
            loss += 1
            count += 1
        elif user_input == rps[0] and computer_input == rps[1]:
            print("Computer wrapped Player with Paper!")
            print("")
            loss += 1
            count += 1
        elif user_input == rps[1] and computer_input == rps[2]:
            print("Computer cut Player with Scissors!")
            print("")
            loss += 1
            count += 1
        elif user_input == computer_input:
            print("OOF")
            print("")
            draw += 1
            count += 1
        else:
            print("Invalid choice from user!")
            print("Game will stop...")
            break

    return wins, loss, draw
