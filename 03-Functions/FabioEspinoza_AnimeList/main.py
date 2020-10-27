import weeb

if __name__ == "__main__":
    # Creating Weebs
    group = int(input("How many people are in your group: "))
    people = ["person"+str(i) for i in range(group)]
    weebers = {person : weeb.Weeb(input("Enter First Name: "), input("Enter Last Name: ")) for person in people}


    #Creating Their Favorite Animes and Displaying it
    for i in range(len(weebers)):
        obj = weebers.get("person"+str(i))
        obj.favorite_animes()
        obj.introduction()

