import random
from typing import List



def weapon_banner(n, pity4,pity5):
    weapon_type_list = ["Sword", "Spear", "Halberd", "Pike", "Bow", "Gun",
                        "Hammer", "Axe", "Kunai", "Shuriken", "Great Sword(2-handed)",
                        "Greathammer(2-handed)", "Throwing Knife", "Staff", "Scepter"]
    weapon_tier_list = [3, 4, 5]
    weapon_type: List[str]
    weapon_tier: List[str]
    weight = (80, 15, 1)
    recieved = []


    if n == 10: #ten pulls\
        if pity5 > 90:
            #5star
            weapon_type = random.choice(weapon_type_list)
            weapon_tier = [5]
            recieved.append([weapon_tier, weapon_type])
            #4star
            weapon_type = random.choice(weapon_type_list)
            weapon_tier = [4]
            recieved.append([weapon_tier, weapon_type])
            #therest
            for i in range(8):
                weapon_type = random.choice(weapon_type_list)
                weapon_tier = random.choices(weapon_tier_list, weights=weight)
                recieved.append([weapon_tier, weapon_type])
        else:
            weapon_type = random.choice(weapon_type_list)
            weapon_tier = [4]
            recieved.append([weapon_tier,weapon_type])
            for i in range(9):
                weapon_type = random.choice(weapon_type_list)
                weapon_tier = random.choices(weapon_tier_list, weights=weight)
                recieved.append([weapon_tier, weapon_type])



    elif n == 1: #single pull
        if pity5 >90:
            weapon_type = random.choice(weapon_type_list)
            weapon_tier = [5]
            recieved.append([weapon_tier, weapon_type])
        elif pity4 >= 10:
            weapon_type = random.choice(weapon_type_list)
            weapon_tier = [4]
            recieved.append([weapon_tier, weapon_type])
        else:
            weapon_type = random.choice(weapon_type_list)
            weapon_tier = random.choices(weapon_tier_list, weights=weight)
            recieved.append([weapon_tier, weapon_type])


    return recieved


def weaponpull():
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
            Collect = weapon_banner(1,Guaranteed_4, Guaranteed_5)
            print("you got ", Collect[0][0],"-star ", Collect[0][1])
            if Guaranteed_4 >= 10:
                Guaranteed_4 = 0
            if Guaranteed_5 >= 90:
                Guaranteed_5 = 0

        elif DChoice == 2:
            total += 10
            Guaranteed_5 += 10
            Collect10 = weapon_banner(10,Guaranteed_4, Guaranteed_5)
            for result in Collect10:
                print("You got", result[0], "-star", result[1])
            if Guaranteed_4 >= 10:
                Guaranteed_4 = 0
            if Guaranteed_5 >= 90:
                Guaranteed_5 = 0

        elif DChoice == 3:
            break


