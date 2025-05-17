"""This component displays the menu for a gift hamper establishment program"""

#import pandas library
import pandas as pd

#list of hamper names
hamper_names = ['Birthday Bliss', 'Get Well Soon', 'Luxury Gourmet', 'New Baby Hamper', 
                                   'Eco-Friendly Hamper', 'Home Sweet Home Hamper', 'A Little Thank You Basket', 
                                   'Chocolate Selection Box', 'Mini Wine Bottle', 'Cheese Wedges', 'Tea Sampler', 'Coffee Beans',
                                   'Scented Candle', 'Bath Bomb', 'Face Mask', 'Essential Oil',
                                   'Stuffed Toy', 'Handwritten Card', 'Gift Wrapping', 'Reusable Basket',
                                   'Baby Booties', 'Teething Toy', 'Baby Shampoo', 'Soft Pacifier']
#list of hamper prices
hamper_prices = [49.99, 39.99, 89.99, 59.99, 44.99, 59.99, 49.99, 
                 12.00, 15.00, 10.00, 8.00, 11.00,
                 9.00, 6.00, 5.00, 7.00,
                 10.00, 3.00, 5.00, 6.00, 
                 8.00, 6.00, 7.00, 5.00] 

#list to store ordered hampers
order_list = [] 
#list to store hamper prices
order_cost = [] 


#create premade_hamper_menu function
def premade_hamper_menu():
    #create menu dictionary
    menu_dict = {}

    #format hamper prices as currency
    pd.options.display.float_format = '${:,.2f}'.format 

    #add premade hamper numbers to dictionary
    menu_dict ['Number'] = [1,2,3,4,5,6,7]

    #add premade hamper names to dictionary
    menu_dict ['Premade Hampers'] = ['Birthday Bliss', 'Get Well Soon', 'Luxury Gourmet', 'New Baby Hamper', 
               'Eco-Friendly Hamper', 'Home Sweet Home Hamper', 'A Little Thank You Basket']

    #add premade hamper blank column to dictionary
    menu_dict [""] = ["","","","","","",""]

    #add premade hamper prices to dictionary 
    menu_dict ['Price'] = [49.99, 39.99, 89.99, 59.99, 44.99, 59.99, 49.99] 

    #display menu dataframe
    df = pd.DataFrame(menu_dict) 
    blankIndex = [''] * len(df) 
    df.index = blankIndex 

    print()
    print("Premade Hamper Menu: Please order using the menu item's number \n \n",df) 
    print()


#create custom_hamper_menu function
def custom_hamper_menu():
    #create menu dictionary
    menu_dict = {}

    #format hamper prices as currency
    pd.options.display.float_format = '${:,.2f}'.format 

    #add custom hamper numbers to dictionary
    menu_dict ['Number'] = [8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

    #add custom hamper item names to dictionary
    menu_dict ['Custom Hamper Items'] = ['Chocolate Selection Box', 'Mini Wine Bottle', 'Cheese Wedges', 'Tea Sampler', 'Coffee Beans',
                                    'Scented Candle', 'Bath Bomb', 'Face Mask', 'Essential Oil',
                                    'Stuffed Toy', 'Handwritten Card', 'Gift Wrapping', 'Reusable Basket',
                                    'Baby Booties', 'Teething Toy', 'Baby Shampoo', 'Soft Pacifier']

    #add custom hamper blank column to dictionary
    menu_dict [""] = ["","","","","","","","","","","","","","","","",""]

    #add custom hamper prices to dictionary 
    menu_dict ['Price'] = [12.00, 15.00, 10.00, 8.00, 11.00,
                        9.00, 6.00, 5.00, 7.00,
                        10.00, 3.00, 5.00, 6.00, 
                        8.00, 6.00, 7.00, 5.00] 
    
    #display menu dataframe
    df = pd.DataFrame(menu_dict) 
    blankIndex = [''] * len(df) 
    df.index = blankIndex 

    print()
    print("Custom Hamper Menu: Please order using the menu item's number \n \n",df) 
    print()

premade_hamper_menu()
custom_hamper_menu()

#create hamper order function for boundaries
def hamper_order():
    num_hampers = 0
    while True: 
        try:
            num_hampers = int(input("How many hampers do you want to order? "))
            if num_hampers >=1 and num_hampers <= 5:
                break
            else:
                print("Your order must be between 1 and 5 hampers")
        
        except ValueError: 
            print("This is not a valid number")

    print(num_hampers)

    #choose hampers from the menu
    print("Please choose hamper(s) from the menu") 
    for item in range(num_hampers): 
        while num_hampers > 0: 
            while True:
                try:
                    hampers_ordered = int(input()) 
                    if hampers_ordered >=1 and hampers_ordered <= 24:
                        break
                    else:
                        print("Your hamper order must be between 1 and 24")
                except ValueError: 
                    print("That is not a valid number")

            hampers_ordered = hampers_ordered-1
            order_list.append(hamper_names[hampers_ordered]) 
            order_cost.append(hamper_prices[hampers_ordered]) 
            print("{} ${:.2f}".format(hamper_names[hampers_ordered], hamper_prices[hampers_ordered]))
            num_hampers = num_hampers-1

    print(order_list)
    print(order_cost)

hamper_order()