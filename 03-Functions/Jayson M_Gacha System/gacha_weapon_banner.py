import random
from typing import List

total = 0
pity10 = 0
pity90 = 0

def weapon_banner(n):
    global pity10, pity90, total
    weapon_type_list = ["Sword", "Spear", "Halberd", "Pike", "Bow", "Gun",
                        "Hammer", "Axe", "Kunai", "Shuriken", "Great Sword(2-handed)",
                        "Greathammer(2-handed)", "Throwing Knife", "Staff", "Scepter"]
    weapon_tier_list = [3, 4, 5]
    weapon_type: List[str]
    weapon_tier: List[str]
    weight = (80, 15, 1)
    recieved = []


    if n == 10: #ten pulls\
        if pity90 >= 90:
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
        pity90 += 10
        total += 10

    elif n == 1: #single pull
        if pity90 >=90:
            weapon_type = random.choice(weapon_type_list)
            weapon_tier = [5]
            recieved.append([weapon_tier, weapon_type])
        elif pity10 >= 10:
            weapon_type = random.choice(weapon_type_list)
            weapon_tier = [4]
            recieved.append([weapon_tier, weapon_type])
        else:
            weapon_type = random.choice(weapon_type_list)
            weapon_tier = random.choices(weapon_tier_list, weights=weight)
            recieved.append([weapon_tier, weapon_type])
        pity10 += 1
        pity90 += 1
        total += 1

    for result in range(len(recieved)):
        print("You got", recieved[result][0], "-star", recieved[result][1])

def weaponpull():
    while True:
        print("welcome to the weapon banner")
        print("-----------------------------------")
        print("total pulls = ", total)
        print("-----------------------------------")
        print("Your Choice of")
        print("1. 1x Draw")
        print("2. 10x Draw")
        print("type '3' to go back")
        print("-----------------------------------")
        DChoice = eval(input("Draw choice = "))
        if DChoice == 1:
            weapon_banner(1)
        elif DChoice == 2:
            weapon_banner(10)
        elif DChoice == 3:
            break
