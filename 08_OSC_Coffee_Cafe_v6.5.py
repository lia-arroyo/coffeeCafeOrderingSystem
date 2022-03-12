# OSC Coffee Cafe Version 5
# Post Usability Testing
# Created: 23/10/18

''' version 2 - post usability testing:
    - Add simplest instructions
        - to enter order number only
        - sugar (Y OR N)
        - explain how free coffee works

    v3:
    - Formatting display of menu and order

    v4:
    - Making output look neater
    - making code more efficient

    v5:
    - turning code into a function

    v6:
    - limiting number of coffees 
    
    '''


''' modules'''
import random


'''functions'''

def main_func():

    # integer + float checker
    def intcheck(question, low, high = None, isfloat = None):

        # error messages
        if high is not None and isfloat is None: # if there is an upper bound 
            error = "Please enter an integer between {} and {} (inclusive)".format(low,high)
            
        elif high is None and isfloat is None: # if there isn't an upper bound
            error = "Please enter an integer that is equal to/more than {}".format(low)

        elif high is None and isfloat is not None: # for payment - can be float
            error = "The total price is ${:.2f}. You didn't pay enough.".format(low)
        else:
            error = "Please enter a valid integer."

        while True:

            try:
                if isfloat is None: # if not float
                    response = int(input(question))

                else: # for payment, if isfloat is not None
                    response = float(input(question))

                # checks response is not too low
                if response < low:
                    print(error)
                    continue

                # checks response is not too high
                if high is not None and response > high:
                    print(error)
                    continue

                return response
            
            except ValueError: 
                print(error)
                continue

    # statement decorator func
    def cc_statement(statement, statement2, statement3, char):
        print(char*(len(statement2)+4))
        print(statement.center(len(statement2)+4))
        print(statement2.center(len(statement2)+4))
        print(statement3.center(len(statement2)+4))
        print(char*(len(statement2)+4))


    ''' main routine '''
    # opening statement
    print("~" * 31)
    print("WELCOME TO OSC COFFEE CAFE!".center(31)) 
    print("~" * 31)

    # menu

    menu = [["Flat White",3.00], \
            ["Cappuccino",3.00], \
            ["Latte",3.50], \
            ["Decaf",3.00], \
            ["Hot Chocolate",4.00] \
            ]

    # displaying menu
    print("-" * 9, "MENU", "-" * 9)
    num = 0
    for i in menu:
        num += 1 # numbers the menu
        print("{}. {:<13} | ${:.2f}".format(num, i[0], i[1])) #num, drink, price
    print("-" * 24)
    print()

    # order name
    while True:
        order_name = input("Order name: ").title()

        if order_name == "": # if order_name is blank, ensures users add a name
            print("Please enter an order name.")
            continue
        else:
            break


    # initializing variables 
    order = [] # user's order
    free = 0 # free coffee counter

    # asks user how many coffee they'd like

    coffee_num = intcheck("How many coffees? ", 1, 10)
    print()
    print("Enter the coffee number based on the MENU. E.g. 3 - Latte")# informs users about coffee number
    print()

    # generates coffee choice 
    for item in range(1, coffee_num + 1): # starts at 1 so that order_num starts at 1
        order_num = intcheck("Coffee choice {}: ".format(item), 1, 5) # menu is 1-5
        # matches order_num to menu

        # asks for sugar for every coffee
        sugar_count = input("Sugar? 'Y' for yes or 'N' for no. ").lower()

        sugar = 0 # starts off with 0 sugar

        if sugar_count == "y":
            sugar += 1 # adds a sugar if user wants one 
        
        # displaying key - drink & price of drink from menu
        
        drink = menu[order_num - 1][0] 
        price = menu[order_num - 1][1]

        # random number
        free_coffee = random.randint(1,5)

        if free == 0 and free_coffee == order_num:
            cc_statement("!!! FREE COFFEE !!!", "You matched the random generated",\
                         "free coffee number! Congrats!", "-")
            free += 1
            price = 0.00 #turns price to $0.00 (free)

        #adds coffee (drink and price) to order list)
        coffee = [drink, price, sugar] # one coffee = drink name, price for drink, and sugar or no sugar
        order.append(coffee) # adds coffee 
            
        # matches order_num to menu
        coffee_type = print("Drink: {} | ${:.2f} | {} Sugar".format(drink, price, sugar))
        print()

    # totalling order
        
    # total price

    # list comprehension - states that every [1] in second list is price
    final_price = [i[1] for i in order]
    total_price = sum(final_price) # adds all the prices of each drink

    # displaying order

    print("Order Name: {}".format(order_name))
    print("-" * 31)
    for i in order: # prints order
        print("{:<13} | {} Sugar | ${:.2f}".format(i[0], i[2], i[1])) #prints drink, sugar/no sugar, price
    print("-" * 31)
    print()
    print("Total order price: ${:.2f}".format(total_price))

    # payment

    payment = intcheck("Payment? $", total_price, None, 1) # input must be higher than total price
                                                        # no high limit, and can be a float
    # change

    change = payment - total_price

    print("Change: ${:.2f}".format(change))
    print()
    cc_statement("Thank you!", "   O S C | C O F F E E | C A F E   ", "Enjoy your Coffee", "~")


main_func()
