menu_food= ['Pizza','Noodles','Chicken']
price = [10,5,4.50]
menu_final=dict(zip(menu_food,price))
print(menu_final)


choice = input('take your order').lower()

def pizzatoppings():
    choiceoftoppings=''
    toppings = ['Pepperoni','Mushrooms','Anchovies']
    print('Here are the toppings!')
    print(toppings)
    topchoice = input('Chose your toppings').lower()

    if topchoice == toppings[0].lower() :
        choiceoftoppings = 'Pepperoni'


    elif topchoice == toppings[1].lower() :
        choiceoftoppings = 'Mushrooms'


    elif topchoice == toppings[2].lower() :
        choiceoftoppings = 'Anchovies'


    else :
        print('You want no toppings')


    return choiceoftoppings




def noddletype():
    noodlesize=['Ramen','Udon','PhaThai']
    choiceoftype = ''
    print('These are the noodles:', noodlesize)
    choicenoodle=input('Make your choice').lower()
    if choicenoodle == noodlesize[0].lower():
        choiceoftype = 'Ramen'
    elif choicenoodle == noodlesize[1].lower():
        choiceoftype = 'Udon'
    elif choicenoodle == noodlesize[2].lower():
        choiceoftype = 'PhaThai'
    return choiceoftype




if choice == menu_food[0].lower():
    print('Your order is pizza with',pizzatoppings() , ', which costs $'+ str(price[0]) )
elif choice == menu_food[1].lower():
    print('Your order is',noddletype(),' which cost ${}'.format(str(price[1])))
elif choice == menu_food[2].lower():
    print('Your order is '+menu_food[2],'which costs $'+str(price[2]))
