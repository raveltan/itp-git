
seats = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]


def draw():
    print("  BIOSKOP NO 5JT ")
    print("   1  2  3  4  5")
    for i in range(len(seats)):
        print(i + 1, seats[i])


def main():
    print("                  ")
    print("INI ADALAH BIOSKOP")
    print("------------------")
    print("  BIOSKOP NO 5JT ")
    print("   1  2  3  4  5")
    for i in range(len(seats)):
        print(i + 1, seats[i])
    print("------------------")
    print("1. Book a seat")
    print("2. Cancel booking ")
    print("------------------")
    pilihan = int(input("choice = "))
    if pilihan == 1:
        draw()
        row = int(input("row = "))
        clmn = int(input("clmn = "))
        if seats[row - 1][clmn - 1] == 1:
            print("error")
            input()
        else:
            print("ARE YOU SURE ??(Y/N)")
            pilihan1 = input()
            if (pilihan1.lower() == "n"):
                print("cancelled")
                input()
            elif (pilihan1.lower() == "y"):
                seats[row - 1][clmn - 1] = 1


    elif pilihan == 2:
        draw()
        row1 = int(input("row = "))
        clmn1 = int(input("clmn = "))
        seats[row1 - 1][clmn1 - 1] = 0


while True:
    main()
