import JaysonMGachaSystem.Character_Banner as chara
import JaysonMGachaSystem.gacha_weapon_banner as weap
import JaysonMGachaSystem.standardbanner as stand

def Draw():
    print("---Welcome to the poorly made Gacha System---")
    print("Made by Jayson M, Bernard W, Eric LK, Leon J")
    print("---------------------------------------------")
    print("Your choice of banner includes: ")
    print("---------------------------------------------")
    print("""1. Character Banner
2. Weapon Banner
3. Standard Banner
4. Quit""")
    print("---------------------------------------------")



while True:
    Draw()

    BChoice = eval(input("Your Choice of Banner = "))
    if BChoice == 1:
        chara.pull()
    elif BChoice == 2:
        weap.weaponpull()
    elif BChoice == 3:
        stand.StandardDraw()
    elif BChoice == 4:
        print("--------------------------------------------------")
        print("Thank you for using this Poorly made Gacha System!")
        break


