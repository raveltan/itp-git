from basicOperators import calc
from squareRoot import sqr
from vectorLength import length_vec
from lineSlope import line_slope
from degrees import deg
from vector import vec_choice

# Ida Bagus Ryogassa Avatara (2440100323), Nathaniel Alvin (2440042430),
# Alfonso ritchie (2201798130), Rafi Muzakki (2440035614), and Hassan Mohamed (2440105785)

# These are the choices the user can input. When done correctly, it will call the function based on what the user inputs
def userChoice():
    if choice == "calculator":
        calc()  # basicOperators.py

    elif choice == "square root":
        sqr()  # squareRoot.py

    elif choice == "vector length":
        length_vec()  # vectorLength.py

    elif choice == "line slope":
        line_slope()  # lineSlope.py

    elif choice == "degrees":
        deg()  # degrees.py

    elif choice == "vector":
        vec_choice()  # vector.py

    else:
        print("Invalid Input.")


if __name__ == "__main__":
    print("ADVANCE CALCULATOR!")
    print("Made by Ida Bagus Ryogassa Avatara (2440100323), Nathaniel Alvin (2440042430)"
          ", Alfonso ritchie (2201798130), Rafi Muzakki (2440035614), and Hassan Mohamed (2440105785)")

    print("Pick Calculator, Square Root, Vector Length, Line Slope, degrees, and Vector")

    choice = input("Enter Here: ").lower()

    if len(choice) > 0:
        userChoice()

    else:
        print("Invalid Input")
