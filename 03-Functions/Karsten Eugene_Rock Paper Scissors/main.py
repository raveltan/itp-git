import game

if __name__ == "__main__":
    play_time = int(input("Enter the amount of times you want to play: "))
    n_wins, n_loss, n_draw = game.start(play_time)

    if n_wins > n_loss:
        print("""
        ######## GAME ENDED! ########
        ######## YOU WIN! ########
        """)
    elif n_wins < n_loss:
        print("""
        ######## GAME ENDED! ########
        ######## YOU LOSE! ########
        """)
    elif n_wins == n_loss:
        print("""
        ######## GAME ENDED! ########
        ######## TIE! ########
        """)
    else:
        print("""
        ######## GAME ERROR! ########
        """)

    print("Wins:", n_wins)
    print("Loss:", n_loss)
    print("Draws:", n_draw)

# Group members: Darren, Ellyz, Karsten, Vania
