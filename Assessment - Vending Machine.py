while True: #creates a while loop, allowing repeatability in the code
    product_list = ['KitKat', 'Twix', 'Water', 'Soda'] #creates a list of the items
    price_list = [2.00, 2.50, 1.00, 2.50] #creates a list of the item prices
    item_code = [1111, 1112, 2111, 2112] #creates a list for the codes needed to receive the items from the vending machine

    zipped_list = zip (product_list, price_list, item_code) #zips the all three of the lists together
    vendMach = list (zipped_list) #sotres the zipped lists as one list

    print (vendMach) #prints the zipped list

    while True: #creates a while loop
        userInput_1 = int(input("\nPlease Select a product: (input the product code): ")) #allows user to input the product code

        if userInput_1 == 1111: #if statement if the user selects '1111'
            while True:
                payment = int(input("\nInsert Payment: ")) #asks the user to input their payment

                if payment < price_list[0]: #if statement if the user didn't input enough money
                    print ("\nI'm sorry, but the amount you entered is not sufficient for the product, please try again.")
                    continue

                else:
                    break

            change = payment - price_list[0] #simple operator to calculate the user's change

            print (f"\nHere is your {product_list[0]} and a change of {change} AED.") #prints the received product and change
            break

        elif userInput_1 == 1112:
            while True:
                payment = int(input("\nInsert Payment: "))
                
                if payment < price_list[1]:
                    print ("\nI'm sorry, but the amount you entered is not sufficient for the product, please try again.")
                    continue

                else:
                    break

            change = payment - price_list[1]

            print (f"\nHere is your {product_list[1]} and a change of {change} AED.")
            break

        elif userInput_1 == 2111:
            while True:
                payment = int(input("\nInsert Payment: "))
                
                if payment < price_list[2]:
                    print ("\nI'm sorry, but the amount you entered is not sufficient for the product, please try again.")
                    continue

                else:
                    break

            change = payment - price_list[2]

            print (f"\nHere is your {product_list[2]} and a change of {change} AED.")
            break

        elif userInput_1 == 2112:
            while True:
                payment = int(input("\nInsert Payment: "))
                
                if payment < price_list[3]:
                    print ("\nI'm sorry, but the amount you entered is not sufficient for the product, please try again.")
                    continue

                else:
                    break

            change = payment - price_list[3]

            print (f"\nHere is your {product_list[3]} and a change of {change} AED.")
            break

        else: #lets the user know they didn't input the right code
            print ("\nSorry, but we what you inputted isn't one of our products, please try again")
            continue
    
    repeat = input("\nWould you like to buy something else? (y/n) \n") #asks the user if they want to buy something else from the vending machine

    if repeat == 'y': #lets the user buy another product
        continue

    else: #ends the loop
        break
