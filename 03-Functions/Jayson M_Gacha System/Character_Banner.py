import random
print('Character Banner')
print('Draw 1x')
print('Draw 10x')
five_star= ['Jean','Deluc','Venti','Klee','Mona','Xiao','Qiqi','Keqing']
four_star= ['Amber','Lisa','Kaeya','Barbara','Razor','Bennet','Noele','Fischl','Sucrose','Beidou','Ningguang','Xiangling','Xingqiu','Chongyun']
three_star= ["Sword", "Spear", "Halberd", "Pike", "Bow", "Gun", "Hammer", "Axe", "Kunai", "Shuriken", "Great Sword(2-handed)", "Greathammer(2-handed)", "Throwing Knife", "Staff", "Scepter"]
tier=['star3','star4','star5']
def pull():
    cnt=0
    pull = 0
    while True:
        ans = input('Do You Want To Draw? (Yes or No): ')
        if ans.lower() == 'yes':
            pull = int(input('Please Choose The Amount of Draws(1 or 10): '))

            if (pull == 1):
                chara_tier = random.choices(tier, weights=(80, 15, 1), k=1)
                if chara_tier == ['star3']:
                    range = random.randint(0, 14)
                    print('You Got',chara_tier, three_star[range])
                elif chara_tier == ['star4']:
                    range = random.randint(0, 13)
                    print('You Got',chara_tier, four_star[range])
                elif chara_tier == ['star5']:
                    range = random.randint(0, 7)
                    print('You Got',chara_tier, five_star[range])
            elif (pull == 10):
                chara_tier = random.choices(tier, weights=(0, 15, 1), k=1)
                if chara_tier == ['star4']:
                    range = random.randint(0, 13)
                    print('You Got',chara_tier, four_star[range])
                elif chara_tier == ['star5']:
                    range = random.randint(0, 7)
                    print('You Got',chara_tier, five_star[range])
                ctr = 0
                while (ctr < 9):
                    chara_tier = random.choices(tier, weights=(80, 15, 1), k=1)
                    if chara_tier == ['star3']:
                        range = random.randint(0, 14)
                        print('You Got',chara_tier, three_star[range])
                    elif chara_tier == ['star4']:
                        range = random.randint(0, 13)
                        print('You Got',chara_tier, four_star[range])
                    elif chara_tier == ['star5']:
                        range = random.randint(0, 7)
                        print('You Got',chara_tier, five_star[range])
                    ctr += 1
            print('Total Pull:', cnt)
        if ans.lower() == 'no':
            print('Congratulation on your reward(s)!')
            break

        cnt+=pull
        if (cnt>90) and ans.lower() == "yes":
            print('Total Pull:',cnt)
            pull = int(input('Please Choose The Amount of Draws(1 or 10): '))
            if (pull == 1):
                chara_tier = random.choices(tier, weights=(0, 0, 1), k=1)
                if chara_tier == ['star5']:
                    range = random.randint(0, 7)
                    print('You Got', chara_tier, five_star[range])
            elif (pull == 10):
                chara_tier = random.choices(tier, weights=(0, 0, 1), k=1)
                if chara_tier == ['star5']:
                    range = random.randint(0, 7)
                    print('You Got',chara_tier, five_star[range])
                ctr = 0
                while (ctr < 9):
                    chara_tier = random.choices(tier, weights=(80, 15, 1), k=1)
                    if chara_tier == ['star3']:
                        range = random.randint(0, 14)
                        print('You Got',chara_tier, three_star[range])
                    elif chara_tier == ['star4']:
                        range = random.randint(0, 13)
                        print('You Got',chara_tier, four_star[range])
                    elif chara_tier == ['star5']:
                        range = random.randint(0, 7)
                        print('You Got',chara_tier, five_star[range])
                    ctr += 1
        elif ans.lower() =="no":
            print('Congratulation on your reward(s)!')
            break
            cnt=0




