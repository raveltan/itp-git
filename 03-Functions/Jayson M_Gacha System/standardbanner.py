import random

DChoice = 0
Guaranteed4 = 0 #number of pulls, when 10, u get 4-star
Guaranteed5 = 0 #number of pulls, when 90, u get 5-star
WeapTierlist = [3,4,5]
Weaponlist = ["Sword", "Spear", "Halberd", "Pike", "Bow", "Gun", "Mace" , "Hammer", "Axe",
              "Shuriken", "Kunai", "Greatsword(2-handed)", "Greathammer(2-handed)", "Throwing Knife"]
CharaTierlist = [4,5]
Charalist5 = ['Jean','Deluc','Venti','Klee','Mona','Xiao','Qiqi','Keqing']
Charalist4 = ['Amber','Lisa','Kaeya','Barbara','Razor','Bennet','Noele','Fischl','Sucrose','Beidou','Ningguang','Xiangling','Xingqiu','Chongyun']
total = 0


def SinglePull():
    global Guaranteed4, Guaranteed5, total

    if Guaranteed5 >= 90:
        GetChoice = random.randint(0, 2)
        if GetChoice == 0:
            Get_tier = [5]
            Get = random.choice(Charalist5)
        else:
            Get_tier = [5]
            Get = random.choice(Weaponlist)
        Guaranteed5 = 0

    elif Guaranteed4 >= 10:
        GetChoice2 = random.randint(0, 1)
        if GetChoice2 == 0:
            Get_tier = [4]
            Get = random.choice(Charalist4)
        else:
            Get_tier = [4]
            Get = random.choice(Weaponlist)

    else:
        Get_tier = random.choices(WeapTierlist, weights=[80, 15, 1])
        Get = random.choice(Weaponlist)
        #reset the counter if get certain tier
        if Get_tier == 4:
            Guaranteed4 = 0
        elif Get_tier == 5:
            Guaranteed5 = 0

    #correction when using different pulls
    if Guaranteed4 >= 10:
        Guaranteed4 = 0


    Guaranteed4 += 1
    Guaranteed5 += 1
    total += 1
    print("You Got", Get_tier,"-star", Get)

def TenPull():
    global Guaranteed4, Guaranteed5, total
    recieved = list()

    if Guaranteed5 >= 90:
        #5starGuaranteed
        GetChoice = random.randint(0,2)
        if GetChoice == 0:
            Charatier = [5]
            Chara = random.choice(Charalist5)
            recieved.append([Charatier, Chara])
        else:
            Weaptier = [5]
            Weapon = random.choice(Weaponlist)
            recieved.append([Weaptier, Weapon])
        Guaranteed5 = 0

        #4starGuaranteed
        GetChoice2 = random.randint(0, 1)
        if GetChoice2 == 0:
            Charatier = [4]
            Chara = random.choice(Charalist4)
            recieved.append([Charatier, Chara])
        else:
            Weaptier = [4]
            Weapon = random.choice(Weaponlist)
            recieved.append([Weaptier, Weapon])

        # correction when using different pulls
        if Guaranteed4 > 10:
            Guaranteed4 = 0

        #the rest of the pull
        for i in range (8):
            Weaptier = random.choices(WeapTierlist, weights=[80, 15, 1])
            Weapon = random.choice(Weaponlist)
            recieved.append([Weaptier, Weapon])
            # reset the counter if get certain tier
            if Weaptier == 4:
                Guaranteed4 = 0
            elif Weaptier == 5:
                Guaranteed5 = 0
    else:
        # 4starGuaranteed
        GetChoice2 = random.randint(0, 1)
        if GetChoice2 == 0:
            Charatier = [4]
            Chara = random.choice(Charalist4)
            recieved.append([Charatier, Chara])
        else:
            Weaptier = [4]
            Weapon = random.choice(Weaponlist)
            recieved.append([Weaptier, Weapon])

        # correction when using different pulls
        if Guaranteed4 > 10:
            Guaranteed4 = 0

        # the rest of the pull
        for i in range(9):
            Weaptier = random.choices(WeapTierlist, weights=[80, 15, 1])
            Weapon = random.choice(Weaponlist)
            recieved.append([Weaptier, Weapon])
            # reset the counter if get certain tier
            if Weaptier == 4:
                Guaranteed4 = 0
            elif Weaptier == 5:
                Guaranteed5 = 0

    Guaranteed5 += 10
    total += 1
    # printing
    for result in range(10):
        print("You got", recieved[result][0], "-star", recieved[result][1])


def StandardDraw():
    global DChoice
    while True:
        print("----------Standard Banner----------")
        #print("Guaranteed 4 =", Guaranteed4)
        #print("Guaranteed 5 =", Guaranteed5)
        print("total pulls = ", total)
        print("-----------------------------------")
        print("Your Choice of")
        print("1. 1x Draw")
        print("2. 10x Draw")
        print("type '3' to go back")
        print("-----------------------------------")
        DChoice = eval(input("Draw choice = "))
        if DChoice == 1:
            SinglePull()
        elif DChoice == 2:
            TenPull()
        elif DChoice == 3:
            break
