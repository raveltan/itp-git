print('Welcome to The Lottery Shop!')
print('1 roll ticket : 1$')
print('2 roll ticket : 0.75$ each')
print('3 roll ticket and more : 0.5$ each')
buy=input('Please Input the Amount of Roll Ticket You Would Like to Buy: ')
print('')
print('You have succesfully bought',buy+' ticket(s)' )
print('Do you want to roll your ticket(s) now? ')
ans=input('Answer Yes Or No: ')
if (ans=='Yes'):
    num=int(input('Please input amount of ticket(s) to roll: '))
    print(' ')
    list=['Tissue','Tissue','Tissue','sandals','sandals','Coupon','Fridge','Microwave','TV', 'Trip to Hawaii']
    import random
    a=1
    b = 0
    while(b<=num):
        a = random.randint(0,9)
        if(b==num):
            break
        else:
            print('Here is your lucky number:',a)
            print('Congratulations, you got a', list[a])
        b+=1
    print(' ')
    print('Thankyou for Using Our Service!')
else:
    print('Thankyou for Using Our Service!')



