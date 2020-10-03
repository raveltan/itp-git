import os

stp_order = False
foods = ["Fried rice", "Porridge", "Nasi Lemak"]
food_price = [25000, 30000, 35000]
drinks = ["Ice tea", "Teh tarik", "Orange Juice"]
drink_price = [3000, 10000, 15000]
desserts = ["Es Campur", "Es Kacang", "Kolak"]
dessert_price = [25000, 30000, 35000]
receipt_items = []
receipt_prices = []
#                ----Greeting----
print("Welcome to the restaurant")


#                ----Menu----
def menu():
    while not stp_order:
        print(" \n 1.Food \n 2.Drinks \n 3.Dessert \n 4.Place Order\n")
        options = int(input("What section would you like to go:"))

        if options == 1:
            print(f"{'Food':^10}{'Price(RP.)':>15}")
            for food in range(len(foods)):
                print(food + 1, foods[food], "\t", food_price[food])
            order = int(input("\nPlease order here :"))

            if order == 1:
                receipt_items.append(foods[0])
                receipt_prices.append(food_price[0])

            elif order == 2:
                receipt_items.append(foods[1])
                receipt_prices.append(food_price[1])

            elif order == 3:
                receipt_items.append(foods[2])
                receipt_prices.append(food_price[2])

            else:
                print("Invalid order Number")
                order = input("\nPlease order here :")

        elif options == 2:
            print(f"{'Drink':<10}{'Price(RP.)':>15}")
            for drink in range(len(drinks)):
                print(drink + 1, drinks[drink], "\t", drink_price[drink])
            order = int(input("\nPlease order here :"))

            if order == 1:
                receipt_items.append(drinks[0])
                receipt_prices.append(drink_price[0])

            elif order == 2:
                receipt_items.append(drinks[1])
                receipt_prices.append(drink_price[1])

            elif order == 3:
                receipt_items.append(drinks[2])
                receipt_prices.append(drink_price[2])
            else:
                print("Invalid order Number")
                order = input("\nPlease order here :")

        elif options == 3:
            print(f"{'Dessert':<10}{'Price(RP.)':>15}")
            for dessert in range(len(desserts)):
                print(dessert + 1, desserts[dessert], "\t", dessert_price[dessert])
            order = int(input("\nPlease order here :"))
            if order == 1:
                receipt_items.append(desserts[0])
                receipt_prices.append(dessert_price[0])

            elif order == 2:
                receipt_items.append(desserts[1])
                receipt_prices.append(dessert_price[1])

            elif order == 3:
                receipt_items.append(desserts[2])
                receipt_prices.append(dessert_price[2])
            else:
                print("Invalid order Number")
                order = input("\nPlease order here :")
        elif options == 4:
            print("Items Ordered\t\t Price(RP.)")
            for receipt in range(len(receipt_items)):
                print(receipt+1, ".", receipt_items[receipt], "\t\t", receipt_prices[receipt])
            print("Total:\t\t", sum(receipt_prices))


menu()
