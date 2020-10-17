import random


Weap_Tier_list = [3,4,5] #constant
Weapon_list = ["Sword", "Spear", "Halberd", "Pike", "Bow", "Gun", "Mace" , "Hammer", "Axe",
              "Shuriken", "Kunai", "Greatsword(2-handed)", "Greathammer(2-handed)", "Throwing Knife"] #constant

Chara_Tier_list = [4,5] #constant
Chara_list_5 = ['Jean','Deluc','Venti','Klee','Mona','Xiao','Qiqi','Keqing'] #constant
Chara_list_4 = ['Amber','Lisa','Kaeya','Barbara','Razor','Bennet','Noele','Fischl','Sucrose','Beidou','Ningguang','Xiangling','Xingqiu','Chongyun'] #constant



def SinglePull(pity4, pity5):

    received = []

    if pity5 == 90:
        Get_Choice = random.randint(0, 2)
        if Get_Choice == 0:
            Get_tier = [5]
            Get = random.choice(Chara_list_5)
        else:
            Get_tier = [5]
            Get = random.choice(Weapon_list)

    elif pity4 == 10:
        Get_Choice_2 = random.randint(0, 1)
        if Get_Choice_2 == 0:
            Get_tier = [4]
            Get = random.choice(Chara_list_4)
        else:
            Get_tier = [4]
            Get = random.choice(Weapon_list)

    else:
        Get_tier = random.choices(Weap_Tier_list, weights=[20, 5, 1])
        Get = random.choice(Weapon_list)

    received.append([Get_tier , Get])

    return received

def TenPull(pity5):

    recieved = list()

    if pity5 == 90:
        #5starGuaranteed
        Get_Choice = random.randint(0,2)
        if Get_Choice == 0:
            Chara_tier = [5]
            Chara = random.choice(Chara_list_5)
            recieved.append([Chara_tier, Chara])
        else:
            Weap_tier = [5]
            Weapon = random.choice(Weapon_list)
            recieved.append([Weap_tier, Weapon])

        #4starGuaranteed
        Get_Choice2 = random.randint(0, 1)
        if Get_Choice2 == 0:
            Charatier = [4]
            Chara = random.choice(Chara_list_4)
            recieved.append([Charatier, Chara])
        else:
            Weaptier = [4]
            Weapon = random.choice(Weapon_list)
            recieved.append([Weaptier, Weapon])


        #the rest of the pull
        for i in range (8):
            Weaptier = random.choices(Weap_Tier_list, weights=[20, 5, 1])
            Weapon = random.choice(Weapon_list)
            recieved.append([Weaptier, Weapon])


    else:
        # 4starGuaranteed
        Get_Choice2 = random.randint(0, 1)
        if Get_Choice2 == 0:
            Chara_tier = [4]
            Chara = random.choice(Chara_list_4)
            recieved.append([Chara_tier, Chara])
        else:
            Weap_tier = [4]
            Weapon = random.choice(Weapon_list)
            recieved.append([Weap_tier, Weapon])


        # the rest of the pull
        for i in range(9):
            Weap_tier = random.choices(Weap_Tier_list, weights=[20, 5, 1])
            Weapon = random.choice(Weapon_list)
            recieved.append([Weap_tier, Weapon])

    return recieved



def StandardDraw():
    total = 0
    Guaranteed_4 = 0
    Guaranteed_5 = 0

    while True:
        print("----------Standard Banner----------")
        print("total =", total)
        print("Guaranteed 4 =", Guaranteed_4)
        print("Guaranteed 5 =", Guaranteed_5)
        print("-----------------------------------")
        print("Your Choice of")
        print("1. 1x Draw")
        print("2. 10x Draw")
        print("type '3' to go back")
        print("-----------------------------------")

        DChoice = eval(input("Draw choice = "))
        if DChoice == 1:
            total += 1
            Guaranteed_4 += 1
            Guaranteed_5 += 1
            Collect = SinglePull(Guaranteed_4,Guaranteed_5)
            print("you got ", Collect[0][0],"-star ", Collect[0][1])
            if Guaranteed_4 == 10:
                Guaranteed_4 = 0
            if Guaranteed_5 == 90:
                Guaranteed_5 = 0

        elif DChoice == 2:
            total += 10
            Guaranteed_5 += 10
            Collect10 = TenPull(Guaranteed_5)
            print(Guaranteed_5)
            for result in Collect10:
                print("You got", result[0], "-star", result[1])
            if Guaranteed_4 == 10:
                Guaranteed_4 = 0
            if Guaranteed_5 == 90:
                Guaranteed_5 = 0

        elif DChoice == 3:
            break
