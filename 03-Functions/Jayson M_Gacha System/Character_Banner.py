import random
print('Character Banner')
print('Draw 1x')
print('Draw 10x')
aaaaa= ['Jean','Deluc','Venti','Klee','Mona','Xiao','Qiqi','Keqing']
aaaa= ['Amber','Lisa','Kaeya','Barbara','Razor','Bennet','Noele','Fischl','Sucrose','Beidou','Ningguang','Xiangling','Xingqiu','Chongyun']
aaa= ["Sword", "Spear", "Halberd", "Pike", "Bow", "Gun", "Hammer", "Axe", "Kunai", "Shuriken", "Great Sword(2-handed)", "Greathammer(2-handed)", "Throwing Knife", "Staff", "Scepter"]
tier=['star3','star4','star5']
def pull():
    cnt=0
    while True:
        ans = input('Do You Want To Draw? (Yes or No): ')
        if ans.lower() == 'yes':
            pull = int(input('Please Choose The Amount of Draws(1 or 10): '))
            if (pull == 1):
                chara_tier = random.choices(tier, weights=(80, 15, 1), k=1)
                if chara_tier == ['star3']:
                    a = random.randint(0, 14)
                    print('You Got', chara_tier, aaa[a])
                elif chara_tier == ['star4']:
                    a = random.randint(0, 13)
                    print('You Got', chara_tier,aaaa[a])
                elif chara_tier == ['star5']:
                    a = random.randint(0, 7)
                    print('You Got', chara_tier, aaaaa[a])
            elif (pull == 10):
                chara_tier = random.choices(tier, weights=(0, 15, 1), k=1)
                if chara_tier == ['star4']:
                    a = random.randint(0, 13)
                    print('You Got', chara_tier, aaaa[a])
                elif chara_tier == ['star5']:
                    a = random.randint(0, 7)
                    print('You Got', chara_tier, aaaaa[a])
                ctr = 0
                while (ctr < 9):
                    chara_tier = random.choices(tier, weights=(80, 15, 1), k=1)
                    if chara_tier == ['star3']:
                        a = random.randint(0, 14)
                        print('You Got', chara_tier,aaa[a])
                    elif chara_tier == ['star4']:
                        a = random.randint(0, 13)
                        print('You Got', chara_tier,aaaa[a])
                    elif chara_tier == ['star5']:
                        a = random.randint(0, 7)
                        print('You Got', chara_tier,aaaaa[a])
                    ctr += 1
        if ans.lower() == 'no':
            print('Congratulation on your reward(s)!')
            break

        cnt+=pull
        if (cnt<90):
            print('Total Pull:',cnt)
        else:
            ans = input('Do You Want To Draw? (Yes or No): ')
            if ans.lower() == 'yes':
                pull = int(input('Please Choose The Amount of Draws(1 or 10): '))
                if (pull == 1):
                    chara_tier = random.choices(tier, weights=(0, 0, 1), k=1)
                    if chara_tier == ['star5']:
                        a = random.randint(0, 7)
                        print('You Got', aaaaa[a])
                elif (pull == 10):
                    chara_tier = random.choices(tier, weights=(0, 0, 1), k=1)
                    if chara_tier == ['star5']:
                        a = random.randint(0, 7)
                        print('You Got', aaaaa[a])
                    ctr = 0
                    while (ctr < 9):
                        chara_tier = random.choices(tier, weights=(80, 15, 1), k=1)
                        if chara_tier == ['star3']:
                            a = random.randint(0, 14)
                            print('You Got', aaa[a])
                        elif chara_tier == ['star4']:
                            a = random.randint(0, 13)
                            print('You Got', aaaa[a])
                        elif chara_tier == ['star5']:
                            a = random.randint(0, 7)
                            print('You Got', aaaaa[a])
                        ctr += 1
            else:
                print('Congratulation on your reward(s)!')
                break
            cnt=0




